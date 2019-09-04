#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:52:24 2019

@author: pengbo
"""

def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket(90, False)
    False
    >>> wears_jacket(40, False)
    True
    >>> wears_jacket(100, True)
    True
    """
    if temp < 60 or raining:
        return True
    return False

def wears_jacket(temp, raining):
    return temp < 60 or raining

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    def divisible(numerator, denominator):
        if numerator == denominator:
            return True
        elif numerator % denominator == 0:
            return False
        return divisible(numerator, denominator+1)
    
    return divisible(n, 2)