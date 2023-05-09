#Counts the vowels in a word

user_input = input("Please enter a word from which to count the vowels: ")
user_input = user_input.lower()
vowel_list = ["a", "e", "i", "o", "u"]
vowel_in_word = []

for letter in user_input:
    
    if letter in vowel_list: 
        vowel_in_word.append(letter)

vowel_count = len(vowel_in_word)
print(vowel_count)

print (test)