from functies import *

# test 1: getNumberOfCharacters
if getNumberOfCharacters('aap.') == 3:
    print("Test geslaagd")
    print(getNumberOfCharacters('aap '))
else:
    print("Deze test is niet geslaagd")
    print(getNumberOfCharacters('aap '))

# schrijf zelf nog wat extra testen voor getNumberOfCharacters

# test 2: getNumberOfSentences
if getNumberOfSentences(getText('easy')) == 14:
    print("Test geslaagd")
    print(getNumberOfSentences(getText('easy')))
else:
    print("Deze test is niet geslaagd")
    print(getNumberOfSentences(getText('easy')))

# schrijf zelf nog een extra testen voor getNumberOfSentences (gebruik test.txt).

if getNumberOfSentences(getText('difficult')) == 3:
    print("Test geslaagd")
    print(getNumberOfSentences(getText('difficult')))
else:
    print("Deze test is niet geslaagd")
    print(getNumberOfSentences(getText('difficult')))

if getNumberOfSentences(getText('test')) == 5:
    print("Test geslaagd")
    print(getNumberOfSentences(getText('test')))
else:
    print("Deze test is niet geslaagd")
    print(getNumberOfSentences(getText('test')))

# test 3: getNumberOfWords
print(getNumberOfWords(getText('data\difficult1.txt')))
if getNumberOfWords(getText('data\difficult1.txt')) == 82:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")

if getNumberOfWords(getText('data\easy1.txt')) == 11:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")

# schrijf zelf nog een extra testen voor getNumberOfWords (gebruik test.txt).