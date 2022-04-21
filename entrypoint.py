# -*- coding: utf-8 -*-
#
# Please refer to AUTHORS.md for a complete list of Copyright holders.
# Copyright (C) 2020-2022 Luis Alejandro Martínez Faneyth.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import tempfile
from urllib.request import urlopen

from tweepy import OAuth1UserHandler, API


consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
oauth_token = os.environ.get('TWITTER_OAUTH_TOKEN')
oauth_secret = os.environ.get('TWITTER_OAUTH_SECRET')
status_text = os.environ.get('STATUS_TEXT')
status_image_url_1 = os.environ.get('STATUS_IMAGE_URL_1')
status_image_url_2 = os.environ.get('STATUS_IMAGE_URL_2')
status_image_url_3 = os.environ.get('STATUS_IMAGE_URL_3')
status_image_url_4 = os.environ.get('STATUS_IMAGE_URL_4')

media_ids = []
auth = OAuth1UserHandler(consumer_key, consumer_secret,
                         oauth_token, oauth_secret)
api = API(auth, wait_on_rate_limit=True)

for imgurl in [status_image_url_1,
               status_image_url_2,
               status_image_url_3,
               status_image_url_4]:

    if not imgurl:
        continue

    _, tmpimg = tempfile.mkstemp(prefix='status-image-url-', suffix='.bin')

    with open(tmpimg, 'wb') as i:
        i.write(urlopen(imgurl).read())

    media = api.media_upload(tmpimg)
    media_ids.append(media.media_id)

api.update_status(status_text, media_ids=media_ids)
