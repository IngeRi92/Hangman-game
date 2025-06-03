Estonian Hangman Game (Poomismäng)

This is a fun and educational Hangman game written in Python using **Pygame**. It features **long and interesting Estonian words**, some with explanations to help you learn new vocabulary while playing.

 Words like:
- `kroonilineinflatsioonisõltuvus`
- `kuu-uurija`
- `kintsakongad` *(= viletsad kontsakingad)*

---

##  Features

- Estonian alphabet support (`Õ`, `Ä`, `Ö`, `Ü`)
- Automatically fills in non-letter characters (like `-`)
- Random word selection from an external file
- Word explanations shown after guessing
- Responsive UI: resizes correctly with the window
- Classic hangman drawing as you make mistakes

---

## Coming/Ideas (Not in  order!)

# Gameplay Enhancements

1. Difficulty Levels
- Easy: Short common words
- Medium: Longer or compound words
- Hard: Rare or complex Estonian words

2. Hint System
- Allow the player to press a key (e.g., H) once per game for:
- A letter reveal
- A short clue (without revealing the definition)

3. Lives & Score System
- Display how many guesses are left.
- Add a score counter that increases with correct words and decreases on failure.

4. Multistage Hangman Drawing
- Make the drawing more detailed (e.g., add facial expressions or animations).

# Educational Features

5. Explanation Popups
- You already do this — keep enhancing it!
- Add an option like [E] to "expand explanation" and show more context or usage.

6. Pronunciation Audio
- Add .mp3 files or use a TTS engine to pronounce the Estonian word when revealed.
- This is great for language learners.

# Visual Improvements

7. Dark Mode / Theme Toggle
- Add a key like T to toggle between light/dark mode.

8. Animations or Effects
- Animate the hangman being drawn (slow fade-in or shake effect on wrong guess).
- Add background music or sound effects for win/loss.

# Game Modes

9. Timed Mode
- Add a countdown timer — guess the word before time runs out!

10. Multiplayer or Challenge Mode
- Pass & play: One player types the word, the other guesses.
- Online multiplayer is possible but complex. // Split Screen, Both get same word (Dont see other player word), who quesses faster gets point

# Content and Word System

11. Categories
- Group words by themes (e.g., "nature", "history", "technology", etc.)
- Let the player choose the category before starting.

12. Dynamic Word Sources
- Pull words from an online API or Estonian language corpus.
- Or use separate .txt files per category.

# Progression and Stats

13. Track Wins/Losses
- Save stats locally (in a JSON or text file):
- Words guessed
- Accuracy
- Longest streak

14. Unlock Achievements
- E.g., “Guessed a 20-letter word” or “Won 5 games in a row”

# Advanced / Bonus Ideas

15. Word Puzzle Mode
- Add a mini crosswords or “jumble” mode where the letters are shuffled.

16. AI Assistant
- Suggests a likely next letter based on letter frequency (especially useful for learners).

17. Online Leaderboard (Optional)
- Send stats to a lightweight Flask backend + SQLite/PostgreSQL
- Display top scores globally