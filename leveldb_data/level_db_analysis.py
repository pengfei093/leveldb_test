import os
import signal

import plyvel


def create_leveldb(db_path, create_if_missing):
    # leveldb.RepairDB(db_path)
    db = plyvel.DB(db_path, create_if_missing=True, compression=None)
    # db = plyvel.DB('/tmp/t', create_if_missing=True)
    return db


def hist_level_db_size(current_leveldb):
    # sn = current_leveldb.snapshot()
    # b = sn.get(b'key')
    it = current_leveldb.iterator(include_value=False)
    print(it)
    print(next(it))
    for key, value in current_leveldb:
        print(key)
        print(value)
    current_leveldb.close()


class LevelDBAnalysis:
    def __init__(self, conf):
        self.conf = conf
        self.files_paths_list = os.listdir(self.conf['leveldb_path'])

    def start(self):
        for file_path in self.files_paths_list:
            if file_path.endswith('_data'):
                leveldb_address = self.conf['leveldb_path'] + '/' + file_path
                current_leveldb = create_leveldb(leveldb_address, False)
                hist_level_db_size(current_leveldb)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    print(1)
    # conf = load_configs_from_files("../conf/leveldb_config.yaml")
    # leveldb_test = LevelDBAnalysis(conf)
    # leveldb_test.start()
