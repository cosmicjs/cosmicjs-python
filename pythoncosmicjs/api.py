import requests


class Api(object):
    def __init__(self, buckets, read_key=None, write_key=None, base_url=None):
        if not buckets:
            print('The error variable is not defined "buckets"')
        self.buckets = buckets
        self.base_url = 'https://api.cosmicjs.com/v1' or base_url
        self.read_key = '?%s' % read_key if read_key else ''
        self.write_key = write_key or ''

    def list_objects(self):
        url = '%s/%s/objects%s' % (self.base_url, self.buckets, self.read_key)
        return self.deserialization(url)

    def one_object(self, object_name):
        url = '%s/%s/object/%s/%s' % (self.base_url, self.buckets, object_name, self.read_key)
        return self.deserialization(url)

    def list_media(self):
        url = '%s/%s/media%s' % (self.base_url, self.buckets, self.read_key)
        return self.deserialization(url)

    @staticmethod
    def deserialization(url):
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        return r.status_code
