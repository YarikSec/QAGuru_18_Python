import json
import logging

import allure
import curlify
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType


def load_schema(path=""):
    with open(path) as file:
        return json.loads(file.read())


def post_reqres(url, **kwargs):
    base_url = "https://reqres.in"
    with step(f"POST {url}"):
        response = requests.post(base_url + url, kwargs)
        curl = curlify.to_curl(response.request)
        logging.info(curlify.to_curl(response.request))
        allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
    return response

def log_to_console(result=None):
    if result:
        logging.info(f"HTTP Response Code: {result.status_code}")
        logging.info(f"HTTP Response Body: {json.dumps(json.loads(result.text), indent=4, ensure_ascii=False) if result.text else 'None'}")
    else:
        logging.info("No response received.")

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_request(url, method, headers=None, data=None, cookies=None):
    with allure.step(f'{method} {url}'):
        allure.attach(url, 'URL', allure.attachment_type.TEXT)
        if headers:
            allure.attach(json.dumps(headers, indent=4), 'Request Headers', allure.attachment_type.JSON)
        if data:
            allure.attach(json.dumps(data, indent=4), 'Request Data', allure.attachment_type.JSON)
        if cookies:
            allure.attach(json.dumps(dict(cookies), indent=4), 'Request Cookies', allure.attachment_type.JSON)
        
        logger.info(f"Request: {method} {url}")
        if headers:
            logger.info(f"Headers: {json.dumps(headers, indent=4)}")
        if data:
            logger.info(f"Data: {json.dumps(data, indent=4)}")
        if cookies:
            logger.info(f"Cookies: {json.dumps(dict(cookies), indent=4)}")

def log_response(response):
    with allure.step('Response'):
        allure.attach(str(response.status_code), 'Status Code', allure.attachment_type.TEXT)
        allure.attach(json.dumps(dict(response.headers), indent=4), 'Response Headers', allure.attachment_type.JSON)
        
        # Проверяем, является ли ответ JSON
        try:
            response_body = json.dumps(response.json(), indent=4, ensure_ascii=False)
            allure.attach(response_body, 'Response Body', allure.attachment_type.JSON)
        except:
            allure.attach(response.text, 'Response Body', allure.attachment_type.TEXT)
        
        logger.info(f"Response Status: {response.status_code}")
        logger.info(f"Response Headers: {json.dumps(dict(response.headers), indent=4)}")
        try:
            logger.info(f"Response Body: {json.dumps(response.json(), indent=4, ensure_ascii=False)}")
        except:
            logger.info(f"Response Body: {response.text}")