#imports
import math

#variables

charmap = ["▌", "▖", "▘"]

result = []

userput = input("Dollcode to translate: ")

operand = userput.split(" ")

block = []
chain = []

#functions
def charToDecimal(characterInput):

    dec = int(format(ord(characterInput), "x"), 16)

    return dec

def decToDollcode(userInput):

    workingOutput = []

    mult = (charToDecimal(userInput))

    while mult >= 1:

        mod = mult % 3

        if mod == 0 :

            mult = (mult - 3) / 3
        
        else: 
            
            mult = (mult - mod) / 3

        workingOutput.append(charmap[int(mod)])
    
    return "".join(reversed(workingOutput))
            
#main

#print(operand)

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
    