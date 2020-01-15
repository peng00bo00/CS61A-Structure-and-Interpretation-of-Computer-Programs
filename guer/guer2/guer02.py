# Q1.3
def map_mut(f, L):
    """
    >>> L = [1, 2, 3, 4]
    >>> map_mut(lambda x: x**2, L)
    >>> L
    [1, 4, 9, 16]
    """
    for i in range(len(L)):
        L[i] = f(L[i])

# Q4.1
def tree(label, branches = []):
    for b in branches:
        assert is_tree(b), 'branches must be trees'
    return [label] + list(branches)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for b in branches(tree):
        if not is_tree(b):
            return False
    return True

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

# Q4.2
def is_min_heap(t):
    for b in branches(t):
        if label(t) > label(b) or not is_min_heap(b):
            return False
    return True

# Q4.3
def largest_product_path(tree):
    """
    >>> largest_product_path(None)
    0
    >>> largest_product_path(tree(3))
    3
    >>> t = tree(3, [tree(7, [tree(2)]), tree(8, [tree(1)]), tree(4)])
    >>> largest_product_path(t)
    42
    """

    if not is_tree(tree):
        return 0
    elif is_leaf(tree):
        return label(tree)
    else:
        p = [tree.label * largest_product_path(b) for b in branches(tree)]
        return max(p)

# Q4.4.3
def contains(t, e):
    if is_leaf(t):
        return e == label(t)
    elif e == label(t):
        return True
    else:
        for b in branches(t):
            if contains(b, e):
                return True
        return False

# Q4.4.4
def max_tree(t):
    """
    >>> max_tree(tree(1, [tree(5, [tree(7)]),tree(3,[tree(9),tree(4)]),tree(6)]))
    tree(9, [tree(7, [tree(7)]),tree(9,[tree(9),tree(4)]),tree(6)])
    """
    if is_leaf(t):
        return t
    else:
        new_branches= [max_tree(b) for b in branches(t)]
        new_label = max([label(t)] + [label(b) for b in new_branches])
        return tree(new_label, new_branches)

# Q4.5
def level_order(tree):
    def helper(trees, labels):
        if len(trees) == 0:
            return labels
        t = trees[0]
        return helper(trees[1:]+branches(t), labels+[label(t)])
    
    return helper([tree], [])

# Q4.6
def all_paths(tree):
    def helper(t, path, paths):
        if is_leaf(t):
            paths.append(path + [label(t)])
            return paths
        for b in branches(t):
            paths = helper(b, path + [label(t)], paths)
        return paths
    
    return helper(tree, [], [])

def all_paths(t):
    if is_leaf(t):
        return [[label(t)]]
    else:
        total = []
        for b in branches(t):
            for path in all_paths(b):
                total.append([label(t)] + path)
        return total

# Q5.3
def make_max_finder():
    """
    >>> m = make_max_finder()
    >>> m([5, 6, 7])
    7
    >>> m([1, 2, 3])
    7
    >>> m([9])
    9
    >>> m2 = make_max_finder()
    >>> m2([1])
    1
    """

    m = None
    def helper(lst):
        nonlocal m
        if m is None:
            m = max(lst)
            return m
        else:
            m = max(m, max(lst))
            return m
    
    return helper

# Q5.6
class Cat():
    noise = 'meow'

    def __init__(self, name):
        self.name = name
        self.hungry = True

    def meow(self):
        if self.hungry:
            print(f"Meow, {self.name} is hungry")
        else:
            print(f"Meow, my name is {self.name}")

    def eat(self):
        print(self.noise)
        self.hungry = False


class Kitten(Cat):
    noise = "i'm baby"
    def __init__(self, name, mama):
        Cat.__init__(self, name)
        self.mama = mama
    
    def meow(self):
        Cat.meow(self)
        print(f"I want mama {self.mama.name}")


