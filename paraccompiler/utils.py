# coding=utf-8
""" Utility in the Para-C Compiler"""
import logging
import re
import os
from click.utils import WIN
from os import PathLike
from typing import Union, Type, Optional

__all__ = [
    'SEPARATOR',
    'decode_if_bytes',
    'cleanup_path',
    'escape_ansi',
    'check_valid_path_name',
    'get_relative_file_name',
    'SpecialBoolDefault'
]

logger = logging.getLogger(__name__)

SEPARATOR = "\\" if WIN else "/"
INVALID_UNIX_FILE_NAME_CHARS = ('/', '<', '>', '\0', '|', ':', '&')
INVALID_WIN_FILE_NAME_CHARS = ('<', '>', ':', '"', '/', '\\', '|', '?', '*')


def decode_if_bytes(
        byte_like: Union[str, bytes, PathLike, Type],
        encoding: str = "utf-8"
) -> Union[str, PathLike]:
    """ Decodes the passed PathLike if it is in bytes """
    if type(byte_like) is str:
        return byte_like
    elif type(byte_like) is bytes or isinstance(bytes, byte_like):
        return byte_like.decode(encoding)
    else:
        return byte_like


def cleanup_path(_p: str) -> str:
    """ Cleans the path for the specific current os """
    if WIN:
        _p = _p.replace("/", SEPARATOR).replace("\\\\", SEPARATOR)
    else:
        # UNIX path
        _p = _p.replace("\\", SEPARATOR).replace("\\\\", SEPARATOR)

    if _p.startswith(f".{SEPARATOR}"):
        _p = os.getcwd() + _p[1:]  # Replacing . with current directory
    return _p


def escape_ansi(string: str) -> str:
    """ Removes ansi colouring in the passed string """
    ansi_escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', string)


def check_valid_path_name(
        path: Union[str, PathLike],
        win_path: Optional[bool] = None
) -> bool:
    """
    Checks whether the name is a valid path-name. This means the file name
    cannot contain < , > , : , " , / , \\ (Escaped) , | , ? , *

    :param path: A path-like or file-name which should be checked
    :param win_path: If explicitly set to True, the path will be checked if it
                     was a windows path, even if it's a os of a different kind
    """
    path = cleanup_path(path)
    path = path.replace(SEPARATOR, '')

    if WIN or win_path:
        if path[1:].startswith(':'):
            path = path[2:]

        if path.endswith(' ') or path.endswith('.'):
            return False
        char_set = INVALID_WIN_FILE_NAME_CHARS
    else:
        char_set = INVALID_UNIX_FILE_NAME_CHARS

    count = 0
    for c in path:
        if 0 <= ord(c) < 28:  # Control chars are forbidden
            return False
        if c in char_set:
            return False
        count += 1
    return True


def get_relative_file_name(
        file_name: str,
        file_path: Union[str, PathLike],
        base_path: Union[str, PathLike],
        win_path: Optional[bool] = None
) -> str:
    """
    Gets the relative file name from the passed str. If the file_path does not
    match the file_name passed RuntimeError will be raised

    :param file_name: Simple file name which cannot contain < , > , : , " , / ,
                      \\ (Escaped) , | , ? , *
    :param file_path: Full path of the file
    :param base_path: Full base path for the working directory
    :param win_path: If explicitly set to True, the path will be checked if it
                     was a windows path, even if it's a os of a different kind
    """
    file_path = cleanup_path(file_path)
    base_path = cleanup_path(base_path)

    if base_path not in file_path:
        raise RuntimeError(
            "base_path and file_path are mismatching. file_path is not in "
            "base_path"
        )

    if ' ' in file_name:
        raise RuntimeError(
            "The Para-C naming conventions do not allow spaces in the filename"
        )

    relative_path = file_path.replace(base_path, '')
    if relative_path.startswith(SEPARATOR):
        relative_path = relative_path[len(SEPARATOR):]

    if not check_valid_path_name(file_path, win_path):
        raise RuntimeError(
            "The file_path contains invalid characters that can not be "
            "processed"
        )

    if not check_valid_path_name(base_path, win_path):
        raise RuntimeError(
            "The base_path contains invalid characters that can not be "
            "processed"
        )

    if relative_path.split(SEPARATOR)[-1] != file_name:
        raise RuntimeError(
            "Mismatching file_names (file_path and file_name do not match)"
        )

    relative_file_name = ""

    relative_elements = relative_path.split(SEPARATOR)[:-1]
    for elem in relative_elements:
        relative_file_name += "".join((elem, "."))

    relative_file_name += file_name.split('.')[0]
    return relative_file_name


class SpecialBoolDefault:
    """
    Special Bool serving to separate wanted flags with default flags
    """

    def __init__(self, value: bool):
        if type(value) is not bool:
            raise ValueError("Expected boolean")
        self.true_default: bool = bool(value)
        self.actual_value: bool = bool(value)

    def set(self, value):
        """ Sets the actual_value in the instance """
        if type(bool) is bool:
            self.actual_value = value
        else:
            raise ValueError("Expected boolean")

    def __eq__(self, other):
        return self.actual_value == other

    def __hash__(self):
        return hash(self.actual_value)

    def __bool__(self):
        return self.actual_value
