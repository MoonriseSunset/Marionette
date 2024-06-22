#imports
import math

#variables

charmap = ["▌", "▖", "▘"]

output = []

userput = input("Text to translate: ")

operand = list(userput)

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
            

    #print("".join(reversed(workingOutput)))
    #print("")

#main

for i in operand:

    output.append(decToDollcode(i))
    output.append("   ")
    

print("".join(output))