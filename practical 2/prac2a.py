def is_vowel(s):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for i in s:
        if i in vowels:
            print("True")
        else:
            print("False")
            
ustr = input()
is_vowel(ustr)