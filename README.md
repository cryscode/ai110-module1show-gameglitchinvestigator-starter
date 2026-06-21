# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects Normal difficulty and enters a guess of 20
2. Game returns "Too low"
3. User enters a guess of 80 and the game returns "Too high"
4. User score updates after each guess
5. If user guesses correctly game ends, else if attempts are exhausted the user can start a new game

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
================================================== test session starts ==================================================
platform win32 -- Python 3.13.13, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\adike\ai110-module1show-gameglitchinvestigator-starter\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\adike\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 12 items                                                                                                       

tests/test_game_logic.py::test_winning_guess PASSED                                                                [  8%]
tests/test_game_logic.py::test_guess_too_high PASSED                                                               [ 16%]
tests/test_game_logic.py::test_guess_too_low PASSED                                                                [ 25%]
tests/test_game_logic.py::test_easy_difficulty_range PASSED                                                        [ 33%]
tests/test_game_logic.py::test_normal_difficulty_range PASSED                                                      [ 41%]
tests/test_game_logic.py::test_hard_difficulty_range PASSED                                                        [ 50%]
tests/test_game_logic.py::test_secret_within_easy_range PASSED                                                     [ 58%]
tests/test_game_logic.py::test_secret_within_normal_range PASSED                                                   [ 66%]
tests/test_game_logic.py::test_secret_within_hard_range PASSED                                                     [ 75%]
tests/test_game_logic.py::test_secret_out_of_range_bug_fixed PASSED                                                [ 83%]
tests/test_game_logic.py::test_new_game_resets_state PASSED                                                        [ 91%]
tests/test_game_logic.py::test_new_game_resets_lost_state PASSED                                                   [100%]

================================================== 12 passed in 0.25s ===================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
