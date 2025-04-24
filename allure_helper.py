import datetime
import json

import allure
import requests


class AllureHelper:

    def attach_http_response(self, response: requests.Response):
        with allure.step(f'Attach {response}'):
            request: requests.PreparedRequest = response.request

        allure.attach(body=f'Request {request.method} {request.url} \n'
                           f'body: {str(request.body)} \n'
                           f'headers: {json.dumps(request.headers)} \n'
                           f'time: {datetime.datetime.now()}')
    def enrich_allure(self, response: requests.Response):
        self.attach_http_response(response)
