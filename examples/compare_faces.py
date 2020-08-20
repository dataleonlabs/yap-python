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
print(response["faces"])
