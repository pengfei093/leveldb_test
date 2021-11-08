import os
import signal

import plyvel


def create_leveldb(leveldb_address, create_if_missing):
    db = plyvel.DB(leveldb_address, create_if_missing=False)
    return db


def hist_level_db_size(current_leveldb):
    # sn = current_leveldb.snapshot()
    # b = sn.get(b'key')
    it = current_leveldb.iterator(include_value=False)
    print(it)
    print(next(it))
    # for key, value in current_leveldb:


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    print(1)
    db_path = '/opt/aelladata/work/aella-scai/localstorage'
    files_paths_list = os.listdir(db_path)
    for file_path in files_paths_list:
        if file_path.endswith('_data'):
            leveldb_address = db_path + '/' + file_path
            current_leveldb = create_leveldb(leveldb_address, False)
            hist_level_db_size(current_leveldb)
            current_leveldb.close()
            break
