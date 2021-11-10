from random import randint

#FIXME: I am working on how to get python to write ^superscripts
#nested dictionary where 'key'= ion charge,
#value = nested list[ion charge superscript, ['symbol, 'element', 'name change'], [...]]
ion_dic = {-1: ['\u207B',
                ['F', 'fluorine', 'fluorine'],
                ['Cl', 'chlorine', 'chloride'],
                ['Br', 'bromine', 'bromide'],
                ['I', 'iodine', 'iodide'],
                ['At', 'astatine', 'astatine']],

           -2: ['\u00b2\u207B',
                ['O', 'oxygen', 'oxide'],
                ['S', 'sulfur', 'sulfide'],
                ['Se', 'selenium', 'selenide'],
                ['Te', 'tellurium', 'telluride'],
                ['Po', 'polonium', 'polonide']],

           -3: ['\u00b3\u207A',
                ['N', 'nitrogen', 'nitride'],
                ['P', 'phosphorus', 'phosphide'],
                ['As', 'arsenic', 'arsenide'],
                ['Sb', 'antimony', 'antimide'],
                ['Bi', 'bismuth', 'bismide']],

           3: ['\u00b3\u207A',
               ['B', 'boron'],
               ['Al', 'aluminium'],
               ['Ga', 'gallium'],
               ['In', 'indium'],
               ['Tl', 'thallium']],

           2: ['\u00b2\u207A',
               ['Be', 'beryllium'],
               ['Mg',  'magnesium'],
               ['Ca',  'hydrogen'],
               ['Sr',  'strontium'],
               ['Cs',  'cesium']],

           1: ['\u207A',
               ['Na', 'sodium'],
               ['K', 'potassium'],
               ['H', 'hydrogen'],
               ['Rb' 'rubidium'],
               ['Cs', 'cesium'],
               ['Li', 'lithium']]}

starting_pos_lst = []

def generate_starting_pos():
    for x in range(50, 920, 100):
        for y in range(50, 600, 100):
            random_xshift = randint(0,15)
            random_yshift = randint(0, 20)
            if random_xshift % 2:
                pos_x = x + random_xshift
            else:
                pos_x = x - random_xshift
            if random_yshift % 2:
                pos_y = y + random_yshift
            else:
                pos_y = y - random_yshift
            starting_pos_lst.append((pos_x, pos_y))
    print(starting_pos_lst)



def rand_ion(charge):
    group_len = len(ion_dic[charge])
    print(group_len)
    rand_ion = ion_dic[charge][randint(1, group_len-1)][0]+ion_dic[charge][0]

    return rand_ion

#def name_compound(cation, anion):
    #name =


#cation1_list = ['Na \n{}'.format(SUPERSCRIPT PLUS), 'K \n{}'.format(SUPERSCRIPT PLUS), 'H \n{}'.format(SUPERSCRIPT PLUS), 'Rb \n{}'.format(SUPERSCRIPT PLUS), 'Cs \n{}'.format(SUPERSCRIPT PLUS)]]
"""
#retired dictionaries
anion1_dict = {
    'F' :[-1, '\u207B', 'fluorine', 'fluorine'],
    'Cl':[-1, '\u207B', 'chlorine', 'chloride'],
    'Br':[-1, '\u207B', 'bromine', 'bromide'],
    'I' :[-1, '\u207B', 'iodine', 'iodide'],
    'At':[-1, '\u207B', 'astatine', 'astine']}

anion3_dict = {
    'N' :[-3, '\u00b3\u207B', 'nitrogen', 'nitride'],
    'P' :[-3, '\u00b3\u207B', 'phosphorus', 'phosphide'],
    'As':[-3, '\u00b3\u207B', 'arsenic', 'arsenide'],
    'Sb':[-3, '\u00b3\u207B', 'antimony', 'antimide'],
    'Bi':[-3, '\u00b3\u207B', 'bismuth', 'bismide']}

cation3_dict = {
    'B' :[3, '\u00b3\u207A', 'boron'],
    'Al':[3, '\u00b3\u207A', 'aluminium'],
    'Ga':[3, '\u00b3\u207A', 'gallium'],
    'In':[3, '\u00b3\u207A', 'indium'],
    'Tl':[3, '\u00b3\u207A', 'thallium']}
    
cation2_dict = {
    'Be':[2, '\u00b2\u207A', 'beryllium'],
    'Mg':[2, '\u00b2\u207A', 'magnesium'],
    'Ca':[2, '\u00b2\u207A', 'hydrogen'],
    'Sr':[2, '\u00b2\u207A', 'strontium'],
    'Cs':[2, '\u00b2\u207A', 'cesium']}

cation1_dict = {
    'Na':[1, '\u207A', 'sodium'],
    'K' :[1, '\u207A', 'potassium'],
    'H' :[1, '\u207A', 'hydrogen'],
    'Rb':[1, '\u207A', 'rubidium'],
    'Cs':[1, '\u207A', 'cesium'],
    'Li':[1, '\u207A', 'lithium']}
    
#retired ion lists:
cation1_list = ['Na\u207A', 'K\u207a', 'H\u207a', 'Rb\u207a', 'Cs\u207a', 'Li\u207a']

cation2_list = ['Be\u00b2\u207A', 'Mg\u00b2\u207A', 'Ca\u00b2\u207A', 'Sr\u00b2\u207A', 'Ba\u00b2\u207A']

cation3_list = ['B\u00b3\u207A', 'Al\u00b3\u207A', 'Ga\u00b3\u207A', 'In\u00b3\u207A', 'Tl\u00b3\u207A']

anion1_list = ['F\u207B', 'Cl\u207B', 'Br\u207B', 'I\u207B', 'At\u207B']

anion2_list = ['O\u00b2\u207B', 'S\u00b2\u207B', 'Se\u00b2\u207B', 'Te\u00b2\u207B', 'Po\u00b2\u207B']

anion3_list = ['N\u00b3\u207B', 'P\u00b3\u207B', 'As\u00b3\u207B', 'Sb\u00b3\u207B', 'Bi\u00b3\u207B']

    """

