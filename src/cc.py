from faker import Faker
import os
from time import sleep

vuln=[]
os.system('clear')
amount = int(raw_input("Amount > "))
print""
for i in range(amount):
	fake = Faker()
	nums = fake.credit_card_number()
	nums = nums[::-1]
	empty = []
	index_counter = 0
	for num in nums:
	    if (index_counter % 2) != 0:
	        num = int(num)
	        num *= 2
	        empty.append(num)
	        index_counter += 1
	    else:
        	num = int(num)
	        empty.append(num)
	        index_counter += 1
	index_counter = 0
	for num in empty:
	    if num > 9:
	        empty[index_counter] -= 9
	    index_counter += 1
	SUM = sum(empty)
	if SUM % 10 == 0 and len(nums)==16:
	    print(nums + " => \033[1;92mAktif\033[0m")
	    vuln.append(nums)
	else:
	    print(nums + "= >\033[1;91mNonaktif\033[0m")
	sleep(0.5)

print('\nSelesai!')
