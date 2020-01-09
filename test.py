from random import randint
import operator


print('Basic Math')
score = int(0)
rounds = int(0)
operatordictionary = {1:operator.add, 2:operator.sub, 3:operator.truediv, 4:operator.mul}
operatordictionarystring = {1:'+', 2:'-', 3:'/', 4:'x'}

while rounds < 3:
    opassign = randint(1,4)
    operatorfunction = operatordictionary[opassign]
    operatorstring = operatordictionarystring[opassign]


    def question(operatorfunction, operatorstring):

        global score
        global rounds
        first = randint(1,20)
        second = randint(1,20)
        answerok = False   

        while answerok == False:     
            print('\n\nWhat is ' + str(first) + ' ' + operatorstring + ' ' + str(second) + '?')
            correctanswer = round(operatorfunction(first, second))
            correctansposition = 1
    
            ans1 = correctanswer
            ans2 = round((correctanswer * randint(1,10)) / 100  + correctanswer)
            ans3 = round(correctanswer + randint(1,7))
            ans4 = round(correctanswer - randint(1,7))
    
            print('1 - ' + str(ans1) + '\n2 - ' + str(ans2) + '\n3 - ' + str(ans3) + '\n4 - ' + str(ans4))
    
           
            try:
                answer = int(input('\nWhat is your answer 1-4 >>> '))
                break
            except ValueError:
                print('Invalid input, please enter 1 - 4.')
            
                if answer < 5:
                    answerok = True
                else:
                    answerok = False



        if answer == 1:
            print('\nCorrect!')
            score += 1
        else:
            print('\nYou are wrong')

        rounds += 1


    question(operatorfunction, operatorstring)
        
print('\nTest complete - You scored ' + str(score) + ' out of ' + str(rounds))

