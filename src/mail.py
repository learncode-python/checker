import requests, json, sys, hashlib, mechanize, os
from bs4 import BeautifulSoup as bs
from time import sleep
from faker import Faker

vuln = []
try:
	os.system('rm -rf aktif.txt')
except:
	pass
os.system('clear')
amout = int(raw_input("Amount > "))
print""
for x in range(amout):
	fake = Faker('id_ID')
	a = fake.email()
	if 'gmail.com' in a:

		br = mechanize.Browser()
		br.set_handle_robots(False)
		br.open("https://accounts.google.com/servicelogin")
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form["Email"] = a
		r = br.submit()
		if "Find my account" in r.read():
			print(a +" => \033[1;91mNonaktif\033[0m")
		else:

			b = a +" => \033[1;92mAktif\033[0m"
			print(b)
			vuln.append(a)


	elif 'yahoo.com' in a:

		br=mechanize.Browser()
		br.set_handle_robots(False)
		br.open('https://login.yahoo.com/config/login')
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form["username"] = a
		r = br.submit()
		if "messages.ERROR_INVALID_USERNAME" in r.read():
			print(a +" => \033[1;91mNonaktif\033[0m")
		else:
			print(a +" => \033[1;92mAktif\033[0m")
			vuln.append(a)

try:
	f = open('aktif.txt','w')
except IOError:
	pass
for i in vuln:
	f.write(i + '\n')
f.close()
print('')
print('Selesai. File disimpan di folder src/ aktif.txt')
exit()
