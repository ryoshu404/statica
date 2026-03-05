import hashlib

class HashExtractor():

    def extract(self, data: bytes) -> dict:

        md5hash = hashlib.md5()
        md5hash.update(data)
        md5hashed = md5hash.hexdigest()
        sha256hash = hashlib.sha256()
        sha256hash.update(data)
        sha256hashed = sha256hash.hexdigest()
        hashes = {}
        hashes['md5'] = md5hashed
        hashes['sha256'] = sha256hashed
        
        return hashes
