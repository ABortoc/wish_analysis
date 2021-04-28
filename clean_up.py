import pathlib
import os


def screenshot_cleaning():
    cur_dir = pathlib.Path(__file__).parent.absolute()
    dir = f'{cur_dir}/screenshots'
    for file in os.scandir(dir):
        os.remove(file.path)
