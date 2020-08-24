# coding: utf-8
# (C) Copyright Young App Corp. 2016, 2020.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# content of test_sample.py
from dotenv import load_dotenv
load_dotenv()

from yapsdk import Yap
import os
import base64

service = Yap(api_key=os.environ['API_KEY'])

# Add custom endpoint
# service = Yap(api_key=os.environ['API_KEY'], endpoint=os.environ['ENDPOINT'])

img = os.path.abspath('./resources/invoice-template.png')

# Read document content
with open(img, 'rb') as document:
    imageBase64 = base64.b64encode(document.read())

response = service.get_lines(content=imageBase64)

# Update precision
# response = service.get_lines(content=imageBase64, precision=1.25)

# print that response
print(response)
# {
#     "lines": [
#         {
#             "text": "string",
#             "id": "uuid4",
#             "bounding_box": [
#                 [51, 11],
#                 [78, 11],
#                 [78, 19],
#                 [51, 19]
#             ],
#             "blocks": [
#                 {
#                     "text": "string",
#                     "id": "8d2d1dce-5d2d-446f-b241-f7ba8efcdc96",
#                     "bounding_box": [
#                         [51, 11],
#                         [78, 11],
#                         [78, 19],
#                         [51, 19]
#                     ]
#                 }
#             ],
#         },
#     ],
#     "width": 120,
#     "height": 420,
#     "fulltext": ["string"]
# }
