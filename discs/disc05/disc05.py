# Tree ADT
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


## Q1.1
def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """

    if is_leaf(t):
        return 0
    else:
        return 1 + max([height(branch) for branch in branches(t)])

## Q1.2
def square_tree(t):
    """Return a tree with the square of every element in t
    >>> numbers = tree(1,
    ...             [tree(2,
    ...                 [tree(3),
    ...                 tree(4)]),
    ...             tree(5,
    ...                 [tree(6,
    ...                     [tree(7)]),
    ...                 tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
        4
            9
            16
        25
            36
                49
            64
    """

    return tree(label(t)**2, [square_tree(branch) for branch in branches(t)])


## Q1.3
def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """

    if label(tree) == x:
        return [x]    
    for branch in branches(tree):
        path = find_path(branch, x)
        if path:
            return [label(tree)] + path


# Q2.2
def add_this_many(x, el, lst):
    """ Adds el to the end of lst the number of times x occurs
    in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """

    count = 0
    for e in lst:
        if e == x:
            count += 1
    
    for _ in range(count):
        lst.append(el)

## Q2.3
def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """

    keys = [fn(e) for e in s]
    dict = {key: [] for key in set(keys)}
    for key, value in zip(keys, s):
        dict[key].append(value)
    return dict

## Q3.2
def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """

    def f(func):
        nonlocal n
        n = func(n)
        return n
    
    return f
