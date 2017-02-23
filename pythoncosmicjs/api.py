import requests


class Api(object):
    def __init__(self, buckets, read_key=None, write_key=None, base_url=None):
        if not buckets:
            print('The error variable is not defined "buckets"')
        self.buckets = buckets
        self.base_url = 'https://api.cosmicjs.com/v1' or base_url
        self.read_key = '?%s' % read_key if read_key else ''
        self.write_key = write_key or ''

    def list_objects(self, limit=None, skip=None):
        limit = '?limit=%s' % limit if limit else ''
        skip = '?skip=%s' % skip if skip else ''
        url = '%s/%s/objects%s%s%s' % (self.base_url, self.buckets, self.read_key, limit, skip)
        return self.deserialization(url)

    def one_object(self, object_name):
        url = '%s/%s/object/%s/%s' % (self.base_url, self.buckets, object_name, self.read_key)
        return self.deserialization(url)

    def list_media(self):
        url = '%s/%s/media%s' % (self.base_url, self.buckets, self.read_key)
        return self.deserialization(url)

    def add_object(self, title, content):
        url = '%s/%s/add-object%s' % (self.base_url, self.buckets, self.write_key)
        r = requests.post(url, data={'title': title, 'type_slug': title.replace(' ', '-'), 'content': content})
        return r.json()

    def delete_object(self, object_name):
        url = '%s/%s/%s' % (self.base_url, self.buckets, object_name)
        r = requests.delete(url, data={'write_key': self.write_key})
        return r.json()
    
    @staticmethod
    def deserialization(url):
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        return r.status_code
