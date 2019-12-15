#!/usr/bin/python3
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver=0
tdata=None
htmlsouce=None
def f1(url1):
	display = Display(visible=0, size=(1200, 1000))
	display.start()
	global driver
	driver=webdriver.Firefox()
	#she zhi yuan su deng dai 
	#driver.implicitly_wait(10)
	driver.get(url1)
	# shi yong  beautiful
	global htmlsouce
	htmlsouce=driver.page_source 
	#da yin ye mian
	#print(htmlsouce)
	soup=BeautifulSoup(htmlsouce,'lxml')
	ss1=soup.select('#cate_item1 > div:nth-child(1) > div:nth-child(2)')
	for tt1 in ss1:
		print(tt1)
	onedata()
	print('cai ji shu ju jie shu ')
	#guan bi webdriver
	driver.quit()
	display.stop()	
# huo qu yiji jie mian shu ju 
def onedata():
	data1=driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div[1]/div/ul').text										
	print(data1)
	pdata=driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div[1]/div/ul')
	sdata=pdata.find_elements_by_xpath("./li")
	# zai zhe li shui mian  5 miao  yong lai yidong kai shu biao  fou ze hui ying xiang shu ju cai ji
	time.sleep(5)
	#kai shi shu ju cai ji
	twodata(sdata)
#huo qu mei yi xia mian de zi lian jie 
def twodata(sdata1):
	#ding yi yige  ju bu bian liang
	a=1
	ac=ActionChains(driver)
	# ju jiao
	for x in sdata1:
		#dui mei ge yuan su ju jiao
		print(x.text)
		time.sleep(2)
		ac.move_to_element_with_offset(x,10,10).perform()		
		time.sleep(2)
		#huo huo qu yuan su
		print(a)
		#js1='document.querySelector('#cate_item1 > div:nth-child(1) > div:nth-child(2)')
		#jsd="var uu=document.querySelector('#cate_item"+str(a)+" > div:nth-child(1) > div:nth-child(2)'); return uu;"
		jsd1="var uu=document.querySelector('#cate_item"+str(a)+" .cate_detail'); return uu;"
		print(jsd1)
		t1=driver.execute_script(jsd1)
																	#cate_item1 > div:nth-child(1) > div:nth-child(2)
																	#cate_item2 > div:nth-child(1) > div:nth-child(2)
																	#cate_item3 > div:nth-child(1) > div:nth-child(2)
																	#cate_item2 > div:nth-child(1)
																	#cate_item2 .cate_detail																	
		# she zhi shi tu dui qi 
		#if a%7==0:
		#	driver.execute_script('arguments[0].scrollIntoView();',t1) 
		'''
		# @1   deng dai yuan su |she zhi yuan su deng dai
		cs1='#cate_item'+str(a)+' .cate_detail'
		print(cs1)
		t1=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,cs1)))
		classtext=t1.get_attribute('class')
		print(classtext)
		'''
		 
		#assert t1 is not null
		#print(t1)
		#t1='/html/body/div[1]/div[5]/div[1]/div[1]/div/div/div['+str(a)+']/div[1]/div[2]'
		#try:
		#	global tdata
		#	tdata=x.find_element_by_xpath(t1)
											
		#except Exception as e:
		#	raise
		#else:
		#	print('....................................................................')
		#finally:
		#driver.quit()
		tdatas=t1.find_elements_by_xpath('./*')	
		time.sleep(1)
		#time.sleep(2.5)
		#ji xu huo qu zi yuan su
		for x1 in tdatas:
			#dui liang ge zi dui xiang feng bie cao zuo 
			#da  yin zhong lei
			print('zhong lei '+x1.find_element_by_xpath('./dt').text)
			#dui di er ge zilei ji xu huo qu 
			xs=x1.find_element_by_xpath('./dd')
			xss=xs.find_elements_by_xpath('./*')
			for x2 in xss:
				print(x2.text) 
		#dui  div wei zhi geng xin 	
		print('5555555555555555555555555555')		
		a=a+1	
		print(a)
if __name__=='__main__':
	url='https://www.jd.com'
	f1(url)
