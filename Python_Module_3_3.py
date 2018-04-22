
# coding: utf-8

# In[2]:


def longest_word(list_of_strings):
    max_length = 0
    longest_word = ""
    for s in list_of_strings:
        if(len(s) > max_length):
            max_length = len(s)
            longest_word = s
    return longest_word

list_of_words = input("Please enter a list of comma separated words: ")
print("The longest word entered is: ", longest_word(list_of_words.split(",")))

