from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get('https://cargo.koreanair.com/ko/FAQ')

# 탭 요소를 감싸는 div를 찾음
tab_container = driver.find_element(By.XPATH, '//*[@id="nav-tab"]')

# 그 안의 모든 탭 버튼(a, button 등)을 찾음
tabs = tab_container.find_elements(By.XPATH, './*')

for tab in tabs:
    try:
        tab.click()
        print(f"Clicked on tab: {tab.text}")
        sleep(1)
        # 태그 잡고 질문 클릭하기
        box_div = driver.find_element(By.XPATH,'//*[@id="claim"]/div')
        div_containers = box_div.find_elements(By.XPATH,'./*')
        for container in div_containers:
            container.click()
            sleep(1)
    except Exception as e:
        print(f"Failed to click tab: {e}")