#imports
import marionette

doll = marionette.Marionette()

while True:
    prompt = input("e (encode), d (decode), m (switch modes), or q to quit: ")

    if prompt == "q":
        break

    elif prompt == "m":
        DecodeEncode = input("Switch modes, e (encode) or d (decode): ")
        secondary = input("Type, d (decimal) | h (hex) | c (char) | s (string) | l (output type)| : ")
        temp = doll.switchMode(DecodeEncode,secondary)
        
        if temp == -1:
            print("Did not recieve e/d for encode/decode")

        elif temp == -2:
            print("Did not recieve d/h/c/s for mode switch")

        else:
            print("Mode is:", temp)

    elif prompt == "e":
        secondary = input("Input to encode: ")
        print(doll.encode(secondary))

    elif prompt == "d":
        tertiary = input("Dollcode to decode: ")
        try:
            print(doll.decode(tertiary))
        except:
            print("Hey! This isn't valid dollcode or mode is wrong!")

    else:
        print("Invalid command")
