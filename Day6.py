# Hangman 
hangman_stages_simple = [

    """
  +-----+
  |     |
  |     O
  |      
  |      
  |      
--+--
    """,
    
    """
  +-----+
  |     |
  |     O
  |     |
  |      
  |      
--+--
    """,
    
    """
  +-----+
  |     |
  |     O
  |    /|
  |      
  |      
--+--
    """,
    
    """
  +-----+
  |     |
  |     O
  |    /|\\
  |      
  |      
--+--
    """,
    
    """
  +-----+
  |     |
  |     O
  |    /|\\
  |    / 
  |      
--+--
    """,
    
    """
  +-----+
  |     |
  |     O
  |    /|\\
  |    / \\
  |      
--+--
    """
]

print("\n-----------------------")
print(">>> Hangman Time! <<<")
print("-----------------------")

word_to_guess = "How To Train Your Dragon"
category = "Movie"
life = 0  

display = []
for i in word_to_guess:
    if i == " ":
        display.append(" ") 
    elif i.isalpha():
        display.append("_") 
    else:
        display.append(i)   

print(f">> Category - {category}")
print(f">> To Guess - {''.join(display)}")
print("-----------------------")

def make_guess():
    global life
    guess = input("\n>> Your guess? - ")
    if guess.lower() in word_to_guess.lower():
        for i in range(len(word_to_guess)):
            if word_to_guess[i].lower() == guess.lower():
                display[i] = word_to_guess[i]
        print(f"\n>> To Guess - {''.join(display)}")
    else:
        life += 1
        print(hangman_stages_simple[life-1])
        print(f"Wrong guess! Lives left: {6-life}")
        print(f"\n>> To Guess - {''.join(display)}")

def checkblank():
    return "_" in display

while checkblank() and life < 6:
    make_guess()

if not checkblank():
    print("\nCongratulations, you guessed the word!")
else:
    print("\nGame Over! The word was:", word_to_guess)
