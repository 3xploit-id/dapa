#!python3
#source code by mr.command

import os
from os import sys
import time
import subprocess

os.system('clear')

print ("""

###DALFOX X PARAMSPIDER###

""")
time.sleep(3)
os.system('clear')
print ('')
print ('PARAMSPIDER')
print ('')
time.sleep(3)

url = input ('website target : ')
op = input ('output param : ')

output = subprocess.check_output('pwd', shell=True)

current_directory = output.decode().rstrip('\n')

print ("")
print(f"Your File: {current_directory}/{op}")
print("")
paramm = input ("salin path di atas kesini  : ")
print("")
print ('''
paramspider
''')
os.system(f'python3 paramspider.py -d {url} -o {paramm}')
time.sleep(3)
print ('')
print ("DONE")
print ('')
time.sleep(3)
os.system('clear')

print ('''
dalfox
''')
time.sleep(6)
os.system(f'dalfox file {paramm} -o /home/mrcommand/resul.txt')
print ("""
done
""")
