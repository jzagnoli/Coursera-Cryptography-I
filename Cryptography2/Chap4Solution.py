from Chap4Script import *


po = PaddingOracle()
mess="f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0" \
     "bdf302936266926ff37dbf7035d5eeb4"
print (mess)
print ("Length Message(in Hex)=",len(mess))
ctmess = mess.decode("Hex")
#print ("Ctmess =",ctmess)
print ("Length Message(in bytes)=",len(ctmess))

result = po.query("f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0"
                  "bdf302936266926ff37dbf7035d5eeb4")
print ("Original Cyphertext Result=",result)

result = po.query("f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0"
                  "bdf302936266926ff37dbf7035d5eeb5")
print ("ChangePad Cyphertext Result=", result)

result = po.query("e20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0"
                  "bdf302936266926ff37dbf7035d5eeb4")
print ("ChangeIV Cyphertext Result=", result)

ctlen = len(ctmess)

#ctguess = ctmess[0:ctlen-10]+ str(guess ^ int(ctmess[len-9]) ^ 0x01) + ctmess[:len-8]
#guess = 69
#print(guess)
#print(str(guess))

#ctguess = ctmess[0:ctlen-9] + chr(guess) + ctmess[ctlen-8:]
#print (mess[len(mess)-20:])
#print(ctguess[ctlen-10:].encode("Hex"))
#print ("Length of guess Message=",len(ctguess))

for guess in range(0,255):
    ctguess = ctmess[0:ctlen-17] + chr(guess)
    #print(ctguess.encode("Hex"))

    result = po.query(ctguess.encode("Hex"))
    #print result
    if  result:
        print(guess)
        print(ctguess[ctlen-32:].encode("Hex"))