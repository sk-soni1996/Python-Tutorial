

st = "I am Learning pytHon!"
# 1. captilize() # it will convert the first character in string to upper case
print(st.capitalize())  # I am learning python!

# 2. title() # it will convert the first character of each word in a string to upper
print(st.title()) # I Am Learning Python!

# 3. len() # it will return the lenght of a given string including spaces
print(len(st)) # 21

# 4. upper() # it will convert the entire string to upper case
print(st.upper()) #I AM LEARNING PYTHON!


# 5. lower() # it will convert the entire string to lower case
print(st.lower()) # i am learning python!

# 6. index() # it will return the index of a word or character in the string(only fisrt occurence)
print(st.index('a'))

# 7. casefold() # converts string to lower case
print(st.casefold())

# 8. endswith() # return true or false for a string ends with given pattern
print(st.endswith('tHon!'))
print(st.endswith("n"))

# 9. startswith() # return true or false for a string starts with given pattern
print(st.startswith('I '))
print(st.startswith('I t'))

# 10. find()	# Searches the string for a specified value and returns the position of where it was found(first occurence)
print(st.find('a'))

# 11. count()	# Returns the number of times a specified value occurs in a string
print(st.count('n'))
print(st.count('n', 11, len(st)))
for ch in st:
    print(f"{ch} = {st.count(ch)}")

# print(st.encode(encoding=''))

# 12 join()
lst = ['i','eat', 'apple', 'everyday']
# for i in lst:
#     print(i, end=" ")

print(",".join(lst))

# 13. replace()
print(st.replace('pytHon', 'jython'))

# 14. split()
st_lst = st.split(" ")
print(st_lst)
for word in st_lst:
    print(f"{word} = {len(word)}")


