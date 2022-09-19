from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
ua = UserAgent(verify_ssl=False)
user_agent = ua.random
print(user_agent)
chrome_options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(chrome_options=chrome_options)

count = 0
while count == 0:
    driver.get('https://allegro.pl/listing?string=macbook')
    page_source = driver.page_source
    links = driver.find_elements_by_class_name('mpof_ki')
    for l in links:
        el = l.find_element_by_tag_name('a')
        print(el)
    print(len(links))
    driver.close()
    if links:
        count += 1


driver.quit()
