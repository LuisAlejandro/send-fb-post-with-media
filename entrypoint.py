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
import json

from pyfacebook import GraphAPI


access_token = os.environ.get('FACEBOOK_ACCESS_TOKEN')
page_id = os.environ.get('FACEBOOK_PAGE_ID')
status_text = os.environ.get('STATUS_TEXT')
status_image_url_1 = os.environ.get('STATUS_IMAGE_URL_1')
status_image_url_2 = os.environ.get('STATUS_IMAGE_URL_2')
status_image_url_3 = os.environ.get('STATUS_IMAGE_URL_3')
status_image_url_4 = os.environ.get('STATUS_IMAGE_URL_4')

if not page_id:
    raise Exception('No FACEBOOK_PAGE_ID provided.')

attached_media = []
graph = GraphAPI(access_token=access_token, version="13.0")

for imgurl in [status_image_url_1,
               status_image_url_2,
               status_image_url_3,
               status_image_url_4]:

    if not imgurl:
        continue

    imgdata = {'url': imgurl, 'published': False}
    media = graph.post_object(object_id=page_id,
                              connection='photos',
                              data=imgdata)
    attached_media.append({'media_fbid': media['id']})

data = {
    'message': status_text,
    'published': True,
    'attached_media': json.dumps(attached_media)
}
graph.post_object(object_id=page_id,
                  connection='feed',
                  data=data)
