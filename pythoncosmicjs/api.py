import requests


class Api(object):
    def __init__(self, buckets=None, read_key=None, write_key=None, base_url=None):
        if buckets is None:
            print('The error variable is not defined "buckets"')
        else:
            self.buckets = buckets
        if base_url is None:
            self.base_url = 'https://api.cosmicjs.com/v1'
        else:
            self.base_url = base_url
        if read_key is None:
            self.read_key = ''
        else:
            self.read_key = '?%s' % read_key
        if write_key is None:
            self.write_key = ''
        else:
            self.write_key = write_key

    def all_objects_json(self):
        url = '%s/%s/objects%s' % (self.base_url, self.buckets, self.read_key)
        r = requests.get(url).json()
        return r

    def object_json(self, object_name=None):
        if object is None:
            self.object_name = object_name
        else:
            self.object_name = object_name
        url = '%s/%s/object/%s/%s' % (self.base_url, self.buckets, self.object_name, self.read_key)
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        if r.status_code == 404:
            return "404"
        else:
            return "Error"

    def all_media_list_json(self):
        url = '%s/%s/media' % (self.base_url, self.buckets)
        r = requests.get(url).json()
        return r
