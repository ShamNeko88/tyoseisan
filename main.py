from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHOUSEISAN_URL: str = "https://chouseisan.com/"

# ドライバーの起動（Chromeを使用）
driver = webdriver.Chrome()

# 調整さんのトップページを開く
driver.get(CHOUSEISAN_URL)
time.sleep(2)
# 「新しいイベントを作る」をクリック
driver.find_element(By.ID, "createBtn").click()
time.sleep(2)
# 入力欄にタイトルなどを入力
driver.find_element(By.CLASS_NAME, "form-input.event-name-input").send_keys("Python勉強会")
time.sleep(2)
