#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')

import requests
if not os.path.isfile('Jutt.so'):
    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/Juttbrand/main/Jutt.cpython-310.so > Jutt.so')
    os.system('clear')
if not os.path.isfile('brand.so'):
    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/Juttbrand/main/brand.cpython-310.so > brand.so')
    os.system('clear')
bit=platform.architecture()[0]
if bit == '64bit':
    from Jutt import reg
    reg()
elif bit == '32bit':
    from brand import reg
    reg()
