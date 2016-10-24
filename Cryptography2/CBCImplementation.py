from __future__ import print_function
import sys
from Crypto.Cipher import AES
from Crypto.Util import Counter

CBCKey ="140b41b22a29beb4061bda66b6747e14".decode("Hex")
CTRKey ="36f18357be4dbd77f050515c73fcf9f2".decode("Hex")
CBCCTR  = ["4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81".decode("Hex"),
           "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253".decode("Hex"),
           "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329".decode("Hex"),
           "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451".decode("Hex")]


def CBCDecode(key,ctraw,mode):
    iv  = ctraw[:16]
    ct  = ctraw[16:]  
    if mode == 2:
        cipher = AES.new(key, mode, iv)
        ptr = cipher.decrypt(ct)
        pad = ptr[len(ptr) - 1]
        print("Mode=", mode, " Key=", key.encode("Hex"), " Ct=", ct.encode("Hex"))
        print("Pad Length=", ord(pad))
        msglen = len(ptr) - ord(pad)
        result = ptr[0:msglen]
    else:
        ctr = Counter.new(128,initial_value=long(iv.encode("Hex"),16))
        print("IV=",iv.encode("Hex"))
        #print("Counter=", ctr().encode("Hex")) #this will cause the counter to be incremented
        print("Mode=",mode," Key=",key.encode("Hex")," Ct=",ct.encode("Hex"))
        cipher1 = AES.new(key, mode, iv, counter=ctr)
        result = cipher1.decrypt(ct)
        #print("Counter=", ctr().encode("Hex"))

    return(result)
#lenkey = len(CBCKey)
#print("Key length=",lenkey)
#lenct = len(CBCCT)
#print("CT length=",lenct)
#lenciv = len(CBCIV)
#print("IV length=",lenciv)

for i in range(4):
    print("Raw Ciphertext=",CBCCTR[i].encode("Hex"))
    if   i < 2:
        MODE = AES.MODE_CBC
        print("Plaintext=", CBCDecode(CBCKey, CBCCTR[i], MODE), "'")
    else:
        MODE = AES.MODE_CTR
        print("Plaintext=", CBCDecode(CTRKey, CBCCTR[i], MODE), "'")
    print

