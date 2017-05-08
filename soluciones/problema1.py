# -*- coding: utf-8 -*-
import sys
must_satisfy = []
cards_values = []

def get_input():
    global must_satisfy, cards_values
    k = int(raw_input("Valor de k: "))
    must_satisfy  = [x for x in range(1, k+1)]
    max_cards = sum(must_satisfy)
    print "--> Debe cumplir: %s" % must_satisfy
    cards_values = []
    if  k <= 20:
        m = raw_input("Numero de montones: ")
        for x in range(1, int(m)+1):
            cards_values.append(int(raw_input("Cantidad monton #%s: " % x)))

        if not max_cards == sum(cards_values):
            print "El numero de cartas debe ser igual al mazo (k)"
            sys.exit()
    else:
        print "El valor de k ser menor a 20"

def sustract_one_card(c):
    """Toma una carta de cada monton"""
    for x in range (0, len(c)):
        c[x] = c[x] - 1

def add_n_deck_cards(c):
    """Agrega un nuevo 'monton' de cartas al final con el valor del tam;o del la lista"""
    c.append(len(c))

def check_zeros(c):
    """Busca y elimina los ceros"""
    for x in range(0, len(c)-1):
        try:
            if c[x] == 0:
                c.remove(0)
        except IndexError:
            sys.exit()


def magic_solitaire(cv, ms):
    while cv != ms:
        sustract_one_card(cv)
        add_n_deck_cards(cv)
        check_zeros(cv)
        print cv

def run():
    print ":::::SOLITARIO MÁGICO::::::"
    print "-----DATOS DE ENTRADA------"
    get_input()
    print "-----DATOS DE SALIDA-------"
    print cards_values
    magic_solitaire(cards_values, must_satisfy)

run()