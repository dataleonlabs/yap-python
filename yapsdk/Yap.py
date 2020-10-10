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

import requests
import json
from yapsdk.utils import isBase64


class Yap:
    '''Constructor of class API'''

    def __init__(self, api_key, endpoint='https://execute-api.youngapp.co'):
        self.api_key = api_key
        self.endpoint = endpoint

    ''' Get info '''
    def get_info(self):
        return {
            "api_key": self.api_key,
            "endpoint": self.endpoint
        }

    ''' Set endpoint '''
    def set_endpoint(self, endpoint):
        self.endpoint = endpoint

    ''' Set api key '''
    def set_api_key(self, api_key):
        self.api_key = api_key

    ''' Get endpoint '''
    def get_endpoint(self):
        return self.endpoint


    ''' Get api key '''
    def get_api_key(self):
        return self.api_key

    ''' Get headers '''
    def get_headers(self):
        return {
            'content-type': "application/json",
            'authorization': "Bearer {}".format(self.api_key),
        }

    ''' Make request function '''
    def make_request(self, path, payload=None, method="POST"):
        headers = self.get_headers()
        response = requests.request(
            method=method,
            url="{0}{1}".format(self.endpoint, path),
            json=payload,
            timeout=30,
            headers=headers
        )

        return json.loads(response.content)

    '''Detects text in the input document with base64 image.'''

    def get_text(self, content, version='lastest'):
        if isBase64(content) == False:
            raise Exception('content argument must be base64')

        return self.make_request(
            path='/{0}/vision/text'.format(version),
            payload={
                'content': content.decode(),
            }
        )

    ''' Detects lines in the input document with base64 image.'''

    def get_lines(self, content, precision=1, version='lastest'):
        if isBase64(content) == False:
            raise Exception('content argument must be base64')

        return self.make_request(
            path='/{0}/vision/lines'.format(version),
            payload={
                'precision': precision,
                'content': content.decode(),
            }
        )

    ''' Detects tables in the input document with base64 image. '''

    def get_tables(self, content, version='lastest'):
        if isBase64(content) == False:
            raise Exception('content argument must be base64')

        return self.make_request(
            path='/{0}/vision/tables'.format(version),
            payload={
                'content': content.decode(),
            }
        )

    ''' Inspects text for named entities, and returns information about them. '''

    def get_entities(self, text, language=None, version='lastest'):
        if isinstance(text, list) == False:
            raise Exception('text argument must be list')

        if (language is not None) and (isinstance(language, str) == False):
            raise Exception('language argument must be str')

        return self.make_request(
            path='/{0}/vision/entities'.format(version),
            payload={
                'text': text,
                'language': language,
            }
        )

    ''' Determines the dominant language of the input text for a batch of documents. '''

    def detect_dominant_language(self, text, version='lastest'):
        if isinstance(text, list) == False:
            raise Exception('text argument must be list')

        return self.make_request(
            path='/{0}/vision/dominant-language'.format(version),
            payload={
                'text': text,
            }
        )

    ''' Provide the detect operation that looks for key facial features. '''

    def detect_faces(self, content, version='lastest'):
        if isBase64(content) == False:
            raise Exception('content argument must be base64')

        return self.make_request(
            path='/{0}/vision/face-detection'.format(version),
            payload={
                'content': content.decode(),
            }
        )

    ''' To compare a face in the source image with each face in the target image.'''

    def compare_faces(self, content1, content2, version='lastest'):
        if isBase64(content1) == False:
            raise Exception('content1 argument must be base64')

        if isBase64(content2) == False:
            raise Exception('content2 argument must be base64')

        return self.make_request(
            path='/{0}/vision/face-compare'.format(version),
            payload={
                'content1': content1.decode(),
                'content2': content2.decode(),
            }
        )

    ''' Inspects text for named entities, and returns information about them based on CSV file. '''

    def get_generic_entities(self, blocks, configurator, version='lastest'):
        if isinstance(configurator, str) == False:
            raise Exception('configurator argument must be str')

        return self.make_request(
            path='/{0}/vision/generic-entities'.format(version),
            payload={
                'blocks': blocks,
                'configurator': configurator,
            }
        )

    ''' Detects entities in the input document with base64 image. '''

    def get_document_entities(self, type_doc, content, version='lastest'):
        if isBase64(content) == False:
            raise Exception('content argument must be base64')

        if isinstance(type_doc, str) == False:
            raise Exception('doc type argument must be str')

        return self.make_request(
            path='/{0}/documents/{1}'.format(version, type_doc),
            payload={
                'content': content.decode(),
            }
        )

    ''' Detects entities in the input document with base64 image. '''

    def get_document_info(self, content, version='lastest'):
        if isBase64(content) == False:
            raise Exception('content argument must be base64')

        return self.make_request(
            path='/{0}/document-info'.format(version),
            payload={
                'content': content.decode(),
            }
        )

    def get_company_info(self, value):
        if (isinstance(value, str) == False) and (isinstance(value, int) == False):
            raise Exception('value argument must be str')
        return self.make_request(
            method='GET',
            path='/v1/assets/companies/fr/{0}'.format(value),
        )

    def get_iban_info(self, value):
        if isinstance(value, str) == False:
            raise Exception('value argument must be str')
        return self.make_request(
            method='GET',
            path='/v1/validate/iban?iban={0}'.format(value),
        )

    def get_vat_info(self, value):
        if isinstance(value, str) == False:
            raise Exception('value argument must be str')
        return self.make_request(
            method='GET',
            path='/v1/validate/vat?vat={0}'.format(value),
        )

    def check_email(self, value):
        if isinstance(value, str) == False:
            raise Exception('value argument must be str')
        return self.make_request(
            method='GET',
            path='/v1/validate/email?email={0}'.format(value),
        )

    def check_phone(self, value):
        if isinstance(value, str) == False:
            raise Exception('value argument must be str')
        return self.make_request(
            method='GET',
            path='/v1/validate/phone?phone={0}'.format(value),
        )

    def get_countries(self):
        return self.make_request(
            method='GET',
            path='/v1/assets/countries',
        )
