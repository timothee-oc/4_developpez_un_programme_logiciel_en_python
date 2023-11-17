from json import dump, load
from os import path, makedirs, listdir

PLAYERS_DIR = "data/players/"
TOURNAMENTS_DIR = "data/tournaments/"


def create_data_dirs():
    """
    Used to create database directories if not already existing.
    """
    if not path.exists(PLAYERS_DIR):
        makedirs(PLAYERS_DIR)
    if not path.exists(TOURNAMENTS_DIR):
        makedirs(TOURNAMENTS_DIR)


def save_json(data, file_path):
    """
    Used to save some data in a file as a json format.
    Used to save tournaments and players data from the database. 
    """
    with open(file_path, 'w', encoding='utf-8') as fp:
        dump(data, fp, ensure_ascii=False, indent=4)


def extract_json(file_path):
    """
    Used to extract some data from a file in a json format.
    Used to extract tournaments and players data from the database.

    :return data(dict)
    """
    with open(file_path, 'r', encoding='utf-8') as fp:
        data = load(fp)
    return data


def list_data_files(files_dir):
    """
    Used to get a list of the files in a given directory.
    Used when searching for a specific player/tournament in the database
    or when generating a report of all players/tournaments in database.
    """
    files_list = listdir(files_dir)
    return files_list
