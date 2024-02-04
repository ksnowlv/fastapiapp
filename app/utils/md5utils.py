import hashlib


# 获取本地文件的 md5 值
def md5_by_file_path(file_path):
    with open(file_path, 'rb') as f:
        m = hashlib.md5()
        while True:
            data = f.read(1024 * 1024)
            if not data:
                break
            m.update(data)
    return m.hexdigest()


def md5_by_string(data: str):
    md5 = hashlib.md5()
    md5.update(data.encode('utf-8'))
    return md5.hexdigest()


def md5_by_data(data: bytes):
    md5 = hashlib.md5()
    md5.update(data)
    return md5.hexdigest()
