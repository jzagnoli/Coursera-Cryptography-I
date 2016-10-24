from __future__ import print_function
import sys

MSGS = [
    "315c4eeaa8b5f8aaf9174145bf43e1784b8fa00dc71d885a804e5ee9fa40b16349c146fb778cdf2d3aff021dfff5b403b510d0d0455468aeb98622b137dae857553ccd8883a7bc37520e06e515d22c954eba5025b8cc57ee59418ce7dc6bc41556bdb36bbca3e8774301fbcaa3b83b220809560987815f65286764703de0f3d524400a19b159610b11ef3e".decode(
        "Hex"),
    "234c02ecbbfbafa3ed18510abd11fa724fcda2018a1a8342cf064bbde548b12b07df44ba7191d9606ef4081ffde5ad46a5069d9f7f543bedb9c861bf29c7e205132eda9382b0bc2c5c4b45f919cf3a9f1cb74151f6d551f4480c82b2cb24cc5b028aa76eb7b4ab24171ab3cdadb8356f".decode(
        "Hex"),
    "32510ba9a7b2bba9b8005d43a304b5714cc0bb0c8a34884dd91304b8ad40b62b07df44ba6e9d8a2368e51d04e0e7b207b70b9b8261112bacb6c866a232dfe257527dc29398f5f3251a0d47e503c66e935de81230b59b7afb5f41afa8d661cb".decode(
        "Hex"),
    "32510ba9aab2a8a4fd06414fb517b5605cc0aa0dc91a8908c2064ba8ad5ea06a029056f47a8ad3306ef5021eafe1ac01a81197847a5c68a1b78769a37bc8f4575432c198ccb4ef63590256e305cd3a9544ee4160ead45aef520489e7da7d835402bca670bda8eb775200b8dabbba246b130f040d8ec6447e2c767f3d30ed81ea2e4c1404e1315a1010e7229be6636aaa".decode(
        "Hex"),
    "3f561ba9adb4b6ebec54424ba317b564418fac0dd35f8c08d31a1fe9e24fe56808c213f17c81d9607cee021dafe1e001b21ade877a5e68bea88d61b93ac5ee0d562e8e9582f5ef375f0a4ae20ed86e935de81230b59b73fb4302cd95d770c65b40aaa065f2a5e33a5a0bb5dcaba43722130f042f8ec85b7c2070".decode(
        "Hex"),
    "32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd2061bbde24eb76a19d84aba34d8de287be84d07e7e9a30ee714979c7e1123a8bd9822a33ecaf512472e8e8f8db3f9635c1949e640c621854eba0d79eccf52ff111284b4cc61d11902aebc66f2b2e436434eacc0aba938220b084800c2ca4e693522643573b2c4ce35050b0cf774201f0fe52ac9f26d71b6cf61a711cc229f77ace7aa88a2f19983122b11be87a59c355d25f8e4".decode(
        "Hex"),
    "32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd90f1fa6ea5ba47b01c909ba7696cf606ef40c04afe1ac0aa8148dd066592ded9f8774b529c7ea125d298e8883f5e9305f4b44f915cb2bd05af51373fd9b4af511039fa2d96f83414aaaf261bda2e97b170fb5cce2a53e675c154c0d9681596934777e2275b381ce2e40582afe67650b13e72287ff2270abcf73bb028932836fbdecfecee0a3b894473c1bbeb6b4913a536ce4f9b13f1efff71ea313c8661dd9a4ce".decode(
        "Hex"),
    "315c4eeaa8b5f8bffd11155ea506b56041c6a00c8a08854dd21a4bbde54ce56801d943ba708b8a3574f40c00fff9e00fa1439fd0654327a3bfc860b92f89ee04132ecb9298f5fd2d5e4b45e40ecc3b9d59e9417df7c95bba410e9aa2ca24c5474da2f276baa3ac325918b2daada43d6712150441c2e04f6565517f317da9d3".decode(
        "Hex"),
    "271946f9bbb2aeadec111841a81abc300ecaa01bd8069d5cc91005e9fe4aad6e04d513e96d99de2569bc5e50eeeca709b50a8a987f4264edb6896fb537d0a716132ddc938fb0f836480e06ed0fcd6e9759f40462f9cf57f4564186a2c1778f1543efa270bda5e933421cbe88a4a52222190f471e9bd15f652b653b7071aec59a2705081ffe72651d08f822c9ed6d76e48b63ab15d0208573a7eef027".decode(
        "Hex"),
    "466d06ece998b7a2fb1d464fed2ced7641ddaa3cc31c9941cf110abbf409ed39598005b3399ccfafb61d0315fca0a314be138a9f32503bedac8067f03adbf3575c3b8edc9ba7f537530541ab0f9f3cd04ff50d66f1d559ba520e89a2cb2a83".decode(
        "Hex"),
    "".decode("Hex")]

