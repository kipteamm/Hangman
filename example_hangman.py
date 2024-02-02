import random

words = ["Juxtaposition", "Quizzical", "Zephyr", "Rhythmic", "Gypsy", "Flapjack", "Knapsack", "Quixotic", "Mystic", "Crypts", "Oxymoron", "Yacht", "Syzygy", "Whiskey", "Bungalow", "Jackpot", "Jazz", "Jigsaw", "Zombify", "Zigzagging", "Kaleidoscope", "Quarantine", "Haphazard", "Waltz", "Vortex", "Juxtapose", "Quagmire", "Jargon", "Hijack", "Buzzwords", "Embezzle", "Jazzier", "Quackery", "Zucchini", "Muzak", "Flummox", "Quarry", "Jovial", "Gizmo", "Bamboozle", "Quartz", "Zipper", "Quasar", "Hyphen", "Quota", "Sphinx", "Quiver", "Yak", "Zodiac", "Quip"]

word = random.choice(words)

wrong_letters = []
visible_word = []

for letter in word:
    visible_word.append('_')
    
print('Word:', " ".join(visible_word))

while len(wrong_letters) < 8:
    correct = False
   
    letter = input("Make a guess: ")
    
    if not letter.isalpha():
        print('You cannot use nonalphabetic characters.')
        
        continue
   
    if letter in wrong_letters or letter in visible_word:
        print('You already tried that letter!')
   
        continue
   
    for letter_index in range(len(word)):
        if word[letter_index] == letter:
            visible_word[letter_index] = letter
           
            correct = True
       
    if not correct:
        wrong_letters.append(letter)

    print('Word:', " ".join(visible_word))
    
    if "".join(visible_word) == word:
        print("You won!")

        break
   
    print('Wrong:', ", ".join(wrong_letters))

if "".join(visible_word) != word:
    print(f"You lost, the word was: {''.join(word)}.")
