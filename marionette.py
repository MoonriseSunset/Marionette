# Marionette
class Marionette:

    def __init__(self):
        self.charmap = ["▌", "▖", "▘"]
        self.decodemap = ["▖", "▘", "▌"]

        self.validModes = ["s", "c", "h", "d", "l"]

        self.output = []

        # Encode/Decode Modes, defaulting to string
        # s = string, c = char, h = hex, d = dec
        self.eMode = "s"

        self.dMode = "s"
    
    def switchMode(self, decodeEncode, mode):

        try:
            M = self.validModes.index(mode)
        except:
            return -2    

        if decodeEncode == "d":

            if mode == "l":
                return self.dMode
            
            self.dMode = mode
            return mode
        
        elif decodeEncode == "e":

            if mode == "l":
                return self.eMode
            
            self.eMode = mode
            return mode

        else:
            return -1
            

    def DecToDollcode(self, In):

        #intermediate dollcode output storer
        intermediate = []

        multiplier = int(In)

        while multiplier >= 1:

            mod = multiplier % 3

            if mod == 0 :

                multiplier = (multiplier - 3) / 3
            
            else: 
                
                multiplier = (multiplier - mod) / 3

            intermediate.append(self.charmap[int(mod)])
    
        return "".join(reversed(intermediate))

    # This function performs the character by character conversion for the encode function
    def CharToDollcode(self, In):

        return self.DecToDollcode(ord(In))
    
    def HexToDollcode(self, In):

        return self.DecToDollcode(int(In, 16))
    
    def DecodeToDecOLD(self, In):
        #clear the output to make sure stuff doesn't get mixed up
        self.output.clear()

        result = []

        block = []

        decode = list(In)
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

        result.append(dec)
        block.clear()
        fixedblock.clear()

        return result[0]
    
    def DecodeToDec(self, In):
        #clear the output to make sure stuff doesn't get mixed up
        self.output.clear()

        result = []

        block = []

        decode = list(In)
        for d in decode:
            block.append(str(self.decodemap.index(d) +1))

        fixedblock = list(reversed(block))

        p = 0
        dec = 0
        for f in fixedblock:
            dec += (3 ** p)*int(f)
            p += 1

        result.append(dec)
        block.clear()
        fixedblock.clear()

        return result[0]

    def DecodeToChar(self, In):
        return chr(self.DecodeToDec(In))
    
    def DecodeToHex(self, In):
        intermediate = str(hex(self.DecodeToDec(In)))
        return intermediate[2:]
    
    def DecodeToString(self, In):

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

    # One of the two primary Marionette functions, it performs string-wide encoding from unicode to dollcode
    def encode(self, In):
        #clear the output to make sure stuff doesn't get mixed up
        self.output.clear()

        #Decimal Encode
        if self.eMode == "d":
            return self.DecToDollcode(In)
        
        #Hex Encode
        elif self.eMode == "h":
            return self.HexToDollcode(In)

        #Char Encode
        elif self.eMode == "c":
            return self.CharToDollcode(In)
        
        #String Encode
        else:
            for o in list(In):
                self.output.append(self.CharToDollcode(o))
                self.output.append(" ")

            return "".join(self.output)

    # The second primary Marionette function, it performs decoding from dollcode to unicode
    def decode(self, In):

        if self.dMode == "d":
            return self.DecodeToDec(In)
        
        elif self.dMode == "c":
            return self.DecodeToChar(In)
        
        elif self.dMode == "h":
            return self.DecodeToHex(In)
        
        else:
            return self.DecodeToString(In)
        