# coding=utf-8
""" Init file for the core tests """
import os
import shutil
from pathlib import Path
import parac

parac.logging.init_rich_console()
prev_input = parac.logging.get_rich_console().input
parac.logging.set_avoid_print_banner_overwrite(True)
cwd = Path(os.getcwd()).resolve()


def overwrite_builtin_input(overwrite: str):
    """ Overwrites the input with a lambda that returns the specified value """
    getattr(parac.logging, 'output_console').input =\
        lambda *args, **kwargs: overwrite


def reset_input():
    """ Resets the output method of the console object """
    getattr(parac.logging, 'output_console').input = prev_input


def add_folder(folder_name: str) -> str:
    """
    Removes any pre-existing data if it exists and adds the folder

    :returns: The path of the folder
    """
    remove_folder(folder_name)
    os.mkdir(p := cwd / folder_name)
    return str(p)


def remove_folder(folder_name: str):
    """ Removes the build and dist folder if they exist """
    path: Path = cwd / folder_name
    if os.path.exists(path):
        shutil.rmtree(str(path.resolve()))

    counter = 2
    while os.path.exists(path := cwd / f"{folder_name}_{counter}"):
        shutil.rmtree(str(path.resolve()))
        counter += 1


def create_test_file(folder_name: str, file_name: str):
    """ Creates a test file in the specified path with the specified name """
    with open(cwd / folder_name / file_name, 'w+') as file:
        file.write("x")
    assert os.path.exists(cwd / folder_name / file_name)
