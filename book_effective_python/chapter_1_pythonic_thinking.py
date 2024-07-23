from util.strings import to_str, to_bytes
from util.iterators import NextValueIterator


print("<<<<< Demonstrates the difference between bytes and str in Python. >>>>>")

def bytes_vs_str():
    """Demonstrates the difference between bytes and str in Python."""
    a = b'h\x65llo'
    print(list(a))
    print(a)
    print(a.decode('utf-8'))
    print(list(a.decode('utf-8')))
    print("".join(a.decode('utf-8')))
    print("--------------------------------------------------")
    p = 'pýtĥöñ'
    print(list(p))
    print(p)
    b = p.encode('utf-8')
    print(list(b))
    print("---------------------------------------------")
    print(repr(to_str(b'hello')))
    print(repr(to_bytes('hello')))
    print("---------------------------------------------")

print("<<<<< Prefer interpolated f-strings over the older str.format() method. >>>>>")

def format_strings():
    """Demonstrates the difference between f-strings and str.format()."""
    a = 0b10111011
    b = 0xc5f
    print('Binary is %d, hex is %d' % (a, b))
    print('Binary is {0}, hex is {1}'.format(a, b))
    print(f'Binary is {a}, hex is {b}')
    print("---------------------------------------------")
    key = 'my_var'
    value = 1.234
    formatted = '%-10s = %.2f' % (key, value)
    print(formatted)
    print("---------------------------------------------")
    menu = {
        'soup': 'lentil',
        'oyster': 'kumamoto',
        'special': 'schnitzel',
    }
    for name, contents in menu.items():
        print(f'{name:10} => {contents:10}')

    template = ('Today\'s soup is %(soup)s, '
                'buy one get two %(oyster)s oysters, '
                'and our special entrée is %(special)s.')
    formatted = template % menu
    print(formatted)
    print("---------------------------------------------")
    key = 'my_var'
    value = 1.234
    formatted = "{:<10} = {:.2f}".format(key, value)
    print(formatted)
    print("---------------------------------------------")

def interpolated_f_strings():
    """Demonstrates the difference between f-strings and str.format()."""
    key = 'my_var'
    value = 1.234
    f_string = f'{key:<10} = {value:.2f}'
    c_tuple = '%-10s = %.2f' % (key, value)
    str_args = '{:<10} = {:.2f}'.format(key, value)
    str_kw = '{key:<10} = {value:.2f}'.format(key=key,
                                              value=value)
    c_dict = '%(key)-10s = %(value).2f' % {'key': key,
                                           'value': value}
    assert c_tuple == c_dict == f_string
    assert str_args == str_kw == f_string

def unpacking_assignments():
    """Demon"""
    snack_calroies = {
        'chips': 140,
        'popcorn': 80,
        'nuts': 190,
    }
    items = tuple(snack_calroies.items())
    print(items)
    print("---------------------------------------------")

def enumerate_over_range():
    """
    ✦ enumerate provides concise syntax for looping over an iterator and getting the index of each item from the iterator as you go.
    ✦ Prefer enumerate instead of looping over a range and indexing into a sequence.
    ✦ You can supply a second parameter to enumerate to specify the number from which to begin counting (zero is the default).
    """
    from random import randint
    random_bits = 0
    for i in range(64):
        if randint(0, 1):
            random_bits |= 1 << i
    print(bin(random_bits))
    print("---------------------------------------------")
    flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
    for i, flavor in enumerate(flavor_list):
        print(f'{i + 1}: {flavor}')
    print("---------------------------------------------")
    for i, flavor in enumerate(flavor_list, 1):
        print(f'{i}: {flavor}')
    print("---------------------------------------------")
    flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
    it = iter(flavor_list)
    print(it)
    print(next(it))
    print(next(it))
    print("---------------------------------------------")


def zip_to_process_iterators():
    """
    Item 8: Use zip to Process Iterators in Parallel
    ✦ The zip built-in function can be used to iterate over multiple itera- tors in parallel.
    ✦ zip creates a lazy generator that produces tuples, so it can be used on infinitely long inputs.
    ✦ zip truncates its output silently to the shortest iterator if you supply it with iterators of different lengths.
    ✦ Use the zip_longest function from the itertools built-in mod- ule if you want to use zip on iterators of unequal lengths without truncation.
    """
    names = ['Cecilia', 'Lise', 'Marie']
    counts = [len(n) for n in names]
    for name, count in zip(names, counts):
        print(name)
        print(count)
    print("---------------------------------------------")
    from itertools import zip_longest
    names.append('Rosalind')
    for name, count in zip_longest(names, counts):
        print(f'{name}: {count}')
    print("---------------------------------------------")

