# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
The first time I ran the game, it loaded successfully, but I noticed several bugs. The game always displayed "Guess a number between 1 and 100" even when a different difficulty was selected. The attempts counter was also incorrect because attempts started at 1 instead of 0. Another issue was that the New Game button did not fully reset the game state, leaving some values from the previous game.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Select Easy difficulty|Display range 1–20 |Displayed "Guess a number between 1 and 100" | None|
| Start a new game| Full attempt count available| Attempts already reduced because attempts started at 1| None|
|Click New Game after playing|Score, history, and status reset |Previous values remained|None |

---

## 2. How did you use AI as a teammate?

I used ChatGPT as my AI teammate during this project. It helped me identify bugs, understand the code, and refactor logic into a separate file.

One correct AI suggestion was moving the game logic functions (get_range_for_difficulty, parse_guess, check_guess, and update_score) from app.py into logic_utils.py. I verified this by running the game after updating the imports and confirming that the application still worked correctly.

One incorrect or misleading AI suggestion happened after refactoring the check_guess() function. The logic was simplified, but the code in app.py was still converting the secret value into a string. This caused a TypeError when comparing an integer guess to a string secret. I verified the issue by running the game and seeing the error message, then fixed it by removing the string conversion
---

## 3. Debugging and testing your fixes

I decided a bug was fixed only after testing both the code and the running application. After making changes, I ran the game and checked whether the behavior matched the expected result.

I added pytest tests for the check_guess() function. The tests verified that winning guesses returned "Win", higher guesses returned "Too High", and lower guesses returned "Too Low". All tests passed successfully when I ran pytest.

AI helped me understand how to structure the tests and what outcomes should be verified. After the tests passed, I also launched the application with streamlit run app.py to confirm the fixes worked in the live game.
---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the entire script whenever the user interacts with the application. Session state is used to preserve values between reruns, such as scores, attempts, and game status. Without session state, variables would reset every time a button was clicked. Session state allows the application to remember information while still using Streamlit's rerun model.
---

## 5. Looking ahead: your developer habits

One habit I want to reuse is testing my code immediately after making a change. Running pytest and manually checking the application helped me find mistakes before moving on to the next step.

Next time I work with AI on a coding task, I will verify each suggested change more carefully before assuming it is correct. This project showed me that AI can be very helpful, but it can also introduce new bugs if I do not review its suggestions carefully.

This project changed the way I think about AI-generated code because I learned that AI is a useful assistant, not a replacement for testing and debugging. Developers still need to verify results and understand the code that AI produces.
