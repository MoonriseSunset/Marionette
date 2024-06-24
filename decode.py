#variables

result = []

userput = input("Dollcode to translate: ")

operand = userput.split(" ")

block = []
chain = []
       
#main

for o in operand:
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
        dec += (3 ** p)*int(f)
        p += 1

    result.append(chr(dec))
    
    block.clear()
    fixedblock.clear()
print("".join(result))
    