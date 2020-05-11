import os, sys

class Main:
	def __init__(self):
		"""Coded By Khazul yussery"""
		self.os = os.system

	def mails(self):
		self.os('cd src;python2 mail.py')

	def cc(self):
		self.os('cd src;python2 cc.py')


main = Main()
os.system('clear')
print("""
	Mail dan Credit Card Checker
	----------------------------

	1). Email checker
	2). Credit Card checker\n""")
choice = raw_input('pilih > ')
if choice == "1":
	main.mails()
elif choice == "2":
	main.cc()
else:
	exit('GoodBye')
