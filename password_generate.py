import random
import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="QWERTYUIOPASDFGHJKLZXCVBNM"
num="0123456789"
sym="!@#*-_?"
all =lower+upper+num+sym
len=16
password="".join(random.sample(all, len))
print (password)