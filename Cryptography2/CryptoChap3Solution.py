from __future__ import print_function
import sys
from Crypto.Hash import SHA256
from Crypto.Util import Counter

f=open("/home/john/Videos/6.1.intro.mp4",mode='rb')
#f=open("/home/john/Videos/6.2.birthday.mp4",mode='rb')
i = 0
data = [None]*10000000
data[i]=f.read(1024)
while data[i] <> '':
    i = i + 1
    data[i]=f.read(1024)
    if i > 12000:
        print ("i=",i,"  Length=",len(data[i]))
        print(data[i][:50].encode("Hex"))
last = i-1
print("last block#",last)
#print ('i=',i-1,"  Length=",len(data[i-1]))
#print (data[i-1][:10].encode("Hex"))
#print ('i=',i,"  Length=",len(data[i]))
#print (data[i])
dout = [None]*(last+1)
dout[last] = data[last]
for j in range(last,-1,-1):
    datain = dout[j]
    hash = SHA256.new(datain)
    if j <> 0:
        dout[j-1] = data[j-1]+(hash.digest())
    if j > (last-2):
        print("j=", j, "  Length=", len(dout[j]))
        print(data[i][:50].encode("Hex"))
    if j <  2:
        print('Block#',j)
        print("Hash=",hash.hexdigest())