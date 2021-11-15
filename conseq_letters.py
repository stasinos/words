#!/bin/python3

import sys
import unicodedata

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def next_letter(c):
    if chr(c) == "ρ": return ord("σ")
    if chr(c) == "ω": return None
    return( c+1 )

# Checks if A contains B,
def has_subarray(A, B):
    n=len(A)
    m=len(B)
    # Two pointers to traverse the arrays
    i = 0; j = 0;
    # Traverse both arrays simultaneously
    while (i < n and j < m):
        # If element matches
        # increment both pointers
        if (A[i] == B[j]):
            i += 1;
            j += 1;
            # If array B is completely
            # traversed
            if (j == m):
                return True;
        # If not,
        # increment i and reset j
        else:
            i = i - j + 1;
            j = 0;
    return False;

fragments = []

for c in range(945,967):
    if chr(c) != "ς":
        substr4 = [chr(c)]
        cc = c
        for i in range(3):
            cc = next_letter( cc )
            substr4.append( chr(cc) )
        fragments.append(substr4)

for c in range(945,966):
    if chr(c) != "ς":
        substr5 = [chr(c)]
        cc = c
        for i in range(4):
            cc = next_letter( cc )
            substr5.append( chr(cc) )
        fragments.append(substr5)

for line in sys.stdin:
    normalized_string = strip_accents( line.strip().lower() )
    normalized_array = list( normalized_string )
    for fragment in fragments:
        if has_subarray( normalized_array, fragment ):
            print( line.strip() )
