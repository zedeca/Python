#NumberGuesser By Zedeca


def NumGPy():
    print('Welcome to NumberGuesser By Zedeca')
    main=input('To Start The Game, type "go": ')
    
    if main=='go' or main=='GO' or main=="Go" or main=='start':
        qrange=input('Ok! What shall the range (Last Number) of guessing?\n(Enter The Number Till Which You Would Like to Guess) ')
        
        try:
            frange=int(qrange)
        except:
            print('Invalid Input. Enter an Integer Only!')
        
        else:
            print('Ok!',frange,'is the range!')
            import random
            import math
            
            t1num=random.randint(1,frange)
            t2num=math.floor(t1num)
            qcount=0
            
            print('Random Number Generated!')
            
            while t2num<=frange:
                qcount=qcount+1
                i1=input(str(qcount)+'. What is your number guess? ')
                
                try:
                    checki1=int(i1)
                except:
                    print('Enter Integers as  Guesses! ')
                
                else:
                    if int(i1)==t2num:
                         print('Very Good! You have guessed the number! ')
                         break
                    
                    elif int(i1)>frange:
                         print('Your guess is above your own range. Try Again!')
                    
                    elif int(i1)!=t2num and t2num>6:
                         
                         if int(i1)==t2num-6 or int(i1)==t2num-5 or int(i1)==t2num-4 or int(i1)==t2num+6 or int(i1)==t2num+5 or int(i1)==t2num+4:
                             print('Close! But you can do better!')
                         
                         elif int(i1)==t2num-3 or int(i1)==t2num-2 or int(i1)==t2num-1 or int(i1)==t2num+3 or int(i1)==t2num+2 or int(i1)==t2num+1:
                             print('Super Close!')
                         
                         else:
                             print('Try Again!')
                    
                    elif int(i1)!=t2num and t2num<6:
                         print('Try Again')
                    
                    else:
                         print('Invalid Guess. Next time, just guess numbers...')     
    
    else:
        lstep=input('Invalid Command Request. Type "go" to play. Type "done" to stop playing NumberGuesser!')
        
        if lstep=='go':
            print('Okay!')
            #Goto
        
        elif lstep=='done':
            print('Okay, have a nice day!')
        
        else:
            print('Invalid Input')

NumGPy()
