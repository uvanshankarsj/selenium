from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()

driver.get("https://www.amazon.in/?&ext_vrnc=hi&ref=pd_sl_7hz2t19t5c_e&adgrpid=58355126069&hvpone=&hvptwo=&hvadid=610644601173&hvpos=&hvnetw=g&hvrand=9131234810492690557&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9148909&hvtargid=kwd-10573980&hydadcr=14453_2316415")
driver.maximize_window()
driver.implicitly_wait(1)
myelement=driver.find_element(By.ID,"twotabsearchtextbox")
myelement.send_keys("10th gen processor i7")
driver.implicitly_wait(1)
# driver.implicitly_wait(30)
# myelement=driver.find_element(By.ID,"password")
# myelement.send_keys("w7-[q=8,")
# driver.implicitly_wait(30)
myelement=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
myelement.click()
# driver.get_screenshot_as_file("testing.png")
myelement=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/span/div/h1/div/div[2]/div/div/form/span/span/span/span")
myelement.click()
myelement=driver.find_element(By.ID,"s-result-sort-select_4")
myelement.click()
driver.implicitly_wait(5)
driver.back()
# for i in range(10000):
    # print("hi")
# driver.implicitly_wait(100)
# searchBar = driver.findElement(By.id("lst-kw"));