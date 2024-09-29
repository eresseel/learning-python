#!/usr/bin/env python
# -*- coding: utf-8 -*-

def kulso():
    szam = 20

    def belso():
        nonlocal szam
        szam += 1
        print(szam)
    
    return belso

f1 = kulso()
f1()