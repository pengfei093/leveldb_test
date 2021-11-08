import os
import signal

import plyvel

values = []


def create_leveldb(leveldb_address, create_if_missing):
    db = plyvel.DB(leveldb_address, create_if_missing=False)
    return db


def hist_level_db_size(current_leveldb):
    for key, value in current_leveldb:
        values.append(len(value))


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    db_path = 'localstorage'
    files_paths_list = os.listdir(db_path)
    for file_path in files_paths_list:
        if file_path.endswith('_data') or file_path.endswith('_data'):
            leveldb_address = db_path + '/' + file_path
            current_leveldb = create_leveldb(leveldb_address, False)
            hist_level_db_size(current_leveldb)
            mean = sum(values) / len(values)
            variance = sum([((x - mean) ** 2) for x in values]) / len(values)
            res = variance ** 0.5
            print("Mean of sample is : " + str(mean))
            print("Standard deviation of sample is : " + str(res))
            current_leveldb.close()
