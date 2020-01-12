from random import randint
from random import shuffle
import operator


print('Basic Math - Addition, Subtraction and Multiplication')
score = int(0)
rounds = int(0)
operatordictionary = {1:operator.add, 2:operator.sub, 3:operator.mul, 4:operator.truediv}       #operators to randomize
operatordictionarystring = {1:'+', 2:'-', 3:'x', 4:'/'}                                         #printable symbols for operator

while rounds < 10:
    opassign = randint(1,3)                                                                     #generate random # for operator selection
    operatorfunction = operatordictionary[opassign]
    operatorstring = operatordictionarystring[opassign]


    def question(operatorfunction, operatorstring):

        global score
        global rounds
        
        if opassign < 3:                                                                        #set larder random numbers for addition and subtraction
            first = randint(1,20)
            second = randint(1,20)
        else:                                                                                   #set max 12x12 for multiplicaton
            first = randint(1, 12)
            second = randint(1, 12)
         
        answerok = False   

        while answerok == False:     
            print('\n\nWhat is ' + str(first) + ' ' + operatorstring + ' ' + str(second) + '?') #ask the question
            correctanswer = round(operatorfunction(first, second))                              #destermine correct answer

            answerlist = [correctanswer, round(correctanswer + randint(6,10)), (correctanswer + randint(1,5)), round(correctanswer - randint(1,5))]
            shuffle(answerlist)                                                                 #shuffle the formulas so multiple choice is random order 
                                                        
            print('1 - ' + str(answerlist[0] ) + '\n2 - ' + str(answerlist[1]) + '\n3 - ' + str(answerlist[2]) + '\n4 - ' + str(answerlist[3]))
    
           
            try:
                answer = int(input('\nWhat is your answer 1 - 4 >>> '))                         #check that entered answer is either 1, 2, 3 or 4
                break
            except ValueError:
                print('Invalid input, please enter 1 - 4.')


        if answer == (answerlist.index(correctanswer) + 1):                                     #reference correct answer by position in the shuffled list
            print('\nCorrect!')
            score += 1
            rounds += 1
        elif answer > 4:
            print('Invalid input, please enter 1 - 4.')
            answerok = False                              
        elif answer < 0:
            print('Invalid input, please enter 1 - 4.')
            answerok = False                                         
        else:
            print('\nYou are wrong')
            rounds += 1


    question(operatorfunction, operatorstring)                                                  #ask the question using the random operator
        
print('\nTest complete - You scored ' + str(score) + ' out of ' + str(rounds))

