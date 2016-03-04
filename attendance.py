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
	
def getid(name):
	studentdict = {'Adin':55, 'Aidan':72, 'Angus':17, 'Anthony':29, 'Arturo':81, 'Asher':21, 'Aster':78, 'Audrey':31, 'Beck':85, 'Bryce':37, 'Cory':77, 'David':57, 'Easton':30, 'Eli':58, 'Elijah':20, 'Finn':42, 'Graeme':59, 'Grant':39, 'Hazel':60, 'Isaac':41, 'Bella':19, 'Jack':36, 'Jake':27, 'Jasmin':86, 'Jessie':35, 'Jon':48, 'Joshua':18, 'Joy':61, 'Justin':80, 'Kayleigh':26, 'Kyle':84, 'Madeleine':82, 'Margaux':14, 'Marissa':33, 'Milo':43, 'Miranda':76, 'Niall':32, 'Olive':51, 'Olivia':83, 'Oscar':79, 'Peyton':25, 'Quinn':7, 'River':47, 'Ruby':62, 'Sam':34, 'Sara':63, 'Sasha':64, 'Shane':65, 'Simon':40, 'Sofia':28, 'Spencer':24, 'Xin':66, 'Zane':67}
	return(studentdict[name])

fieldtriplist = ["FieldTrip","Fieldtrip","fieldtrip","field trip","field-trip"]
offsitelist = ["Offsite","offsite","off-site","off site"]
checkoutlist = ["checkout","CheckOut","Check-Out","Check Out"]

studentid=0

if sys.argv[1] == "help":
	print("Incorrect Usage!")
	print("arguments follow:")
	print("password, studentname, statusname, info, returntime")
	print("note that custom facilitators and offsite locations are currently unavalible")
	print("example:")
	print("attendance.py Integrity! Offsite 11:30 Pings milo easton river")
	sys.exit()


password = sys.argv[1]
studentid = sys.argv[2]
statusname = sys.argv[3]
if len(sys.argv) >= 5:
    info = sys.argv[4]
if len(sys.argv) >= 6:
    returntime = sys.argv[5]
    if ":" not in returntime:
        if len(returntime) == 3:
            returntime = returntime[:1] + ':' + returntime[1:]
        else:
            returntime = returntime[:2] + ':' + returntime[2:]
    print(returntime)
chromedriver = 'C:\\Windows\\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)

browser.get("http://attendance.pscs.org/secondary_login.php?PBM=2") 
time.sleep(3)

username = browser.find_element_by_id("mypassword")
username.send_keys(password)

login_attempt = browser.find_element_by_name("Submit")
login_attempt.click();
time.sleep(3)

if studentid == 0:
	for k in range(0,len(studentids)):
		checkbox = browser.find_element_by_id(studentids[k])
		checkbox.click()
else:
	studentid = getid(names(studentid,['Adin','Aidan','Angus','Anthony','Arturo','Asher','Aster','Audrey','Beck','Bryce','Cory','David','Easton','Eli','Elijah','Finn','Graeme','Grant','Hazel','Isaac','Bella','Jack','Jake','Jasmin','Jessie','Jon','Joshua','Joy','Justin','Kayleigh','Kyle','Madeleine','Margaux','Marissa','Milo','Miranda','Niall','Olive','Olivia','Oscar','Peyton','Quinn','River','Ruby','Sam','Sara','Sasha','Shane','Simon','Sofia','Spencer','Xin','Zane']))
	studentid = str(studentid)
	checkbox = browser.find_element_by_id(studentid)
	checkbox.click()

if statusname in offsitelist:
	whenreturn = browser.find_element_by_id("offtime")
elif statusname in fieldtriplist:
	whenreturn = browser.find_element_by_id("fttime")
if statusname in offsitelist or statusname in fieldtriplist:
	whenreturn.send_keys(returntime)

if statusname in offsitelist:
    print("offsite")
    gobutton = browser.find_element_by_name("offsite")
    info = names(info, ['World Pizza', 'Uwajimaya', 'Starbucks', "Specialty's", 'Eastern Cafe', 'Oasis', 'Pings', 'Chipotle', 'Marination'])
    browser.find_element_by_xpath("//option[@value='" + info + "']").click()
elif statusname in checkoutlist:
    print("checkout")
    gobutton = browser.find_element_by_name("checkout")
elif statusname in fieldtriplist:
    print("fieldtrip")
    gobutton = browser.find_element_by_name("fieldtrip")
    if info == "Krista":
        info = "Crysta"
    info = names(info,['Crysta', 'Scobie', 'Liana', 'Nic', 'Andy', 'Special_Aproved', 'Chrissy', 'Sam', 'Sieglinde', 'Anne', 'Kristin_J', 'Melinda', 'Dan', 'Judy', 'Quinn_H'])
    browser.find_element_by_xpath("//option[@value='" + info + "']").click()
else:
    print("present")
    time.sleep(5)
    #gobutton = browser.find_element_by_name("present")
    gobutton = browser.find_element_by_xpath("//input[@class='PSCSbtn button']")
    for i in browser.find_elements_by_xpath("//*[@type='submit']"):
        print(i.get_attribute("value") + " : " + i.get_attribute("name") + " : " + i.get_attribute("id") + " : " + i.get_attribute("class"))
    print("gobutton : " + str(gobutton))

gobutton.click();
time.sleep(10)

output = browser.page_source.encode('utf-8')
if '<div class="error"' in output:
	print("Sorry, incorrect usage, please review the help command")
f = open('attendance_output.html','w')
f.write(output)
f.close()
browser.quit()
