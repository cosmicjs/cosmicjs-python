import requests


class Api(object):
    def __init__(self, buckets, read_key=None, write_key=None, base_url=None):
        self.buckets = buckets
        self.base_url = 'https://api.cosmicjs.com/v1' or base_url
        self.read_key = '?read_key=%s' % read_key if read_key else ''
        self.write_key = '?write_key=%s' % write_key if write_key else ''

    def all_content(self):
        url = '%s/%s/' % (self.base_url, self.buckets)
        return self.deserialization(url)

    def list_objects(self, limit=None, skip=None):
        payload = {'limit': limit, 'skip': skip}
        url = '%s/%s/objects%s' % (self.base_url, self.buckets, self.read_key)
        return self.deserialization(url, payload)

    def one_object(self, object_name):
        url = '%s/%s/object/%s/%s' % (self.base_url, self.buckets, object_name, self.read_key)
        return self.deserialization(url)

    def list_media(self, limit=None, skip=None):
        if limit and skip:
            query_parameters = '?limit=%s&?skip=%s' % (limit, skip)
        else:
            query_parameters = '%s%s' % ('?limit=' + str(limit) if limit else '', '?skip=' + str(skip) if skip else '')
        url = '%s/%s/media%s%s' % (self.base_url, self.buckets, self.read_key, query_parameters)
        return self.deserialization(url)

    def search_object(self, object_type=None, limit=None, skip=None, metafield_keys=None, metafield_value=None):
        payload = {'limit': limit, 'skip': skip, 'metafield_key': metafield_keys, 'metafield_value': metafield_value}
        url = '%s/%s/object-type/%s/search' % (self.base_url, self.buckets, object_type)
        return self.deserialization(url, payload)

    def add_object(self, title, content):
        url = '%s/%s/add-object%s' % (self.base_url, self.buckets, self.write_key)
        r = requests.post(url, data={'title': title, 'type_slug': title.replace(' ', '-'), 'content': content,
                                     'write_key': self.write_key})
        return r.json()

    def edit_object(self, slug, title, content):
        url = '%s/%s/edit-object' % (self.base_url, self.buckets)
        r = requests.put(url, data={'slug': slug, 'title': title, 'content': content})
        return r.json()

    def delete_object(self, object_name):
        url = '%s/%s/%s' % (self.base_url, self.buckets, object_name)
        r = requests.delete(url, data={'write_key': self.write_key})
        return r.json()

    @staticmethod
    def deserialization(url, params=None):
        r = requests.get(url, params)
        if r.status_code == 200:
            return r.json()
