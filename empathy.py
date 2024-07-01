#imports
import marionette

doll = marionette.Marionette("s")

while True:
    prompt = input("e (encode), d (decode), or q to quit: ")

    if prompt == "q":
        break

    if prompt == "e":
        secondary = input("Text to encode: ")
        print(doll.encode(secondary))

    if prompt == "d":
        tertiary = input("Text to decode: ")
        try:
            print(doll.decode(tertiary))
        except:
            print("Hey! This isn't valid dollcode!")
