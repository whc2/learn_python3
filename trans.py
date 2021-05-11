#!/usr/bin/env python3

import os

base_for = "ACGT"
base_rev = "TGCA"
comp_tab = str.maketrans(base_for, base_rev)

print(comp_tab)	# {65: 84, 67: 71, 71: 67, 84: 65}

# another
dict = {"a": "123", "b": "456", "c": "789"}
string = "abc"
print(string.maketrans(dict))

# another
intab = "aeiou"
outtab = "12345"
transtab = str.maketrans(intab, outtab)
print(transtab)

str = "this is string example ... wow!!!"
print (str.translate(transtab))
