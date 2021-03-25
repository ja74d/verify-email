#!/usr/bin/python3.9

from verify_email import verify_email

import os

os.system('clear')

email = input(str('enter email:'))

result = verify_email(email)

if result == True:
	print(f'<<{email}>> is exist!')
else:
	print(f'<<{email}>> is not exist!!!')
