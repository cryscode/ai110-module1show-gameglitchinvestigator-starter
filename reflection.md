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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude, ChatGPT
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Claude suggested a fix for the misleading hint issue and even mentioned a secondary bug that was a potential problem
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Claude was mislead by a comment I left for myself for a different problem so suggested a fix that didnt even relate to the problem and was breaking something else.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
By testing the game myself and seeing improved results.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
I had to check the problem i had previously reported in my table to amke sure the output was as expected. I realized that bugs could come from the tiniest mistake and it was really hard to find by scanning.
- Did AI help you design or understand any tests? How?
Claude designed tests for each of the functions it corrected.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
A rerun is when the application script runs from the top to bottom again and session state helps you store and remember variables across reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I would ask AI for help with tests because it does a good job in generating robust and detailed tests.
- What is one thing you would do differently next time you work with AI on a coding task?
I would definitely ask for multiple things in one prompt as well as all related things in one prompt because it helps me stay organized.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
While I know AI makes mistakes, the project showed that AI mistakes could be sillier than a human's code so we still need to be careful when using AI.
