#variables

charmap = ["▌", "▖", "▘"]

output = []

userput = input("Text to translate: ")

operand = list(userput)

#functions

def charToDecimal(characterInput):

    dec = ord(characterInput)

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

for i in operand:

    output.append(decToDollcode(i))
    output.append("   ")
    

print("".join(output))