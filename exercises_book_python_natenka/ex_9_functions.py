#!/usr/bin/env python3

def summ(a,b,c='Сумма: '):
    '''
    This funtion summarize two integers, then two strings.
    Return a tuple with (a+b,str(a)+str(b))
    '''
    return c, a+b, str(a)+str(b)

print(summ(1,2))
print(summ(b=1,a=2))
print(summ(1,2,c='Theese are digits'))

def summ_unlimit(*args):
    return len(args)

print(summ_unlimit(1,2,3,4,5,6,7,8,9,10))

def summ_kw(**kwargs):
    return len(kwargs)

print(summ_kw(a1=1,a2=2,a3=3))