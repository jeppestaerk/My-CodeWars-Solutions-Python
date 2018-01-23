from kata.Test import test


def disemvowel(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    for v in vowels:
        string = string.replace(v, '')
        string = string.replace(v.lower(), '')
    return string


test.assert_equals(disemvowel('This website is for losers LOL!'), 'Ths wbst s fr lsrs LL!')
