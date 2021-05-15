from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element_by_xpath("//span[@id = 'input_value']").text)

    print(x)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)

    answer = browser.find_element_by_css_selector("#answer").send_keys(y)

    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    checkbox = browser.find_element_by_css_selector("#robotCheckbox").click()

    radiobutton = browser.find_element_by_css_selector("#robotsRule").click()

    submit = browser.find_element_by_xpath("//button[@type='submit']").click()







finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()