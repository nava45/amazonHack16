"""
Problem:

Maximum Sum
Given a list of numbers, write a program to select a subset of numbers whose sum is maximum while not picking any neighbors together

Examples: 
[1, 2, 3, 4] - Selected subset: {2, 4} 
[4, 1, 2] - Selected subset: {4, 2} 
[4, 15, 2] - Selected subset: {15}

"""

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
        odd_subset = [i for i in input_list[0::2] if i > 0]
        event_subset = [i for i in input_list[1::2] if i > 0]
        if sum(odd_subset) > sum(event_subset):
            return odd_subset
        return event_subset

if __name__ == '__main__':
    input_list = get_input()
    print find_max_sum(input_list)
