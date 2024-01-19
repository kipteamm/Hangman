1. **List of words**: 
   - Provide a (predefined) list of words.
   - The program randomly selects a word from this list at the beginning of each game.

2. **Start of the game**:
   - The word is initially hidden from the player.
   - Give the player the length of the word.

3. **Letter guessing**:
   - The player guesses a letter (must always be an alphabetic character).
   - If the entry is invalid, the player is asked to guess again.

4. **Letter guessing logic**:
   - If the guessed letter appears in the word:
     - Reveal the letters in the visible word.
   - If the guessed letter is not in the word:
     - Add the letter to a list of incorrectly guessed letters.
    
5. **Provide the user with feedback**
   - Show them the updated word or the current state of the word.
   - Show them their list of wrong letters.

6. **Wrong letter**:
   - The player may guess wrong a maximum of 7 times.
   - Keep track of each letter they guess to prevent the player from guessing an already guessed letter again.
     
7. **Winning**:
   - The player wins if they guess all the letters in the word correctly before the maximum number of wrongs is exceeded.

7. **Lose**:
   - The player loses if they exceed the maximum number of mistakes allowed.

8. **End of the game**:
   - When the game ends, reveal the correct word to the player.

9. **User interface**:
   - Continuously update and display the current status of the word (correctly guessed letters and remaining unguessed letters).
   - Continuously update and display the current list of incorrect guesses.
