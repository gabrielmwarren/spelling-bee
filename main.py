import random
import string

word_file = open('words.txt', 'r')
word_list = []
for l in word_file.readlines():
    word_list.append(l.strip())
word_file.close()



ctrltr = input("What's the center letter of the beehive?")
if len(ctrltr) != 1:
    feedback = "I only accept a single letter. Please enter the center letter again."
    print(feedback)

outerltrs = input("What are the outer letters of the beehive?")
if len(set(outerltrs)) != 6:
    feedback = "Please provide six unique letters."
    print(feedback)

min_length = int(input("What is the minimum word length?"))
if min_length > 10:
    feedback = "Please provide single digit number."
    print(feedback)

beehive = ctrltr + outerltrs

valid_words = []
pangrams = []
def main():
    count = 0
    while (len(valid_words) < 300):
        # word = generate_Word(beehive)
        word = random.choice(word_list)
        count += 1
        if (ctrltr in word) and (set(word).issubset(set(beehive))) and (len(word) > (min_length-1)):
            valid_words.append(word)
        if set(word) == set(beehive):
            pangrams.append(word)
    print(count)
main()
results = set(valid_words) 
separator = ", "
print(separator.join(sorted(results, key=lambda item: (-len(item), item))))
print(separator.join(pangrams))