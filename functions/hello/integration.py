import pytest
import requests
from lambda_forge.constants import BASE_URL

@pytest.mark.integration(method="GET", endpoint="/hello")
def test_hello_status_code_is_200():

    response = requests.get(url=f"{BASE_URL}/hello")

    assert response.status_code == 200 
