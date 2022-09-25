from sys import argv
import os

script = argv
name = str(script[0])

cmd = 'comeca preencher.txt'
os.system(cmd)
os.mkdir('clone')
os.system(r'copy preencher.txt clone')
os.system(r'copy replicator.py clone')
os.system(r'copy '+name+' clone')