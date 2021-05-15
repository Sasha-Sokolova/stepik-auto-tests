from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    button = browser.find_element_by_xpath("//button[@type='submit']").click()




    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    x = browser.find_element_by_css_selector("#input_value").text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)

    answer = browser.find_element_by_css_selector("#answer").send_keys(y)

    sumbit = browser.find_element_by_xpath("//button[@type='submit']").click()








finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()