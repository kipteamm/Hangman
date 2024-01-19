1. **List of words**: 
   - Provide a predefined list of words.
   - The programme randomly selects a word from this list at the beginning of each game.

2. **Displaying the word**:
   - The word is initially hidden from the player. Later, the letters he guesses correctly are revealed.

3. **Letter guessing**:
   - The player guesses a letter (must always be an alphabetic character).
   - If the entry is invalid, the player is asked to guess again.

4. **Letter guessing logic**:
   - If the guessed letter appears in the word:
     - Reveal the letters in the visible word.
   - If the guessed letter is not in the word:
     - Add the letter to a list of incorrectly guessed letters.

5. **Wrong letter**:
   - The player may guess wrong a maximum of 7 times.
   - Keep track of each letter he guesses and is wrong and show it so it does not fall into rehearsal.

6. **Winning**:
   - The player wins if he guesses all the letters in the word correctly before the maximum number of wrong is exceeded.

7. **Lose**:
   - The player loses if he exceeds the maximum number of errors allowed.

8. **End of the game**:
   - When the game ends, reveal the correct word to the player.

9. **User interface**:
   - Continuously update and display the current status of the word (correctly guessed letters and remaining unguessed letters).
   - The current list of incorrectly guessed letters and the remaining number of allowed
