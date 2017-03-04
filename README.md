[![Issue Count](https://codeclimate.com/github/uskavan/pythoncosmicjs/badges/issue_count.svg)](https://codeclimate.com/github/uskavan/pythoncosmicjs)

## Install
1. `git clone https://github.com/uskavan/cosmicjs-python.git`
2. `python setup.py install`

### Usage
```python
from pythoncosmicjs import Api
# Configure
api = Api(buckets='buckets name', read_key='read key', write_key='write key')
# Get bucket
print(api.all_content())
# Get objects
print(list_objects(limit=10, skip=5)) # limit, skip the default is None
# Get objects by type

# Get object
print(one_object(object_name='object name')) # object_name mandatory variable
# Get media
print(list_media(limit=10, skip=5)) # limit, skip the default is None
# Add object
print(api.add_object(title='title object', content='content object')) title, content required variables
# Edit object
print(edit_object(title='change the title', content='change the content')) title, content required variables
# Delete object
print(delete_object='first') # the name of the object you want to delete
# Search object
print(search_object(object_type='', limit=1, skip=10, metafield_keys='bob', metafield_value='bob'))
```
## Link

[Documentation](https://github.com/uskavan/pythoncosmicjs/wiki)

[Official website Сosmicjs](https://cosmicjs.com/)

[Referral Link](https://cosmicjs.com/?ref=S1G_ALN9x)
