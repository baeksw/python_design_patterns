import pytest 
from itertools import permutations

def test_permutations():
    '''
    순열 
    '''
    expected = [('a', 'b', 'c')
            , ('a', 'c', 'b')
            , ('b', 'a', 'c')
            , ('b', 'c', 'a')
            , ('c', 'a', 'b')
            , ('c', 'b', 'a')]
    actual = list(permutations('abc'))
    
    assert expected == actual




