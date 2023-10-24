from app.main.config import Email
from app.main.exceptions import FailedDependency
from json.decoder import JSONDecodeError
from httpx import AsyncClient, ConnectError, TimeoutException
from app.utils.logger import Logger
import http
import time


class HttpxHelper:
    KEY = "success"

    def __init__(self):
        self.base_url = Email.base_url
        self.token = Email.access_token
        self.header = {"Authorization": f"Bearer {self.token}"}

    async def api_call(self, path: str, json: dict):
        async with AsyncClient(timeout=30.0) as client:
            url = f"{self.base_url}/{path}"
            start_time = time.time()

            try:
                response = await client.post(url=url, json=json, headers=self.header)

            except TimeoutException:
                raise FailedDependency("Timeout in connection at Email Service")

            except ConnectError:
                raise FailedDependency("Connection Error at Email Service")

            except Exception as error:
                raise FailedDependency(f"Unexpected Error from Email Service: {error.args}")

            end_time = (time.time() - start_time) * 1000
            status_phrase = http.HTTPStatus(response.status_code).phrase
            process_time = "{0:.2f}".format(end_time)

            if response.status_code != 200:
                raise FailedDependency(f"Invalid Response from Email Service: status {response.status_code}")

            try:
                if response.json() is None or not response.json()[self.KEY]:
                    raise FailedDependency("Invalid Response from Email Service")
            except JSONDecodeError:
                pass

            Logger.service(url, response.status_code, status_phrase, process_time)