TARGET = "32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904".decode("Hex")
PADx = [None] * 136
PADx[0] = "66" ;   PADx[1] = "39" ;   PADx[2] = "6e" ;   PADx[3] = "89" ;   PADx[4] = "c9";   PADx[5] = "db" ;   PADx[6] = "d8";   PADx[7] = "cc";
PADx[8] = "98" ;   PADx[9] = "74" ;   PADx[10] = "35" ;  PADx[11] = "2a" ;  PADx[12] = "cd";  PADx[13] = "63" ;  PADx[14] = "95";  PADx[15] = "10";
PADx[16] = "2e" ;  PADx[17] = "af" ;  PADx[18] = "ce" ;  PADx[19] = "78" ;  PADx[20] = "aa";  PADx[21] = "7f" ;  PADx[22] = "ed";  PADx[23] = "28";
PADx[24] = "a0" ;  PADx[25] = "7f" ;  PADx[26] = "6b" ;  PADx[27] = "c9" ;  PADx[28] = "8d";  PADx[29] = "29" ;  PADx[30] = "c5";  PADx[31] = "0b";
PADx[32] = "69" ;  PADx[33] = "b0" ;  PADx[34] = "33" ;  PADx[35] = "9a" ;  PADx[36] = "19";  PADx[37] = "f8" ;  PADx[38] = "aa";  PADx[39] = "40";
PADx[40] = "1a" ;  PADx[41] = "9c" ;  PADx[42] = "6D" ;  PADx[43] = "70" ;  PADx[44] = "8f";  PADx[45] = "80" ;  PADx[46] = "c0";  PADx[47] = "66";
PADx[48] = "c7" ;  PADx[49] = "63" ;  PADx[50] = "fe" ;  PADx[51] = "f0" ;  PADx[52] = "12";  PADx[53] = "31" ;  PADx[54] = "48";  PADx[55] = "cd";
PADx[56] = "d8" ;  PADx[57] = "e8" ;  PADx[58] = "02" ;  PADx[59] = "d0" ;  PADx[60] = "5b";  PADx[61] = "a9" ;  PADx[62] = "87";  PADx[63] = "77";
PADx[64] = "33" ;  PADx[65] = "5d" ;  PADx[66] = "ae" ;  PADx[67] = "fc" ;  PADx[68] = "ec";  PADx[69] = "d5" ;  PADx[70] = "9c";  PADx[71] = "43";
PADx[72] = "3a" ;  PADx[73] = "6b" ;  PADx[74] = "26" ;  PADx[75] = "8b" ;  PADx[76] = "60";  PADx[77] = "bf" ;  PADx[78] = "4e";  PADx[79] = "f0";
PADx[80] = "3c" ;  PADx[81] = "9a" ;  PADx[82] = "61" ;  PADx[83] = "10" ;  PADx[84] = None;  PADx[85] = "00" ;  PADx[86] = "00";  PADx[87] = "00";
PADx[88] = "00" ;  PADx[89] = "00" ;  PADx[90] = "00" ;  PADx[91] = "00" ;  PADx[92] = "00";  PADx[93] = "00" ;  PADx[94] = "00";  PADx[95] = "00";
PADx[96] = "00" ;  PADx[97] = "00" ;  PADx[98] = "00" ;  PADx[99] = "00" ;  PADx[100] = "00"; PADx[101] = "00" ; PADx[102] = "00"; PADx[103] = "00";
PADx[104] = "00" ; PADx[105] = "00" ; PADx[106] = "00" ; PADx[107] = "00" ; PADx[108] = "00"; PADx[109] = "00" ; PADx[110] = "00"; PADx[111] = "00";
PADx[112] = "00" ; PADx[113] = "00" ; PADx[114] = "00" ; PADx[115] = "00" ; PADx[116] = "00"; PADx[117] = "00" ; PADx[118] = "00"; PADx[119] = "00";
PADx[120] = "00" ; PADx[121] = "00" ; PADx[122] = "00" ; PADx[123] = "00" ; PADx[124] = "00"; PADx[125] = "00" ; PADx[126] = "00"; PADx[127] = "00";
PADx[128] = "00" ; PADx[129] = "00" ; PADx[130] = "00" ; PADx[131] = "00" ; PADx[132] = "00"; PADx[133] = "00" ; PADx[134] = "00"; PADx[135] = "00";



def strxor(a, b):  # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

    # for msg in MSGS:
    #   print ("Msg=")
    #  print(msg.encode("Hex"))

def prtguess(cyphertext,index):
    guess = strxor(PAD, cyphertext)
    for t in range(83):
        guesschar = guess[t]
        if PADx[t] == None:
            print(" ", end="")
        else:
            print(guesschar, end="")

    print("   Message=",index," LenTarget=", len(cyphertext))

def prtpos():
    for i in range(len(TARGET)):
        if (i % 10) == 0:
            print(int(i / 10), end="")
        else:
            print(" ", end="")
    print()
    for i in range(len(TARGET)):
        print((i % 10), end="")
    print()

def prthex(cyphertext):
    for t in range(len(cyphertext)):
        print(cyphertext[t].encode("Hex"), "", end="")
    print()

def prthexpos():
    for i in range(156):
        if i < 10:
            print("", i, "", end="")
        elif i < 100:
            print(i, "", end="")
        else:
            print(i, end="")
    print("")

#PAD = ''.join(PADx).decode("Hex")
PAD = ""
for i in range(len(PADx)):
    if PADx[i] == None:
        PAD = PAD + "0"
    else:
        PAD = PAD + (PADx[i].decode("Hex"))

def prthexspc(guesstext):
    for t in range(len(result)):
        if 48 < ord(result[t]) < 122:
            print("XX", "", end="")
        else:
            print(result[t].encode("Hex"), "", end="")
    print("")



testmsg = 0

print("\n")

print("TESTMGS=", testmsg, " Len=", len(MSGS[testmsg]))

prthex(MSGS[testmsg])

prthexpos()
print()

for i in range(0, 10):
    if i != testmsg:
        print("MSG=", i, " Len=", len(MSGS[i]))
        result = strxor(MSGS[testmsg],MSGS[i])
        prthexspc(result)
        prthexpos()
        prthex(MSGS[i])
        print()

prthex(TARGET)
prtguess(TARGET,99)
for i in range(0, 10):
    prtguess(MSGS[i],i)
prtpos()