import re
import urllib.request

with open("./uk.txt") as f:
    str = f.read()

pattern = re.compile("\|国旗画像 = (.+)")
match = pattern.search(str)
image_file_name = match.group(1)

url = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=imageinfo&titles=File:Flag%20of%20the%20United%20Kingdom.svg"
params = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": f"File:{image_file_name}"
}

req = urllib.request.Request('{}?{}'.format(
    url, urllib.parse.urlencode(params)))
with urllib.request.urlopen(req) as res:
    body = res.read()
    print(body)
