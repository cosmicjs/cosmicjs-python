from pythoncosmicjs import Api

bucket_slug = 'pythoncosmicjs'
read_key = '1eEggaao4xJFBnhAOBGV6oX40chL7Kp71bMXpyCMk51OUt9acb'
write_key = '9rIG8XYnKDP60MtIis8ORv1pzgp2kYsT7PsXyV1yciqwaNIpPC'
api = Api(bucket_slug, read_key, write_key)

print(api.add_object('Test add object', 'Test add object'))
