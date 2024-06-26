# Marionette
class Marionette:

    def __init__(self):
        self.charmap = ["▌", "▖", "▘"]
        self.decodemap = ["▖", "▘", "▌"]

        self.output = []

    # This function performs the character by character conversion for the encode function
    def CharToDollcode(self, In):

        #intermediate dollcode output storer
        intermediate = []

        #perform the unicode to decimal conversion
        multiplier = ord(In)


        while multiplier >= 1:

            mod = multiplier % 3

            if mod == 0 :

                multiplier = (multiplier - 3) / 3
            
            else: 
                
                multiplier = (multiplier - mod) / 3

            intermediate.append(self.charmap[int(mod)])
    
        return "".join(reversed(intermediate))

    # One of the two primary Marionette functions, it performs string-wide encoding from unicode to dollcode
    def encode(self, In):
        
        #clear the output to make sure stuff doesn't get mixed up
        self.output.clear()

        for o in list(In):
            self.output.append(self.CharToDollcode(o))
            self.output.append(" ")

        return "".join(self.output)

    # The second primary Marionette function, it performs decoding from dollcode to unicode
    def decode(self, In):

        #clear the output to make sure stuff doesn't get mixed up
        self.output.clear()

        operand = In.split(" ")

        result = []

        block = []

        for o in operand:
            decode = list(o)
            for d in decode:
                block.append(str(self.decodemap.index(d) +1))

            fixedblock = list(reversed(block))

            p = 0
            dec = 0
            for f in fixedblock:
                dec += (3 ** p)*int(f)
                p += 1

            result.append(chr(dec))
            block.clear()
            fixedblock.clear()

        return "".join(result)