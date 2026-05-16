#!/usr/bin/env python3
"""Sync shared reference files into self-contained skill packages."""

from __future__ import annotations

import argparse
import filecmp
import json
import shutil
import sys
from pathlib import Path

DEFAULT_CONFIG = Path("skills/common/reference-sync.json")


def parse_pair(value: str) -> tuple[Path, Path]:
    if ":" not in value:
        raise argparse.ArgumentTypeError(
            "expected SOURCE:DEST, for example "
            "skills/common/bkn-methodology.md:skills/bkn-requirement/references/bkn-methodology.md"
        )
    source, dest = value.split(":", 1)
    if not source or not dest:
        raise argparse.ArgumentTypeError("SOURCE and DEST must both be non-empty")
    return Path(source), Path(dest)


def load_config(path: Path) -> list[tuple[Path, Path]]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"config not found: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON in {path}: {exc}")

    copies = data.get("copies")
    if not isinstance(copies, list):
        raise SystemExit(f"{path} must contain a top-level 'copies' list")

    pairs: list[tuple[Path, Path]] = []
    for index, item in enumerate(copies, start=1):
        if not isinstance(item, dict):
            raise SystemExit(f"{path}: copies[{index}] must be an object")

        source = item.get("source")
        dest = item.get("dest")
        if not isinstance(source, str) or not isinstance(dest, str):
            raise SystemExit(f"{path}: copies[{index}] requires string 'source' and 'dest'")

        pairs.append((Path(source), Path(dest)))

    return pairs


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Copy shared methodology/reference files into skill-local references so "
            "single-skill distribution remains self-contained."
        )
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG,
        help=f"JSON registry of copy relationships. Defaults to {DEFAULT_CONFIG}.",
    )
    parser.add_argument(
        "--copy",
        dest="copies",
        action="append",
        type=parse_pair,
        metavar="SOURCE:DEST",
        help="Add an ad hoc source-to-destination copy in addition to the registry.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Do not write files; fail if any destination is missing or differs.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be copied without writing files.",
    )
    args = parser.parse_args()

    copies = load_config(args.config)
    if args.copies:
        copies.extend(args.copies)
    if not copies:
        print(f"no copy entries found in {args.config}", file=sys.stderr)
        return 1

    failed = False

    for source, dest in copies:
        if not source.is_file():
            print(f"missing source: {source}", file=sys.stderr)
            failed = True
            continue

        same = dest.is_file() and filecmp.cmp(source, dest, shallow=False)

        if args.check:
            if same:
                print(f"ok: {source} == {dest}")
            else:
                reason = "missing" if not dest.exists() else "differs"
                print(f"out of sync ({reason}): {source} -> {dest}", file=sys.stderr)
                failed = True
            continue

        if same:
            print(f"unchanged: {dest}")
            continue

        print(f"copy: {source} -> {dest}")
        if not args.dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, dest)

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
