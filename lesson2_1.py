from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_xpath("//img[@id = 'treasure']").get_attribute("valuex")

    print(x)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)

    answer = browser.find_element_by_css_selector("#answer").send_keys(y)

    checkbox = browser.find_element_by_css_selector("#robotCheckbox").click()

    radiobutton = browser.find_element_by_css_selector("#robotsRule").click()

    submit = browser.find_element_by_xpath("//button[@type='submit']").click()






finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()