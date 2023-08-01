# Refactor
## AI based code refactor.

The module's primary focus is to assist users in writing faster, more coherent, and more Pythonic code. OpenAI's ChatGPT model offers two main methods for interacting with it: suggest() and create_conversation(). These instance methods of the ChatGPT class provide suggestions, explanations, or answers related to specific user-written functions, either defined in the same environment or imported. The suggestions can be centered around three key topics: optimizing code speed, improving code style, or explaining the purpose of the function. Users have the flexibility to request the model's assistance in any of these areas to enhance their coding experience. 

### How to use:

<img width="1138" alt="Screenshot 2023-02-02 at 16 49 20" src="https://user-images.githubusercontent.com/93786486/216373017-879c036a-e3c0-4416-bad5-1dfb225245b5.png">

We can call the suggest method on our ChatGPT instance. We can specify the focus and if code should be returned 
(and other kwargs modifying the response's length or randomness).

<img width="1213" alt="Screenshot 2023-02-03 at 16 23 18" src="https://user-images.githubusercontent.com/93786486/216640778-c150125c-ae9e-4583-ba69-4450a8eea824.png">


We can continue the conversation if we are not satisfied with the answer by calling create_conversation with the parameters shown below. 
To continue the conversation we have to set the forget parameter to False (so that the memory is not emptied) and we can specify a remind_me parameter to be able to look at what's in the model memory (our conversation so far, including the function we inspected and the suggestions it made for us).
We can either specify the next question as an argument or wait for the input prompt.
We can exit from the create_conversation function by typing "BYE" or "QUIT".

<img width="1213" alt="Screenshot 2023-02-03 at 16 23 38" src="https://user-images.githubusercontent.com/93786486/216640863-7c3f28a4-3937-42ef-b66e-1a1d8b9c4c23.png">

