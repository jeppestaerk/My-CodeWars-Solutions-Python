from kata.Test import test


def is_isogram(string):
    word = string.lower()
    return True if word and len(set(word)) == len(word) or len(word) == 0 else False


test.assert_equals(is_isogram("Dermatoglyphics"), True)
test.assert_equals(is_isogram("isogram"), True)
test.assert_equals(is_isogram("aba"), False, "same chars may not be adjacent")
test.assert_equals(is_isogram("moOse"), False, "same chars may not be same case")
test.assert_equals(is_isogram("isIsogram"), False)
test.assert_equals(is_isogram(""), True, "an empty string is a valid isogram")