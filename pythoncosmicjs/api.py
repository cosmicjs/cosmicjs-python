import requests


class Api(object):
    def __init__(self, buckets, read_key=None, write_key=None, base_url=None):
        if not buckets:
            print('The error variable is not defined "buckets"')
        self.buckets = buckets
        self.base_url = 'https://api.cosmicjs.com/v1' or base_url
        self.read_key = '?read_key=%s' % read_key if read_key else ''
        self.write_key = '?write_key=%s' % write_key if write_key else ''

    def all_content(self):
        url = '%s/%s/' % (self.base_url, self.buckets)
        return self.deserialization(url)

    def list_objects(self, limit=None, skip=None):
        limit = '?limit=%s' % limit if limit else ''
        skip = '?skip=%s' % skip if skip else ''
        url = '%s/%s/objects%s%s%s' % (self.base_url, self.buckets, self.read_key, limit, skip)
        return self.deserialization(url)

    def one_object(self, object_name):
        url = '%s/%s/object/%s/%s' % (self.base_url, self.buckets, object_name, self.read_key)
        print(url)
        return self.deserialization(url)

    def list_media(self):
        url = '%s/%s/media%s' % (self.base_url, self.buckets, self.read_key)
        return self.deserialization(url)

    def search_object(self, text_search, limit=None, skip=None):
        limit = '?limit=%s' % limit if limit else ''
        skip = '?skip=%s' % skip if skip else ''
        metafieldkeys = '?metafield_key=%s' % metafieldkeys if metafieldkeys else ''
        metafield_value = '?metafield_value=%s' % metafield_value if metafield_value else ''
        url = '%s/%s/object-type/%s/search%s%s' % (self.base_url, self.buckets, text_search, limit, skip)

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
    def deserialization(url):
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        return r.status_code
