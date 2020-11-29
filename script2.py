from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_option = Options()
chrome_option.add_extension("setupvpn.crx")
driver1 = webdriver.Chrome(executable_path='chromedriver.exe',options=chrome_option)
driver1.get("https://www.google.com/")

from selenium.webdriver.common.proxy import Proxy, ProxyType

prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.http_proxy = "ip_addr:port"
prox.socks_proxy = "ip_addr:port"
prox.ssl_proxy = "ip_addr:port"

capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)

driver = webdriver.Chrome(desired_capabilities=capabilities)




try:
    elem = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'zipcodeInput'))
    )
    elem.send_keys("Hola")
    driver.find_element_by_class_name("Button_btn__23s9Z Button_button__21zUC Button_button-red__7mEF_").click()


finally:
    driver.quit()