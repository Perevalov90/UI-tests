import pytest
from noon.pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)