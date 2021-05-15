from selenium import webdriver
import time
import os


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)




    input1 = browser.find_element_by_xpath("//input[@name='firstname']").send_keys("Van")

    input2 = browser.find_element_by_xpath("//input[@name='lastname']").send_keys("X")


    input4 = browser.find_element_by_xpath("//input[@name='email']").send_keys("test@test.ru")


    current_dir = os.path.abspath(os.path.dirname(__file__))

    file_path = os.path.join(current_dir, 'text.txt')

    input5 = browser.find_element_by_xpath("//input[@type='file']").send_keys(file_path)

    button = browser.find_element_by_xpath("//button[@type='submit']").click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

# driver.findElement(By.xpath("//input[@id='usernamereg-firstName']")).sendKeys("Your-Name");