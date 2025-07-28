# https://www.codingame.com/training/medium/scrabble

# Inputs
dic_n = int(input())
dic = []
for i in range(dic_n):
    dic.append(input())
letters = list(input().casefold())


# Functions
def count_letters_from_words(word):
    tmp = {}
    for w in word:
        if w in tmp:
            tmp[w] += 1
        else:
            tmp[w] = 1
    return tmp

def is_writable(word, hand):
    for letter in word:
        if not letter in hand:  # If we don't have the letter in hand
            return False
        if word[letter] > hand[letter]:  # If we don't have enough of this letter
            return False
    return True

def calculate_word_score(word):
    score = 0
    for key in word:
        score += (word[key] * pts[key])
    return score


# Variables
pts = {
    'e':1, 'a':1, 'i':1, 'o':1, 'n':1, 'r':1, 't':1, 'l':1, 's':1, 'u':1,
    'd':2, 'g':2,
    'b':3, 'c':3, 'm':3, 'p':3,
    'f':4, 'h':4, 'v':4, 'w':4, 'y':4,
    'k':5,
    'j':8, 'x':8,
    'q':10, 'z':10,
}
let = count_letters_from_words(letters)
out = ("", 0)


# Process
for word in dic:
    wor = count_letters_from_words(word)
    if is_writable(wor, let):
        score = calculate_word_score(wor)
        if score > out[1]:
            out = (word, score)


# Result
print(out[0])
