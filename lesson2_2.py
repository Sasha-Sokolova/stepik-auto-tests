from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_xpath("//span[@id = 'num1']").text
    y = browser.find_element_by_xpath("//span[@id = 'num2']").text

    number = int(x) + int(y)

    dropdown = browser.find_element_by_xpath("//select[@id = 'dropdown']").click()



    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(number))

    submit = browser.find_element_by_xpath("//button[@type='submit']").click()






finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()