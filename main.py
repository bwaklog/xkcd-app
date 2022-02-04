#! /Users/adityahegde/opt/anaconda3/bin/python3.9

# Modules for accessing api and getting data
import requests
from pprint import pprint
import random
from PIL import Image

# Get current total comics
rtest = requests.get('https://xkcd.com/info.0.json')
rtest_json = rtest.json()
num_max = rtest_json['num']


class xkcd:
    ra_int = random.randint(0, num_max+1)

    response = requests.get(f'https://xkcd.com/{ra_int}/info.0.json')

    metadata = dict(response.json())

    # Important Metadata filtered from JSON
    alt = metadata['alt']
    img_url = metadata['img']
    num = metadata['num']
    title = metadata['title']
    transcript = metadata['transcript']
    year = metadata['year']
    c_url = response
    js = response.json()


    def sh(self):
        metadata = self.metadata
        img_data = requests.get(self.img_url).content
        with open(f"{metadata['safe_title']}_{metadata['num']}.jpg", 'wb') as handler:
            handler.write(img_data)

        im = Image.open(f"{metadata['safe_title']}_{metadata['num']}.jpg")
        im.show()


comic = xkcd()
pprint(f'Title : {comic.title} - {comic.num}')
pprint(comic.c_url.url)
pprint(comic.js)
pprint(comic.img_url)
comic.sh()
