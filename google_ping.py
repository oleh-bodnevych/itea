#! /usr/bin/python3
import os
hostname = "Google.com"
response = os.system("ping -c 2 " + hostname)

#and then check
if response == 0:
  print ('\n',hostname, ' available!')
else:
  print('\n',hostname, 'is down!')
print("My Script working!!!!!!")

