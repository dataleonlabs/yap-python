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
from yapsdk import Yap
import os

load_dotenv()

service = Yap(api_key=os.environ['API_KEY'])

# Add custom endpoint
# service = Yap(api_key=os.environ['API_KEY'], endpoint=os.environ['ENDPOINT'])

response = service.get_generic_entities(
    blocks="<blocks>", configurator='<csv>'
)

# print that response
print(response)
# {
#     "entities": [
#         {
#             "confidence": 0.4,
#             "name": "string",
#             "value": "string",
#             "text": "string",
#             "bounding_box": 123,
#         }
#     ]
# }
