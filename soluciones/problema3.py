# -*- coding: utf-8 -*-
import sys
p = []

def get_input():
    global p
    allowed = set("()[]{}")
    p = raw_input("Cadena de caracteres ()[]{}: ")

    if len(p) >= 128:
        print "Solo se permiten 128 caracteres!"
        sys.exit()

    if not set(p) <= allowed:
        print "Solo se permiten ()[]{} !"
        sys.exit()


def is_balanced(p0):
    c1 = p0.count('(')
    c2 = p0.count(')')
    c3 = p0.count('[')
    c4 = p0.count(']')
    c5 = p0.count('{')
    c6 = p0.count('}')

    if  c1 == c2 and c3 == c4 and c5 == c6:
        return True
    else:
        return False

def run():
    print ":::::BALANCE DE PARÉNTESIS::::::"
    print "-----DATOS DE ENTRADA------"
    get_input()
    if is_balanced(p):
        print "BALANCEADO"
    else:
        print "NO BALANCEADO"

run()