from bson import ObjectId
from pymongo import MongoClient
import gridfs
from typing import Any

g_gridfs = None


class XGridFS(object):

    def __init__(self):
        self.fs = None
        pass

    def init_gridfs(self):
        # 连接到 MongoDB 数据库
        #client = MongoClient('mongodb://localhost:27017/')
        #docker下要使用Docker容器之间的连接，通常应该使用Docker的服务名称而不是localhost来指定主机名。在这里，应该将MongoDB服务器地址设为Docker容器的名称，即mongodb，而不是localhost
        client = MongoClient('mongodb://mongodb:27017/')
        db = client['my_database']
        self.fs = gridfs.GridFS(db, 'fs')
        print(f"XGridFS fs:{self.fs}")

    def put_file(self, file_content: Any, file_name: str):
        file_id = self.fs.put(file_content, filename=file_name)
        return file_id

    def find_file(self, file_id: str):
        return self.fs.get(ObjectId(file_id))

    def find_one(self, d: dict):
        file = self.fs.find_one(d)
        if file:
            return file

        return None

    def gridfs(self):
        return self.fs

    @staticmethod
    def shared_gridfs():
        global g_gridfs
        if not g_gridfs:
            g_gridfs = XGridFS()
            g_gridfs.init_gridfs()

        return g_gridfs
