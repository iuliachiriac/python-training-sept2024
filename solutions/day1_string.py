# 1. Given the string s = "bandana":
s = 'bandana'
#     * check if string "and" is contained in s
print(f'"and" is contained in "{s}":', 'and' in s)
#     * find the index of the following strings.py: "n", "q"
print(f'Index of "n" in "{s}":', s.index('n'))
print(f'Index of "q" in "{s}" (-1 means not found):', s.find('q'))
#     * how many times does the string "an" appear in s?
print(f'Occurrences of "an" in "{s}":', s.count('an'))
#     * check if s is alphanumeric
print(f'"{s}" is alphanumeric:', s.isalnum())
#     * transform s to all uppercase
print(f'"{s}" uppercase:', s.upper())

# 2. Given the string "abcdefghijklmn" print the following:
s = 'abcdefghijklmn'
#     * the third character of this string.
print('Third character:', s[2])
#     * the second to last character of this string.
print('Second to last character:', s[-2])
#     * the first five characters of this string.
print('First five characters:', s[:5])
#     * all but the last two characters of this string.
print('All but the last two characters:', s[:-2])
#     * all the characters of this string with even indices (remember indexing
#     starts at 0, so the characters are displayed starting with the first).
print('All the characters with even indices:', s[::2])
#     * all the characters of this string with odd indices
#     (i.e. starting with the second character in the string).
print('All the characters with odd indices:', s[1::2])
#     * all the characters of the string in reverse order.
print('All the characters in reverse order:', s[::-1])
#     * every second character of the string in reverse order, starting from the
#     last one.
print('Every second character, in reverse order:', s[::-2])

# 3. Given the following variables
first_name = 'Mike'
last_name = 'Clarkson'
accounts = 2
balance = 128.5532
# print the following message using the different methods presented for string
# formatting:
# M. Clarkson has 2 bank accounts with a total balance of 128.55$.

print('%.1s. %s has %d bank accounts with a total balance of %.2f$.' %
      (first_name, last_name, accounts, balance))

print('{:.1}. {} has {} bank accounts with a total balance of {:.2f}$.'.format(
      first_name, last_name, accounts, balance))

print('{0:.1}. {1} has {2} bank accounts with a total balance of {3:.2f}$. {0} {1}'
      .format(first_name, last_name, accounts, balance))

print('{first:.1}. {last} has {no_acc} bank accounts with a total balance of '
      '{balance:.2f}$. {first} {last}'.format(
            first=first_name,
            last=last_name,
            no_acc=accounts,
            balance=balance
        ))

print(f'{first_name:.1}. {last_name} has {accounts} bank accounts with a total'
      f' balance of {balance:.2f}$.')
