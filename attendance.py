from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import re
from selenium import *
import urllib
import os
from selenium.webdriver.common.keys import Keys
import sys
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def names(info,choices):
	output = process.extractOne(info, choices)
	return(output[0])
	print(output[0])

fieldtriplist = ["FieldTrip","Fieldtrip","fieldtrip","field trip","field-trip"]
offsitelist = ["Offsite","offsite","off-site","off site"]
checkoutlist = ["checkout","CheckOut","Check-Out","Check Out"]

studentid=0

if sys.argv[1] == "help":
	print("Incorrect Usage!")
	print("arguments follow:")
	print("password, statusname, returntime, info, studentid...")
	print("note that custom facilitators and offsite locations are currently unavalible")
	print("example:")
	print("attendance.py Integrity! Offsite 11:30 Pings 40 50 17")
	sys.exit()
studentcounter = 5
password = sys.argv[1]

if len(sys.argv)==4:
	statusname = sys.argv[2]
	studentcounter = 3
else:
	statusname = sys.argv[2]
	returntime = sys.argv[3]
	info = sys.argv[4]

if len(sys.argv) > studentcounter+1:
	studentids = []
	for i in range(0,len(sys.argv)-studentcounter):
		studentids.append(sys.argv[i+studentcounter])
		print(sys.argv[i+studentcounter])
else:
	studentid = sys.argv[studentcounter]
	
print(statusname)
chromedriver = 'C:\\Windows\\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)

browser.get("http://attendance.pscs.org/secondary_login.php?PBM=2") 
time.sleep(3)

username = browser.find_element_by_id("mypassword")
username.send_keys(password)

login_attempt = browser.find_element_by_name("Submit")
login_attempt.click();
time.sleep(3)
if len(returntime) == 4:
	returntime = returntime[:2] + ':' + returntime[2:]
	print("corrected returntime")

if studentid == 0:
	for k in range(0,len(studentids)):
		checkbox = browser.find_element_by_id(studentids[k])
		checkbox.click()
else:
	checkbox = browser.find_element_by_id(studentid)
	checkbox.click()

if statusname in offsitelist:
	whenreturn = browser.find_element_by_id("offtime")
elif statusname in fieldtriplist:
	whenreturn = browser.find_element_by_id("fttime")
if statusname in offsitelist or statusname in fieldtriplist:
	whenreturn.send_keys(returntime)

if statusname in offsitelist:
	gobutton = browser.find_element_by_name("offsite")
	info = names(info, ['World Pizza', 'Uwajimaya', 'Starbucks', "Specialty's", 'Eastern Cafe', 'Oasis', 'Pings', 'Chipotle', 'Marination'])
	browser.find_element_by_xpath("//option[@value='" + info + "']").click()
elif statusname == "present":
	gobutton = browser.find_element_by_name("present")
elif statusname in checkoutlist:
	gobutton = browser.find_element_by_name("checkout")
elif statusname in fieldtriplist:
	gobutton = browser.find_element_by_name("fieldtrip")
	if info == "Krista":
		info = "Crysta"
		print("corrected name")
	info = names(info,['Crysta', 'Scobie', 'Liana', 'Nic', 'Andy', 'Special_Aproved', 'Chrissy', 'Sam', 'Sieglinde', 'Anne', 'Kristin_J', 'Melinda', 'Dan', 'Judy', 'Quinn_H'])
	browser.find_element_by_xpath("//option[@value='" + info + "']").click()
gobutton.click();
time.sleep(3)

output = browser.page_source.encode('utf-8')
if '<div class="error"' in output:
	print("Sorry, incorrect usage, please review the help command")
f = open('attendance_output.html','w')
f.write(output)
f.close()
browser.quit()
