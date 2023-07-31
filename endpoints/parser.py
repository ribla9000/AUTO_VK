import time

from repository.parser import VKRepository, Chrome


def run_browser(profile: str = "Profile 1", proxy: bool = False):
    return VKRepository.run_browser(profile, proxy)


def check_login(browser: Chrome):
    is_auth = VKRepository.is_authorized(browser)
    if is_auth:
        VKRepository.open_friends(browser)
        return True
    return False


def login(browser: Chrome, _login: str, password: str):
    VKRepository.vk_login(browser, _login, password)
    time.sleep(4)
    check_login(browser)
    return


def get_count_friends(browser: Chrome):
    return VKRepository.get_count_friends(browser)


def scroll_page_down(browser: Chrome, friends_count: int):
    return VKRepository.scroll_page_down(browser, friends_count)


def get_friends(browser: Chrome, value: int):
    return VKRepository.get_friends(browser, value)


def choose_friend(browser, friend_box: dict,  id: int):
    return VKRepository.choose_friend(browser, friend_box, id)


def get_profiles():
    return VKRepository.get_profiles()

