from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_requests
from src.helpers.common_verification import verify_http_status_code
from src.helpers.payload_manager import payload_create_token
from src.helpers.utils import common_headers_json
import pytest

def test_create_token():
    response=post_requests(url=APIConstants.base_url(),
                           payload=payload_create_token(),
                           headers=common_headers_json(),
                           auth=None,
                           in_json=False)
    print(response)

