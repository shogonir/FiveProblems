#! /usr/bin/env python
# -*- coding:utf-8 -*-

# use for roop
def calculate_sum_with_for (num_list) :
    list_sum = 0
    for num in num_list :
        list_sum += num
    return list_sum

# use while roop
def calculate_sum_with_while (num_list) :
    list_sum, i = 0, 0
    while i < len(num_list) :
        list_sum += num_list[i]
        i += 1
    return list_sum

# use recursive function
def calculate_sum_with_recurse (num_list, i = 0) :
    if i == len(num_list) - 1 :
        return num_list[i]
    else :
        return num_list[i] + calculate_sum_with_recurse(num_list, i+1)

if __name__ == '__main__' :
    
    num_list = range(10)

    print 'for     : {0}'.format(calculate_sum_with_for(num_list))
    print 'while   : {0}'.format(calculate_sum_with_while(num_list))
    print 'recurse : {0}'.format(calculate_sum_with_recurse(num_list))

