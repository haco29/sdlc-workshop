"""Load and save the poll as JSON. The only module that touches the disk."""

from __future__ import annotations

import json
from pathlib import Path

from poll.core import Poll

DEFAULT_PATH = Path("poll.json")


def load(path: Path | None = None) -> Poll | None:
    """Return the saved poll, or None when there isn't one yet."""
    path = path or DEFAULT_PATH
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def save(poll: Poll, path: Path | None = None) -> None:
    path = path or DEFAULT_PATH
    path.write_text(json.dumps(poll, indent=2, ensure_ascii=False), encoding="utf-8")


def clear(path: Path | None = None) -> None:
    (path or DEFAULT_PATH).unlink(missing_ok=True)
