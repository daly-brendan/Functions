#anagram function

def are_anagrams (word1, word2):
    #returns true if the two words are identical
    word1_sorted = sorted(word1)
    word2_sorted = sorted(word2)

    if word1_sorted == word2_sorted:
        print ("The words {} and {} are anagrams".format(word1, word2))
        return True

    else:
        print ("The words are not anagrams")
        return False

two_words = input("Enter two words seperated by a space here: ")
word1, word2 = two_words.split()

are_anagrams(word1,word2)


"""
"""
#score analysis
def who_won(score1, score2):
    if score1 < score2:
        print ("Team 2 won the game")
    elif score1 > score2:
        print ("Team 1 won the game")
    elif score1 == score2:
        print ("The game ended in a tie")

who_won(9,5)

"""
"""

def vowel_and_consonants(my_string):
    num_vowels = 0
    consonant_count = 0
    my_string_bool = my_string.isalpha()
    while my_string_bool == True:
        for char in my_string:
            if char in "aeiouAEIOU":
                num_vowels = num_vowels + 1
            else:
                consonant_count = consonant_count + 1
        print('Ther are', num_vowels, 'vowels in your sentence')
        print('There are', consonant_count, 'consonants in your sentence')
        break
    while my_string_bool == False:
        print ("This program only accepts alphabetical inputs, numbers and punction should be removed before hiiting enter!")
        break


my_string = input("Enter a sentence here: ")
vowel_and_consonants(my_string)

"""
"""
#discount calculator
def members_discount(member_bool):
    item_price = 90
    item_price = item_price * .95
    if member_bool == True:
        item_price = item_price * .90
        print(item_price)
    else:
        item_price = item_price
        print(item_price)
members_discount(False)

"""
"""
#y2k
def is_it_a_leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0:
            print (year, "is a leap year")
        else:
            print (year, "is not a leap year")
is_it_a_leap_year(1896)

#twitter fingers
def char_count(message):  
    message_length = len(message)
    if message_length > 160:
        print("This message is too long; this is what we allow: ")
        print("")
        print (message[0:160])
    else:
        print(message, "The length of the message is:", len(message))

my_message = input("enter a message here to test it's length: ")
char_count(my_message)

"""
"""
#string to list converter
def str_converter(string):
    list1 = []
    list1 [:0]=string
    return list1
orig_str = 'abcde'
new_list = (str_converter(orig_str))
        #there has to be an easier way of doing this
