import pytest
from noon.pages.login_page import LoginPage
from playwright.sync_api import Browser, BrowserContext

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Передаем настройки контекста, которые поддерживаются Playwright"""
    return {
        **browser_context_args,
        "ignore_https_errors": True,
        "viewport": {"width": 1920, "height": 1080},
        "user_agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/125 Safari/537.36"
        ),
        "java_script_enabled": True,
    }

@pytest.fixture(scope="session")
def browser_context(browser: Browser, browser_context_args) -> BrowserContext:
    """Создаем контекст вручную, с аргументами запуска браузера"""
    context = browser.new_context(**browser_context_args)
    return context

@pytest.fixture
def page(browser_context: BrowserContext):
    page = browser_context.new_page()
    # отключаем HTTP/2 и прочие флаги при запуске браузера
    page.context.browser.new_context()
    return page

@pytest.fixture
def login_page(page):
    return LoginPage(page)