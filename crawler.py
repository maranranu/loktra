from selenium import webdriver
import time
import sys

driver = webdriver.Firefox()
time.sleep(5)

url = 'http://www.shopping.com'
print url
driver.get(url)

arguments = sys.argv

keywords = arguments[1]

driver.get('http://shopping.com/products?KW='+keywords)

try:
	total = driver.find_element_by_xpath('//*[@id="sortFiltersBox"]/span[2]').text
	total = total.split(" ")
	print total[-1]
	try:
		driver.get('http://www.shopping.com/products~PG-'+arguments[2]+'?KW='+keywords)
		total_element = (driver.find_element_by_xpath('//*[@id="sortFiltersBox"]/span[2]').text).split(" ")
		print int(total_element[3])-int(total_element[1]) + 1
	except:
		print "page number is not passed or invalid page number"
		pass
except:
	print "No matches for given keyword"
	pass


