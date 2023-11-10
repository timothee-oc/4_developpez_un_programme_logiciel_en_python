from json import dump, load
from os import path, makedirs, listdir

PLAYERS_DIR = "data/players/"
TOURNAMENTS_DIR = "data/tournaments/"


def create_data_dirs():
    if not path.exists(PLAYERS_DIR):
        makedirs(PLAYERS_DIR)
    if not path.exists(TOURNAMENTS_DIR):
        makedirs(TOURNAMENTS_DIR)


def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as fp:
        dump(data, fp, ensure_ascii=False, indent=4)


def extract_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as fp:
        data = load(fp)
    return data


def list_data_files(files_dir):
    files_list = listdir(files_dir)
    return files_list
