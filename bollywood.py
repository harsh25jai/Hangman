import random
import time

print"BOLLYWOOD"
print"\n"
name = raw_input(" Type your Name : ")
print "Hello! " ,name
print "Ready to play BOLLYWOOD"
print "\n"
time.sleep(1)
print "Start Guessing Word .................to win the Game"
print'\n'
time.sleep(0.5)

def  words():
    w=['partner','players','firangi','ghost','agneepath','kahaani','housefull','tezz','jannat','ishaqzaade','cocktail','joker','murder','razz','barfi','heroine','Yaariyan','heartless','aiyyaa','makkhi','chakravyuh','rush','talaash','khiladi','dabangg','kick','dhoom','gunday','highway','queen','bewakoofiyan','dishkiyaoon','youngistaan','heropanti','masti','tever','aashiqui','fugly','crook','jackpot','rascals','luck','golmaal','veer','besharam','race','ramleela','rangrezz','race','singham','zid','xpose','raone','raanjhanaa','lootera','krrish','prince','rrajkumar','holiday','highway','bodyguard','wanted','boss','aurangzeb','haider','','']
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
        print'\n'
        print "\n YOU HAVE WON THE BOLLYWOOD"
        print'\n'
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
            print   "YOU HAVE LOST THE BOLLYWOOD"
            print'\n'
            print "MOVIE IS :",word
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
            

