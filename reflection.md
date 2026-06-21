# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
I feel it looks like a very typical AI generated game.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  The hints were misleading e.g the secret was 100 but the hint said go lower for 50
  The New game button was not working and I had to reload to try again 
  Normal difficulty has more attempts than easy but I feel it should be the other way around
  The supposed ranges for the different difficulty levels aren't usec

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|guess  |"Go higher" hint   |"Go lower" hint  |"none"                  |
|of 50  |                   |shown instead    |                        |
|none   |Always start with 8|Starts with 7    |"none"                  |
|       |attempts           |on first and 8 on|                        |
|       |                   |second try       |                        |
|none   |New game button    |New game button  |"Game over. Start a new |
|       |resets history     |not working      | game to try again."    |
|""     |"Enter a guess"    |Adds it to history| none until attempts run out|
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
