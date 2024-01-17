import pytest
from fake_useragent import FakeUserAgent


@pytest.fixture(scope="function", autouse=False)
def headers_fixture() -> dict:
    ua = FakeUserAgent()
    headers = {"User-Agent": ua.random}

    return headers