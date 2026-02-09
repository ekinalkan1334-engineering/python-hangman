import random

words=["python","computer","java","code","terminal"]
secret_word= random.choice(words)

what_we_see=["_"] * len(secret_word)

#Game state variables (before the game starts)
used_letters=[]  #letters already guessed by the player
wrong= 0         #number of wrong guesses
max_wrong= 6     #maximum allowed wrong guesses


print("Welcome to Hangman")

while wrong < max_wrong and "_" in what_we_see:
    print("\nWord:", " ".join(what_we_see))
    print("Used letters:", ",".join(used_letters))
    print("Wrong guesses:", wrong, "/", max_wrong)

    letter= input("Enter a letter: ").lower()   #Ask the player for a letter

    if len(letter) != 1:                       #Check if only a single character was entered
      print("Please enter a single letter")
      continue

    if not letter.isalpha():                  #Check if it's a valid letter
       print("Please enter a letter only")
       continue
    
    if letter in used_letters:                  #Check if the letter was already used
       print("You already used this latter")
       continue
 
    #Add the valid letter to the list of used letters
    used_letters.append(letter)


    #Check if the letter is in the secret_word
    if letter in secret_word:
       for index in range(len(secret_word)):       #Update what_we_see for all positions of this letter
          if secret_word[index] == letter:
             what_we_see[index] = letter

             print("Correct guess!")

    else:            #Letter is wrong
       wrong += 1
       print("Wrong guess!")

#End of the game
if "_" not in what_we_see:
   print("\nConguratulations! You won! The word was: ", secret_word )

else:
   print("\nGame Over! You lost! The word was: ", secret_word)



   
       










