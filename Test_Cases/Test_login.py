import pytest
from pages.Login_page import LoginPage
from pages.Home_page import HomePage

# @pytest.mark.usefixtures("page")
# def test_navigate(page):
#     home_page = HomePage(page)
#     login_page = LoginPage(page)
#     login_page.navigate()
#     login_page.close_popup()
#     home_page.click_login_link()
@pytest.mark.usefixtures("page")
def test_login(page):
    login_page = LoginPage(page)
    login_page.login("9960739317", "Test@9850")

@pytest.mark.usefixtures("page")
def test_project_name(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    login_page.login("9960739317", "Test@9850")
    home_page.check_project_name()

@pytest.mark.usefixtures("page")
def test_1project(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    login_page.login("9960739317", "Test@9850")
    home_page.check_1project()

@pytest.mark.usefixtures("page")
def test_2project(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    login_page.login("9960739317", "Test@9850")
    home_page.check_2project()

@pytest.mark.usefixtures("page")
def test_3project(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    login_page.login("9960739317", "Test@9850")
    home_page.check_2project()

@pytest.mark.usefixtures("page")
def test_4project(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    login_page.login("9960739317", "Test@9850")
    home_page.check_3project()

@pytest.mark.usefixtures("page")
def test_5project(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    login_page.login("9960739317", "Test@9850")
    home_page.check_4project()

@pytest.mark.usefixtures("page")
def test_6project(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    login_page.login("9960739317", "Test@9850")
    home_page.check_5project()

@pytest.mark.usefixtures("page")
def test_7project(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    login_page.login("9960739317", "Test@9850")
    home_page.check_6project()

@pytest.mark.usefixtures("page")
def test_8project(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    login_page.login("9960739317", "Test@9850")
    home_page.check_7project()

@pytest.mark.usefixtures("page")
def test_9project(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    login_page.login("9960739317", "Test@9850")
    home_page.check_8project()

@pytest.mark.usefixtures("page")
def test_10project(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    login_page.login("9960739317", "Test@9850")

    home_page.check_9project()

@pytest.mark.usefixtures("page")
def test_11project(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    login_page.login("9960739317", "Test@9850")
    home_page.check_10project()

@pytest.mark.usefixtures("page")
def test_project_total(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    login_page.login("9960739317", "Test@9850")
    home_page.check_total()
