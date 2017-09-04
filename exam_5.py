#! /usr/bin/env python
# -*- coding:utf-8 -*-

import itertools
from exam_2 import combine_alternately

if __name__ == '__main__' :

    target_result = 100
    operations = ['+', '-', '']
    
    for operator_string in itertools.product(operations, repeat=8) :
        
        num_list = ['{0}'.format(i+1) for i in range(9)]
        formula = ''.join(combine_alternately(num_list, operator_string))
        
        if eval(formula) == target_result :
            print '{0}={1}'.format(formula, target_result)