# Q7.1
def filter_tree(t, fn):
    """
    >>> t = Tree(1, [Tree(2), Tree(3, [Tree(4)]), Tree(6, [Tree(7)])])
    >>> filter_tree(t, lambda x: x % 2 != 0)
    >>> t
    tree(1, [Tree(3)])
    >>> t2 = Tree(2, [Tree(3), Tree(4), Tree(5)])
    >>> filter_tree(t2, lambda x: x != 2)
    >>> t2
    Tree(2)
    """

    if not fn(t.label):
        t.branches = []
    else:
        for b in t.branches[:]:
            if not fn(b.label):
                t.branches.remove(b)
            else:
                filter_tree(b, fn)

# Q7.2
def nth_level_tree_map(fn, tree, n):
    """Mutates a tree by mapping a function all the elements of a tree.
    >>> tree = Tree(1, [Tree(7, [Tree(3), Tree(4), Tree(5)]),
                Tree(2, [Tree(6), Tree(4)])])
    >>> nth_level_tree_map(lambda x: x + 1, tree, 2)
    >>> tree
    Tree(2, [Tree(7, [Tree(4), Tree(5), Tree(6)]),
             Tree(2, [Tree(7), Tree(5)])])
    """

    def helper(t, level):
        if level % n == 0:
            t.label = fn(t.label)
        for b in t.branches:
            helper(b, level+1)
    
    helper(tree, 0)

# Q8.3
def has_cycle(link):
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    """

    links = []
    while link.rest:
        if link in links:
            return True
        links.append(link)
        link = link.rest
    return False

# Q8.4
def seq_in_link(link, sub_link):
    """
    >>> lnk1 = Link(1, Link(2, Link(3, Link(4))))
    >>> lnk2 = Link(1, Link(3))
    >>> lnk3 = Link(4, Link(3, Link(2, Link(1))))
    >>> seq_in_link(lnk1, lnk2)
    True
    >>> seq_in_link(lnk1, lnk3)
    False
    """

    if sub_link is Link.empty:
        return True
    elif link is Link.empty:
        return False
    else:
        if link.first == sub_link.first:
            return seq_in_link(link.rest, sub_link.rest)
        else:
            return seq_in_link(link.rest, sub_link)

# Q9.4
def generate_constant(x):
    """A generator function that repeats the same value x forever.
    >>> area = generate_constant(51)
    >>> next(area)
    51
    >>> next(area)
    51
    >>> sum([next(area) for _ in range(100)])
    5100
    """
    while True:
        yield x

# Q9.5
def black_hole(seq, trap):
    """A generator that yields items in SEQ until one of them matches TRAP, in which case that
    value should be repeatedly yielded forever.
    >>> trapped = black_hole([1, 2, 3], 2)
    >>> [next(trapped) for _ in range(6)]
    [1, 2, 2, 2, 2, 2]
    >>> list(black_hole(range(5), 7))
    [0, 1, 2, 3, 4]
    """
    for e in seq:
        if e == trap:
            yield from generate_constant(trap)
        else:
            yield e

# Q9.7
def gen_inf(lst):
    while True:
        yield from lst

# Q9.8
def naturals():
    i = 1
    while True:
        yield i
        i += 1

def filter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter(range(5), is_even))
    [0 , 2 , 4]
    >>> all_odd = (2*y-1 for y in range (5))
    >>> list(filter(all_odd, is_even))
    []
    >>> s = filter(naturals(), is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """

    for e in iterable:
        if fn(e):
            yield e

# Q9.10
def tree_sequence(t):
    """
    >>> t = tree(1, [tree(2, [tree(5)]), tree(3, [tree(4)])])
    >>> print(list(tree_sequence(t)))
    [1, 2, 5, 3, 4]
    """

    yield t.label
    for b in branches(t):
        yield from tree_sequence(b)

# Q9.11
def make_digit_getter(n):
    """ Returns a function that returns the next digit in n
    each time it is called, and the total value of all the integers
    once all the digits have been returned.
    >>> year = 8102
    >>> get_year_digit = make_digit_getter(year)
    >>> for _ in range(4):
    ... print(get_year_digit())
    2
    0
    1
    8
    >>> get_year_digit()
    11
    """
    total = 0
    def get_next():
        nonlocal n, total
        if n == 0:
            return total
        val = n % 10
        n = n // 10
        total += val
        return val

    return get_next