from random import randint

#FIXME: I am working on how to get python to write ^superscripts
#cation1_list = ['Na \n{}'.format(SUPERSCRIPT PLUS), 'K \n{}'.format(SUPERSCRIPT PLUS), 'H \n{}'.format(SUPERSCRIPT PLUS), 'Rb \n{}'.format(SUPERSCRIPT PLUS), 'Cs \n{}'.format(SUPERSCRIPT PLUS)]]

cation1_list = ['Na', 'K', 'H', 'Rb', 'Cs', 'Li']

cation2_list = ['Be', 'Mg', 'Ca', 'Sr', 'Ba']

cation3_list = ['B', 'Al', 'Ga', 'In', 'Tl']

anion1_list = ['F', 'Cl', 'Br', 'I', 'At']

anion2_list = ['O', 'S', 'Se', 'Te', 'Po']

anion3_list = ['N', 'P', 'As', 'Sb', 'Bi']

def rand_ion(charge):
    if charge == 1:
        lst = cation1_list

    if charge == 2:
        lst = cation2_list

    if charge == 3:
        lst = cation3_list

    if charge == -1:
        lst = anion1_list

    if charge == -2:
        lst =  anion2_list

    if charge == -3:
        lst = anion3_list

    rand_ion = lst[randint(0,len(lst)-1)]

    return rand_ion

