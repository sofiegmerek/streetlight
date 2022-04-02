from pymemcache.client import base
from pymemcache import fallback

def do_some_query():
    # Replace with actual querying code to a database,
    # a remote REST API, etc.
    myfile = open("/Users/sofiegmerek/pymemcache/world.txt", "r")
    return myfile.read()
   # myfile.close()
   # return 42


# Don't forget to run `memcached' before running this code
client = base.Client(('localhost', 11211))
old_cache = base.Client(('localhost', 11211), ignore_exc=True)
new_cache = base.Client(('localhost', 11212))

#client = fallback.FallbackClient((new_cache, old_cache))
result = client.get('world3')

if result is None:
    # The cache is empty, need to get the value
    # from the canonical source:
    result = do_some_query()

    # Cache the result for next time:
    client.set('world3', result)

# Whether we needed to update the cache or not,
# at this point you can work with the data
# stored in the `result` variable:
print(result)
