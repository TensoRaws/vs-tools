from __future__ import annotations

from vstools.stgpytools import (
    FileIsADirectoryError, FileNotExistsError, FilePermissionError, FileTypeMismatchError, FileWasNotFoundError
)

__all__ = [
    'FileNotExistsError',
    'FileWasNotFoundError',
    'FilePermissionError',
    'FileTypeMismatchError',
    'FileIsADirectoryError'
]
