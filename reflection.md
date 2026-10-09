# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
Looked clean but with many bugs.
- List at least two concrete bugs you noticed at the start  
see bug reproduction log
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |
| | | | |
| | | | |

1. Attempts left not counting the first attempt and then stops 1 early (off by 1), fixed
2. Gets the output wrong, even for numbers outside the range, e.g. 120 and will say go higher, fixed
3. New game button does not work, need to refresh the page fixed
4. The AI found a bug with the score:
The scoring in update_score also looks odd. A "Too High" guess adds 5 points on even attempts and subtracts 5 on odd ones, which probably explains your negative score. fixed
5. The difficulty selection does not seem to work. fixed

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI found a bug with the score wether it was even or not as too high adding points.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
I dont have an example for this however there was one suggestions where the AI got it wrong where it was a rendering issue rather than a logic issue on the backened, the AI thought it was a logic issue at first but then found the correct issue on the next diagnosis for the issue.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I ran streamlit again and did tests on the website.
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
Tested all methods in logic_utils.py, learned how to use pytest and have AI help streamline that process.
- Did AI help you design or understand any tests? How?
Absolutely, AI is incredibly powerful for finding bugs where tracing them back could take many hours.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
It seems the app uses many states to determine where it is at in the program and by using these states u can "rerun" to start from scratch and create a fresh game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
The power of using AI to debug and analyze code.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
Use the AI to explain through more of the code rather than going straight to debugging.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI generated code is a very efficient and powerful but can still make mistakes.