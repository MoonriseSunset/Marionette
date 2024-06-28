# Marionette

## Background

Based on noe's [dollcode](https://noe.sh/dollcode/) standard, Marionette can translate ***any*** unicode character, or any string of unicode characters, into individual special-ternary dollcode characters or strings of special-ternary dollcode characters.

## How to use:

1. Clone the repo
2. Run ``playground.py``
3. Translate away through the terminal :)


## *LIMITATIONS:*

- **Cannot translate text files, only raw strings**

## TODO:
- [ ] Solve multi-layer encoding/decoding
- [ ] Text file I/O
- [ ] Finish main documentation


# Technical breakdown:

### ``playground.py``
---

``playground.py`` breaks out the functions from the core ``marionette.py`` into a terminal format. It's very simple, just a breakable infinite loop with ``if`` statements to trigger the different functions.

### ``marionette.py``
---

Originally, the project started with two separate python files one for encoding and one for decoding, however Moonrise consolidated the two into a single Class for ease of use. Check the WIP in-code comments for more info :) (*very WIP*)

# ⚠️ DISCLAIMER ⚠️
- Moonrise is in no way associated or otherwise connected with the Voidgoddess site, Ziz, or anyone else involved in the creation(?) and proliferation of dolls. This is purely a fun esoteric encryption project that dolls and any entity, human or not, is free to use however they like. For translating pure hex, *not* unicode characters, into dollcode, please refer to https://noe.sh/dollcode/. Thank you!

- Kabalabax, while learning and versing itself in the ways of the winding fractal and becoming the combat doll it wishes to see on the battlefield, has no relation whatsoever to things within the circle of the Voidgoddess site, Ra, anyone.
