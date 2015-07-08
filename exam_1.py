#! /usr/bin/env python
# -*- coding:utf-8 -*-

num_list = range(10)

# use for roop
list_sum = 0
for num in num_list :
    list_sum += num
print 'list_sum counted with for roop           :', list_sum

# use while roop
list_sum, i = 0, 0
while i < len(num_list) :
    list_sum += num_list[i]
    i += 1
print 'list_sum counted with while roop         :', list_sum

# use recursive function
def count_sum (num_list, i=0) :
    if i == len(num_list) - 1 :
        return num_list[i]
    else :
        return num_list[i] + count_sum(num_list, i+1)
print 'list_sum counted with recursive function :', count_sum(num_list)
