# -*- coding: utf-8 -*-

def is_pangram(inp):
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    inp = list(inp.lower())
    for a in alpha:
        if a not in inp:
            return False
            break

    return True
        
