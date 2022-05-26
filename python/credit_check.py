from functools import total_ordering
import functools


def credit_check(account_num):
    dig_list= [int(a) for a in str(account_num)]
    for i, x in enumerate(dig_list):
        if(i % 2 == 0):
            mult_dig= x*2
            if(mult_dig>=10):
                total=0
                for b in str(mult_dig):
                    total+=int(b)
                dig_list[i] = total
            else:
                dig_list[i]=mult_dig                    
    checker = functools.reduce(lambda agg, item:agg+item,dig_list)
    if checker % 10 == 0:
        return "The number is valid!"
    else:
        return "The number is invalid!"


