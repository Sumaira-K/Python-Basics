# requests is a package that allows you to send HTTP requests in Python. It is not included in the standard library, so you need to install it using pip.
# JSON is a package that allows you to work with JSON data in Python. It is included in the standard library, so you don't need to install it.
import json
import requests
import sys
if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])