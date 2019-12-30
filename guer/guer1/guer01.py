def paths(m, n):
    """
    >>> paths(2, 2)
    2
    >>> paths(117, 1)
    1
    """

    if m == 1 or n == 1:
        return 1
    return paths(m-1, n) + paths(m, n-1)


def merge(s1, s2):
    """ Merges two sorted lists
    >>> merge([1, 3], [2, 4])
    [1, 2, 3, 4]
    >>> merge([1, 2], [])
    [1, 2]
    """

    if s1 == []:
        return s2
    elif s2 == []:
        return s1
    
    if s1[0] < s2[0]:
        return [s1[0]] + merge(s1[1:], s2)
    else:
        return [s2[0]] + merge(s1, s2[1:])


def mario_number(level):
    """Return the number of ways that Mario can perform a sequence of steps
    or jumps to reach the end of the level without ever landing in a Piranha
    plant. Assume that every level begins and ends with a dash.
    >>> mario_number('-P-P-') # jump, jump
    1
    >>> mario_number('-P-P--') # jump, jump, step
    1
    >>> mario_number('--P-P-') # step, jump, jump
    1
    >>> mario_number('---P-P-') # step, step, jump, jump or jump, jump, jump
    2
    >>> mario_number('-P-PP-') # Mario cannot jump two plants
    0
    >>> mario_number('----') # step, jump ; jump, step ; step, step, step
    3
    >>> mario_number('----P----')
    9
    >>> mario_number('---P----P-P---P--P-P----P-----P-')
    180
    """

    
    if level == '-P-' or level == '-':
        return 1
    elif len(level) == 0 or level[0] == 'P':
        return 0
    else:
        return mario_number(level[1:]) + mario_number(level[2:])
    