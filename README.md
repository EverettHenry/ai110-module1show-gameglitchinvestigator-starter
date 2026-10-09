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
Guess a number between a range and have hints for higher or lower, have limited attempts.
- [ ] Detail which bugs you found.
Higher or lower hint not being correct, new game not working, difficulty not working, score not being correct, attempt counter being off by 1
- [ ] Explain what fixes you applied.
Fixed all bugs.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Select your difficulty
2. Enter a guess within your difficulty range
3. Narrow down your guesses until you get the answer or run out of guesses
4. Start a new game or quit

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
tests/test_game_logic.py::test_range_known_difficulties[Easy-expected0] PASSED                                             [  2%]
tests/test_game_logic.py::test_range_known_difficulties[Normal-expected1] PASSED                                           [  4%]
tests/test_game_logic.py::test_range_known_difficulties[Hard-expected2] PASSED                                             [  6%]
tests/test_game_logic.py::test_range_unknown_difficulty_defaults_to_normal[] PASSED                                        [  8%]
tests/test_game_logic.py::test_range_unknown_difficulty_defaults_to_normal[easy] PASSED                                    [ 10%]
tests/test_game_logic.py::test_range_unknown_difficulty_defaults_to_normal[Impossible] PASSED                              [ 12%]
tests/test_game_logic.py::test_range_unknown_difficulty_defaults_to_normal[None] PASSED                                    [ 14%]
tests/test_game_logic.py::test_parse_guess_valid[5-5] PASSED                                                               [ 16%]
tests/test_game_logic.py::test_parse_guess_valid[0-0] PASSED                                                               [ 18%]
tests/test_game_logic.py::test_parse_guess_valid[-3--3] PASSED                                                             [ 20%]
tests/test_game_logic.py::test_parse_guess_valid[100-100] PASSED                                                           [ 22%]
tests/test_game_logic.py::test_parse_guess_valid[7.9-7] PASSED                                                             [ 25%]
tests/test_game_logic.py::test_parse_guess_valid[-2.5--2] PASSED                                                           [ 27%]
tests/test_game_logic.py::test_parse_guess_valid[3.0-3] PASSED                                                             [ 29%]
tests/test_game_logic.py::test_parse_guess_empty[None] PASSED                                                              [ 31%]
tests/test_game_logic.py::test_parse_guess_empty[] PASSED                                                                  [ 33%]
tests/test_game_logic.py::test_parse_guess_not_a_number[abc] PASSED                                                        [ 35%]
tests/test_game_logic.py::test_parse_guess_not_a_number[1.2.3] PASSED                                                      [ 37%]
tests/test_game_logic.py::test_parse_guess_not_a_number[5a] PASSED                                                         [ 39%]
tests/test_game_logic.py::test_parse_guess_not_a_number[--4] PASSED                                                        [ 41%]
tests/test_game_logic.py::test_parse_guess_not_a_number[  ] PASSED                                                         [ 43%]
tests/test_game_logic.py::test_parse_guess_not_a_number[nan] PASSED                                                        [ 45%]
tests/test_game_logic.py::test_parse_guess_not_a_number[inf] PASSED                                                        [ 47%]
tests/test_game_logic.py::test_check_guess_win[50-50] PASSED                                                               [ 50%]
tests/test_game_logic.py::test_check_guess_win[1-1] PASSED                                                                 [ 52%]
tests/test_game_logic.py::test_check_guess_win[100-100] PASSED                                                             [ 54%]
tests/test_game_logic.py::test_check_guess_win[0-0] PASSED                                                                 [ 56%]
tests/test_game_logic.py::test_check_guess_too_high[60-50] PASSED                                                          [ 58%]
tests/test_game_logic.py::test_check_guess_too_high[51-50] PASSED                                                          [ 60%]
tests/test_game_logic.py::test_check_guess_too_high[100-1] PASSED                                                          [ 62%]
tests/test_game_logic.py::test_check_guess_too_high[0--1] PASSED                                                           [ 64%]
tests/test_game_logic.py::test_check_guess_too_low[40-50] PASSED                                                           [ 66%]
tests/test_game_logic.py::test_check_guess_too_low[49-50] PASSED                                                           [ 68%]
tests/test_game_logic.py::test_check_guess_too_low[1-100] PASSED                                                           [ 70%]
tests/test_game_logic.py::test_check_guess_too_low[-1-0] PASSED                                                            [ 72%]
tests/test_game_logic.py::test_update_score_win_points[1-80] PASSED                                                        [ 75%]
tests/test_game_logic.py::test_update_score_win_points[2-70] PASSED                                                        [ 77%]
tests/test_game_logic.py::test_update_score_win_points[5-40] PASSED                                                        [ 79%]
tests/test_game_logic.py::test_update_score_win_points[8-10] PASSED                                                        [ 81%]
tests/test_game_logic.py::test_update_score_win_points[9-10] PASSED                                                        [ 83%]
tests/test_game_logic.py::test_update_score_win_points[50-10] PASSED                                                       [ 85%]
tests/test_game_logic.py::test_update_score_win_adds_to_current_score PASSED                                               [ 87%]
tests/test_game_logic.py::test_update_score_wrong_guess_penalty[Too High] PASSED                                           [ 89%]
tests/test_game_logic.py::test_update_score_wrong_guess_penalty[Too Low] PASSED                                            [ 91%]
tests/test_game_logic.py::test_update_score_wrong_guess_can_go_negative PASSED                                             [ 93%]
tests/test_game_logic.py::test_update_score_unknown_outcome_unchanged[] PASSED                                             [ 95%]
tests/test_game_logic.py::test_update_score_unknown_outcome_unchanged[Unknown] PASSED                                      [ 97%]
tests/test_game_logic.py::test_update_score_unknown_outcome_unchanged[None] PASSED                                         [100%]

====================================================== 48 passed in 0.11s =======================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
