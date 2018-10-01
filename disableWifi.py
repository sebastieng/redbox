from  sfrbox import *


hashLogin = open('hashLogin.txt', 'r').read().rstrip()
hashPassword = open('hashPassword.txt', 'r').read().rstrip()

sfrBox=SfrBox(hashLogin,hashPassword)
sfrBox.disableWifi()
