from selenium import webdriver
import time

# gakuseki = 0
# for num in range(9999999):
#     print(gakuseki)
#     gakuseki = gakuseki + 1

driver = webdriver.Chrome("./chromedriver")
driver.get("https://n-high-english-test.herokuapp.com/signup")
userBox = driver.find_element_by_css_selector("#user_name")
userBox.send_keys("Selenium")
nickBox = driver.find_element_by_css_selector("#user_nickname")
nickBox.send_keys("Selenium")
gakusekiBox = driver.find_element_by_css_selector("#user_student_number")
gakusekiBox.send_keys("18N1200287")
passBox = driver.find_element_by_css_selector("#user_password")
passBox.send_keys("Selenium")
signUp = driver.find_element_by_css_selector(".btn")
signUp.click() #検索ボタンをクリック

time.sleep(3)
#
# toggle = driver.find_element_by_css_selector(".dropdown")
# toggle.click
#
# driver.findElement(By.xpath("//*[text()=\"ログアウト\"]")).click();
logout = driver.findElement(By.xpath("/html/body/header/div/nav/ul/li[2]/ul/li[3]/a"))
logout.click