def else_blocks_after_loops():
    """
    Item 9: Avoid else Blocks After for and while Loops
    ✦ Python has special syntax that allows else blocks to immediately follow for and while loop interior blocks.
    ✦ The else block after a loop only runs if the loop body did not encounter a break statement.
    ✦ Avoid using else blocks after loops because their behavior isn’t intuitive and can be confusing.
    """
    # block runs immediately after the loop finishes
    for i in range(3):
        print('Loop', i)
    else:
        print('Else block!')
    print("---------------------------------------------")
    # Using a break statement in a loop actually skips the else block:
    for i in range(3):
        print('Loop', i)
        if i == 1:
            break
    else:
        print('Else block!')
    print("---------------------------------------------")
    # The else block runs when the loop is skipped entirely:
    for x in []:
        print('Never runs')
    else:
        print('For Else block!')
    print("---------------------------------------------")
    # The else block runs when the while loop condition becomes false:
    while False:
        print('Never runs')
    else:
        print('While Else block!')

    print("---------------------------------------------")
    a = 4
    b = 9
    for i in range(2, min(a, b) + 1):
        print('Testing', i)
        if a % i == 0 and b % i == 0:
            print('Not coprime')
        break
    else:
        print('Coprime')

    def coprime(a, b):
        for i in range(2, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                return False
        return True

    assert coprime(4, 9)
    assert not coprime(3, 6)

    def coprime_alternate(a, b):
        is_coprime = True
        for i in range(2, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                is_coprime = False
                break
        return is_coprime

    assert coprime_alternate(4,9)
    assert not coprime_alternate(3, 6)
    print("---------------------------------------------")

def assignment_expressions():
    """
    Item 10: Prevent Repetition with Assignment Expressions
    ✦ Assignment expressions allow you to assign values to variables as part of a larger expression.
    ✦ Assignment expressions use the new walrus operator (:=) to merge assignment and comparison expressions.
    ✦ Assignment expressions help you avoid duplicating computations in your code.
    ✦ When assignment expression is a subexpression of a larger expression, you can avoid introducing a new variable in the surrounding scope.
    ✦ Although switch/case statements and do/while loops are not present in Python, assignment expressions can be used to achieve similar results.
    """

    def make_lemonade(count):
        print(f'Making {count} lemonade')
        return count

    def out_of_stock():
        print('Out of stock!')
        return 0

    fresh_fruit = {
        'apple': 10,
        'banana': 8,
        'lemon': 5,
    }

    # without walrus operator
    count = fresh_fruit.get('lemon', 0)
    if count:
        make_lemonade(count)
    else:
        out_of_stock()

    # with walrus operator
    if count:= fresh_fruit.get('lemon', 0):
        make_lemonade(count)

    def make_cider(count):
        ...

    # without walrus operator
    count = fresh_fruit.get('apple', 0)
    if count >= 4:
        make_cider(count)
    else:
        out_of_stock()

    # with walrus operator
    if (count := fresh_fruit.get('apple', 0)) >= 4:
        make_cider(count)
    else:
        out_of_stock()

    def slice_bananas(count):
        print(f'Slicing {count} bananas')
        return count

    def make_smoothies(count):
        print(f'Making {count} smoothies')
        return count

    class OutOfBananas(Exception):
        pass

    # without walrus operator
    # 1
    pieces = fresh_fruit.get('banana', 0)
    if pieces >= 2:
        banana_slice = slice_bananas(pieces)
        to_enjoy = make_smoothies(banana_slice)
    else:
        pieces = 0
        to_enjoy = out_of_stock()
    # 2
    pieces = 0
    count = fresh_fruit.get('banana', 0)
    if count >= 2:
        pieces = slice_bananas(count)
    try:
        smoothies = make_smoothies(pieces)
    except OutOfBananas:
        out_of_stock()

    # with walrus operator
    if (count := fresh_fruit.get('banana', 0)) >= 2:
        pieces = slice_bananas(count)
    else:
        pieces = 0

    try:
        smoothies = make_smoothies(pieces)
    except OutOfBananas:
        out_of_stock()

    print("---------------------------------------------")
    print("switch/case statement emulation with walrus operator")

    # switch/case imitation without walrus operator
    count = fresh_fruit.get('banana', 0)
    if count >= 2:
        pieces = slice_bananas(count)
        to_enjoy = make_smoothies(pieces)
    else:
        count = fresh_fruit.get('apple', 0)
        if count >= 4:
            to_enjoy = make_cider(count)
        else:
            count = fresh_fruit.get('lemon', 0)
            if count:
                to_enjoy = make_lemonade(count)
            else:
                to_enjoy = 'Nothing'

    # with walrus operator
    if (count := fresh_fruit.get('banana', 0) >= 2):
        pieces = slice_bananas(count)
        to_enjoy = make_smoothies(pieces)
    elif (count := fresh_fruit.get('apple', 0) >= 4):
        to_enjoy = make_cider(count)
    elif count := fresh_fruit.get('lemon', 0):
        to_enjoy = make_lemonade(count)
    else:
        to_enjoy = 'Nothing'

    print("---------------------------------------------")
    print("do/while loop construct emulation with walrus operator")

    def pick_fruit(fruit_iter: NextValueIterator):
        try:
            return fruit_iter.next_value()
        except StopIteration:
            return None

    def make_juice(fruit, count):
        print(f'Making {count} {fruit} juice')
        return [fruit] * count

    # without walrus operator
    print("-- without walrus operator")

    bottles = []
    fruit_iter = NextValueIterator(fresh_fruit.items())
    picked_fruit = pick_fruit(fruit_iter)
    while picked_fruit:
        batch = make_juice(*picked_fruit)
        bottles.extend(batch)
        picked_fruit = pick_fruit(fruit_iter)

    print("-----------------------")

    # oop-and-a-half idiom
    print("-- oop-and-a-half idiom")

    bottles = []
    fruit_iter = NextValueIterator(fresh_fruit.items())
    while True:
        picked_fruit = pick_fruit(fruit_iter)
        if not picked_fruit:
            break
        batch = make_juice(*picked_fruit)
        bottles.extend(batch)

    print("-----------------------")

    # with walrus operator
    print("-- with walrus operator")

    bottles = []
    fruit_iter = NextValueIterator(fresh_fruit.items())
    while picked_fruit := pick_fruit(fruit_iter):
        batch = make_juice(*picked_fruit)
        bottles.extend(batch)

    print("---------------------------------------------")


def main():
    bytes_vs_str()
    format_strings()
    interpolated_f_strings()
    enumerate_over_range()
    zip_to_process_iterators()
    else_blocks_after_loops()
    assignment_expressions()

if __name__ == '__main__':
    main()
