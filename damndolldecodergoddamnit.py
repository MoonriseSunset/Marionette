#imports
import math

#variables

result = []

userput = input("Dollcode to translate: ")

operand = userput.split(" ")

block = []
chain = []
       
#main

for o in operand:
    #print("Highest Level:" + str(list(o)))
    decode = list(o)
    for d in decode:
        if(d == "▌"):
            block.append("3")
        elif(d == "▖"):
            block.append("1")
        elif(d == "▘"):
            block.append("2")

    
    fixedblock = list(reversed(block))

    p = 0
    dec = 0
    for f in fixedblock:
        #print(f)
        dec += (3 ** p)*int(f)
        p += 1
    #print(dec)
    result.append(chr(dec))

    #print("Raw Block:" + str(block))
    #print("Fixed Block:" + str(fixedblock))
    block.clear()
    fixedblock.clear()
print("".join(result))
    