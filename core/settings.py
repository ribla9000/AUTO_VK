from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service
from repository.security import set_proxy


def get_options(profile: str = "Profile 1", proxy: bool = False):
    options = ChromeOptions()
    options.page_load_strategy = "eager"
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_argument("accept-lang=ru-RU;q=0.9,en-US;q=0.8,en;q=0.7")
    options.add_argument('disable-blink-features=AutomationControlled')
    options.add_argument('--allow-profiles-outside-user-dir')
    options.add_argument('--enable-profile-shortcut-manager')
    options.add_argument(r'user-data-dir=./profiles')
    options.add_argument(f'--profile-directory={profile}')
    if isinstance(proxy, str):
        proxy_host = set_proxy(ip=input("Input IP: "), port=int(input("Input PORT: ")))
        options.add_argument(f"--proxy-server={proxy_host['ip']}:{proxy_host['port']}")
    return options


def start(profile: str = "Profile 1", proxy: bool = False):
    webdriver_service = Service("src/chromedriver")
    browser = Chrome(service=webdriver_service, options=get_options(profile, proxy))
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        'source': '''
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Proxy;
          '''})
    return browser