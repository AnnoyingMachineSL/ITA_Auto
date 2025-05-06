import datetime
import json

import allure
import requests


class AllureHelper:

    def _attach_http_request(self, response: requests.Response):
        with allure.step(f'Attach {response.request}'):
            request: requests.PreparedRequest = response.request

            allure.attach(body=f'Request {request.method} {request.url} \n'
                               f'body: {json.loads(request.body.decode())} \n'
                               f'headers: {json.dumps(dict(request.headers))} \n'
                               f'time: {datetime.datetime.now()}')

    def _attach_http_response(self, response: requests.Response):
        with allure.step(f'Attaching {response}'):
            allure.attach(body=f'Request {response} {response.url} \n'
                               f'body: {json.loads(response.json())} \n'
                               f'headers: {json.dumps(dict(response.headers))} \n'
                               f'time: {datetime.datetime.now()}')

    def enrich_allure(self, response: requests.Response):
        self._attach_http_request(response)
        self._attach_http_response(response)
