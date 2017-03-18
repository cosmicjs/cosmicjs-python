[![Issue Count](https://codeclimate.com/github/cosmicjs/cosmicjs-python/badges/issue_count.svg)](https://codeclimate.com/github/cosmicjs/cosmicjs-python)

## Install
1. `git clone https://github.com/uskavan/cosmicjs-python.git`
2. `cd cosmicjs-python`
3. `python setup.py install`

### Usage
```python
from pythoncosmicjs import Api
# Configure
api = Api(bucket='bucket-slug', read_key='read_key', write_key='write_key')
# Get bucket
print(api.all_content())
# Get all objects
print(api.objects(limit=10, skip=5)) # limit, skip the default is None
# Get objects by type
print(api.object_type(type_slug='pages', limit=10, skip=5)) # limit, skip the default is None
# Get object
print(api.one_object(object_slug='object-slug')) # object_slug mandatory variable
# Get media
print(api.list_media(limit=10, skip=5)) # limit, skip the default is None
# Add object
print(api.add_object(title='object title', content='object content')) # title, content required variables
# Edit object
print(api.edit_object(object_slug='object-slug', title='change to the title', content='change to the content')) # title, content required variables
# Delete object
print(api.delete_object(object_slug='object-slug')) # the name of the object you want to delete
# Search object
print(api.search_object(object_type='', limit=1, skip=10, metafield_keys='bob', metafield_value='bob'))
```
## Link

[Documentation](https://github.com/uskavan/pythoncosmicjs/wiki)

[Official website Сosmicjs](https://cosmicjs.com/)

[Referral Link](https://cosmicjs.com/?ref=S1G_ALN9x)
