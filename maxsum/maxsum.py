"""
Problem:

Maximum Sum
Given a list of numbers, write a program to select a subset of numbers whose sum is maximum while not picking any neighbors together

Examples: 
[1, 2, 3, 4] - Selected subset: {2, 4} 
[4, 1, 2] - Selected subset: {4, 2} 
[4, 15, 2] - Selected subset: {15}

"""

import operator


def find_max(input_list):
    try:
        index, value = max(enumerate(input_list), key=operator.itemgetter(1))
        return index, value
    except ValueError:
        return '', ''

def get_input():
    '''
    Enter input numbers with space as delimiter
    '''
    input_str = raw_input("Enter interger with space as delimiter: ")
    try:
        input_list = [int(i) for i in input_str.split()]
        return input_list
    except ValueError:
        print "Enter ONLY integers"
        return 

def find_max_sum(input_list):
    if input_list:
        fst_max_index, fst_max_val = find_max(input_list)
        
        # skipping the neighbors of first maximum
        input_list[fst_max_index] = 0
        input_list[fst_max_index-1] = 0
        try:
            input_list[fst_max_index+1] = 0
        except IndexError:
            pass

        sec_max_idx, sec_max_val = find_max(input_list)
        
        if not sec_max_val:
            return [fst_max_val]

        # return subset
        if fst_max_index > sec_max_idx:
            return [sec_max_val, fst_max_val]
        else:
            return [fst_max_val, sec_max_val]


if __name__ == '__main__':
    input_list = get_input()
    print find_max_sum(input_list)
