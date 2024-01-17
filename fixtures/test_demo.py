import requests
from fixtures import headers_fixture

def test_assert_headers(headers_fixture: dict):
    url = "https://httpbin.org/headers"  
    res = requests.get(url=url, headers=headers_fixture)

    print(res.status_code)
    print(res.json())

    assert res.status_code == 200
    assert res.json()['headers']["User-Agent"] == headers_fixture["User-Agent"]