from typing import Any
from json.decoder import JSONDecodeError
from httpx import AsyncClient, ConnectError, TimeoutException
from app.utils import Logger


class InvalidMethod(Exception):
    pass


class ExternalServiceError(Exception):
    pass


class BaseServiceClient:
    def __init__(
        self,
        base_url=None,
        external_service_error_exception_class=ExternalServiceError,
        external_service_error_exception_message="invalid response from external service",
        external_service_timeout_message="timeout in connection with external service",
    ):
        self.base_url = base_url
        self.external_service_error_exception_class = external_service_error_exception_class
        self.external_service_error_exception_message = external_service_error_exception_message
        self.external_service_timeout_message = external_service_timeout_message

    async def api_call(
        self,
        method: str,
        path: str,
        params: dict[str, Any] = {},
        json: dict[str, Any] = {},
        headers: dict[str, Any] = {},
    ):
        Logger().info(
            f"Sending request with, url: {self.base_url}, path: {path}, method: {method}, params: {params}, headers: {headers}"
        )
        async with AsyncClient(timeout=30.0) as client:
            try:
                url = f"{self.base_url}{path}"

                if method.upper() == "GET":
                    response = await client.get(url=url, params=params, headers=headers)
                elif method.upper() == "POST":
                    response = await client.post(url=url, params=params, json=json, headers=headers)
                elif method.upper() == "PUT":
                    response = await client.put(url=url, params=params, json=json, headers=headers)
                elif method.upper() == "PATCH":
                    response = await client.patch(url=url, params=params, json=json, headers=headers)
                elif method.upper() == "DELETE":
                    response = await client.delete(url=url, params=params, headers=headers)
                else:
                    raise InvalidMethod("invalid api call method")
            except TimeoutException:
                raise self.external_service_error_exception_class(self.external_service_timeout_message)
            except ConnectError as error:
                raise self.external_service_error_exception_class(str(error))

            Logger().debug(f"Response from server {vars(response)}")

            response_data = {}

            try:
                if response.json() is not None:
                    response_data = response.json()
                    Logger().info(f"Response data from server {response_data}")
            except JSONDecodeError:
                raise self.external_service_error_exception_class(self.external_service_error_exception_message)

            response_data["status"] = response.status_code

            return response_data
