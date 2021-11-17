import sys

import redis


class RedisClien:
    def __init__(self, db=0):
        host = '192.168.3.229'
        passwd = 'Gi3d85028501'
        port = 6379
        self.host = host
        self.port = port
        self.passwd = passwd
        self.db = db
        self.client = redis.Redis(host=host, port=port, password=passwd, db=db, decode_responses=True)

    def get(self, key):
        return self.client.get(key)

    def set(self, key, value):
        return self.client.set(key, value)

    def close(self):
        return self.client.close()


if __name__ == '__main__':
    db = 0
    r = RedisClien(db)
    mode = getattr(r, sys.argv[1])
    print(mode(sys.argv[2], sys.argv[3])) if sys.argv[1] == 'set' else print(mode(sys.argv[2]))
    r.close()
