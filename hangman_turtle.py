import random
import turtle

words=["python","computer","java","code","terminal"]
secret_word= random.choice(words)

what_we_see=["_"] * len(secret_word)

#Game state variables (before the game starts)
used_letters=[]  #letters already guessed by the player
wrong= 0         #number of wrong guesses
max_wrong= 6     #maximum allowed wrong guesses


wn = turtle.Screen()        #about screen
wn.title("Hangman Game")
wn.bgcolor("lightblue")

t = turtle.Turtle()
t.hideturtle()         
t.speed(0)     #max speed
t.pensize(2)  


#CONSTANTS
BASE_X = -100
BASE_Y = -100
POST_HEIGHT = 200
BEAM_LENGTH = 100
ROPE_LENGTH = 50

ROPE_X = 100
ROPE_Y = 35

HEAD_RADIUS = 15
BODY_LENGTH = 50
ARM_LENGTH = 25
LEG_LENGTH = 30

#for base, vertical post, top beam, and the rope for hanging the head
def draw_gallows():
    t.penup()
    t.goto(BASE_X, BASE_Y)
    t.pendown()
    t.forward(200)              # base
    t.backward(100)
    t.left(90)
    t.forward(POST_HEIGHT)      # post
    t.right(90)
    t.forward(BEAM_LENGTH)      # beam
    t.right(90)
    t.forward(ROPE_LENGTH)      # rope
    t.penup()
    t.setheading(0)

#for head
def draw_head():
    t.goto(ROPE_X, ROPE_Y - HEAD_RADIUS)
    t.pendown()
    t.circle(HEAD_RADIUS)
    t.penup()

#for body
def draw_body():
    t.goto(ROPE_X, ROPE_Y - 2 * HEAD_RADIUS + 15)
    t.setheading(-90)
    t.pendown()
    t.forward(BODY_LENGTH)
    t.penup()

#for left arm
def draw_left_arm():
    t.goto(ROPE_X, ROPE_Y - 2 * HEAD_RADIUS + 10)
    t.setheading(180)
    t.pendown()
    t.forward(ARM_LENGTH)
    t.penup()

#for right arm
def draw_right_arm():
    t.goto(ROPE_X, ROPE_Y - 2 * HEAD_RADIUS + 10)
    t.setheading(0)
    t.pendown()
    t.forward(ARM_LENGTH)
    t.penup()

#for left leg
def draw_left_leg():
    t.goto(ROPE_X, ROPE_Y - 2 * HEAD_RADIUS - BODY_LENGTH + 15)
    t.setheading(-120)
    t.pendown()
    t.forward(LEG_LENGTH)
    t.penup()

#for right leg
def draw_right_leg():
    t.goto(ROPE_X, ROPE_Y - 2 * HEAD_RADIUS - BODY_LENGTH + 15)
    t.setheading(-60)
    t.pendown()
    t.forward(LEG_LENGTH)
    t.penup()

#regarding the order in which the drawings should be
def update_hangman(wrong):
    if wrong == 1:
        draw_head()
    elif wrong == 2:
        draw_body()
    elif wrong == 3:
        draw_left_arm()
    elif wrong == 4:
        draw_right_arm()
    elif wrong == 5:
        draw_left_leg()
    elif wrong == 6:
        draw_right_leg()


#Draw gallows at start
draw_gallows()

#Game loop
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
       update_hangman(wrong)

#End of the game
if "_" not in what_we_see:
   print("\nConguratulations! You won! The word was: ", secret_word )

else:
   print("\nGame Over! You lost! The word was: ", secret_word)


wn.mainloop()