from repository.parser import VKRepository, Chrome


def run_browser(profile: str = "Profile 1", proxy=False):
    return VKRepository.open_friends(profile=profile, proxy=proxy)


def get_count_friends(browser: Chrome):
    return VKRepository.get_count_friends(browser)


def scroll_page_down(browser: Chrome, friends_count: int):
    return VKRepository.scroll_page_down(browser, friends_count)


def get_friends(browser: Chrome, value: int):
    return VKRepository.get_friends(browser, value)


def choose_friend(browser, friend_box: dict,  id: int):
    VKRepository.choose_friend(browser, friend_box, id)
