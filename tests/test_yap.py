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

from yapsdk import Yap
import io
import os

def test_class():

    # Test with customer endpoint
    api_key = "91abd22c-0c24-49d8-9bb8"
    endpoint = "https://youngapp.co"
    service = Yap(api_key=api_key, endpoint=endpoint)
    
    info = service.get_info()
    assert info["api_key"] == api_key
    assert info["endpoint"] == endpoint

    # Test with default endpoint
    service = Yap(api_key=api_key)
    info = service.get_info()
    assert info["api_key"] == api_key
    assert info["endpoint"] == 'https://execute-api.youngapp.co'
