'''
Module that has functions and attributes that will help and optimize the password generation.
'''
lower_case_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upper_case_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!","@","$","%","&","/","(", ")", "=", "?", "¿", "Ç", "*", "+", "}", "[", "-", "_", ".", ":", ",", ";"]

def get_element(id_dataset, id_item):
    '''
    Returns an element of a given dataset.
    '''
    if id_dataset == 0:
        return lower_case_letters[id_item]
    elif id_dataset == 1:
        return upper_case_letters[id_item]
    elif id_dataset == 2:
        return numbers[id_item]
    elif id_dataset == 3:
        return symbols[id_item]
    else:
        return "-1"

def get_sizes(id_dataset):
    '''
    Returns the size of a given dataset.
    '''
    if id_dataset == 0:
        return len(lower_case_letters)
    elif id_dataset == 1:
        return len(upper_case_letters)
    elif id_dataset == 2:
        return len(numbers)
    elif id_dataset == 3:
        return len(symbols)
    else:
        return -1
