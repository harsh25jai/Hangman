import random
import time

print"HANGMAN"
print"\n"
name = raw_input(" Type your Name : ")
print "Hello! " ,name
print "Ready to play HANGMAN"
print "\n"
time.sleep(1)
print "Start Guessing Word .................to win the Game"
time.sleep(0.5)

def  words():
    w=['hangman','python','computer','fundamentals','methothodology','programming','component','foundations','operating','software','windows','linux','keyboard','mouse','printer','analoag','joystick','apple','dictionary','resolution','tornado','volcano','literals','tuples','internals','efficiency','hate','love','teacher','friend','secret','race','game','designer','lenovo','mobile','dish','bottle','talktime','manual','analysis','finanancial','comprehensive','guess','linear','array','calculator','camera','finance','','','']
    return w[random.randint(0,len(w))]

word = words()
guesses = ''
turns = 10

while turns > 0:         
    failed = 0             
    for char in word:      
        if char in guesses:    
            print char,
        else:
            print "_",     
            failed += 1    
    if failed == 0:        
        print "\n YOU HAVE WON THE HANGMAN"
        print '''            
           /(|
          (  :
         __\  \  _____
       (____)  `|
      (____)|   |
       (____).__|
        (___)__.|_____'''

        break              

    print
    guess = raw_input("Guess a character :")
    guesses += guess                    
    if guess not in word:  
        turns -= 1        
        print "WRONG\n" 
        print "YOU HAVE", + turns, 'MORE GUESSES'
        if turns == 0:           
            print   "YOU HAVE LOST THE HANGMAN"
            print'''
        _,....._
        (___     `'-.__
       (____
       (____
       (____         ___
            `)   .-'`
            /  .'
           | =|
            \_\    '''
            print  "ANSWER :",word
        
time.sleep(5)

