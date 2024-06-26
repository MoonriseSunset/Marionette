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
