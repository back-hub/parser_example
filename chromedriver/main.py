from selenium import webdriver
import time
from auth_data import login, password


driver = webdriver.Chrome(executable_path="/home/backhub/PycharmProjects/dummy_parser/chromedriver/chromedriver")

def parser(url, url_transcript, object:str):
    driver.get(url)

    login_input = driver.find_element_by_id("login_input")
    login_input.clear()
    login_input.send_keys(login)

    pass_input = driver.find_element_by_id("pass_input")
    pass_input.clear()
    pass_input.send_keys(password)

    button = driver.find_element_by_id("Submit1").click()
    time.sleep(5)
    driver.get(url_transcript)
    some_list = driver.find_elements_by_class_name("tdClass")
    emp_list = []
    for el in some_list:
        txt = el.text
        emp_list.append(txt)
    i = 0
    el_ind = emp_list.index(object)
    new_list = []
    while i != 9:
        new_list.append([emp_list[el_ind + i]])
        i += 1
    print(new_list)
    driver.close()
    driver.quit()
    return new_list


