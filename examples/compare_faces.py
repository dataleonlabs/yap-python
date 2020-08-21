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

img1 = os.path.abspath('./resources/id-card1.png')
img2 = os.path.abspath('./resources/picture.png')


# Read document content
with open(img1, 'rb') as document:
    imageBase641 = base64.b64encode(document.read())

with open(img2, 'rb') as document:
    imageBase642 = base64.b64encode(document.read())

response = service.compare_faces(content1=imageBase641, content2=imageBase642)

# print that response
print(response)
# {
#     "faces": [
#         {
#             "bounding_box": {
#                 "width": 0.4544285535812378,
#                 "height": 0.4926297068595886,
#                 "left": 0.29225078225135803,
#                 "top": 0.2607613205909729
#             },
#             "landmarks": [
#                 [0.42053353786468506, 0.47441565990448],
#                 [0.6223667860031128, 0.47215574979782104],
#                 [0.4395148754119873, 0.6473249197006226],
#                 [0.6078771948814392, 0.6452915072441101],
#                 [0.5231670141220093, 0.5680342316627502],
#                 [0.3449179530143738, 0.43304699659347534],
#                 [0.4037591814994812, 0.4133119583129883]
#             ],
#             "confidence": 99.9996566772461,
#             "similarity": 59.9996566772461
#         }
#     ]
# }
