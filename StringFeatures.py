def VertigoZString():
    #Zedeca : Vertigo String
    #NOTE: This program is CASE-SENSITIVE.
    import re
    import datetime
    import pandas as pd
    
    x=str(datetime.datetime.now())
    print(x[:10])
    print('Welcome To Vertigo String By Zedeca\n')
    name=input('Enter Username: ' )
    
    def CList():
        print('|  Command List   |')
        print('1. Locate Text')
        print('2. Find and Replace')
        print('3. Whitespace Remover')
        print('4. Word Frequency')
        
    CList()
    main=input(str('Hello '+name+'!\nWhat can Vertigo do for you from the command list above? '))
    
    if main=='Find And Replace' or main=='FR' or main=='fr' or main=='find and replace' or main=='2':
         zstr=input(str('Enter the data: '))
         ystr=input(str('Enter the data to find/to be replaced: '))
         xstr=input(str('Enter the data to replace with: '))
         qstr=zstr.replace(ystr,xstr)
         print(qstr)
         print('There You Go!')
    
    elif main=='Locate Text' or main=='locate text' or main=='lt' or main=='LT' or main=='1':
         astr= input('Enter Number/Letter/Word/Sentence/Phrase: ')
         nstr= input(str('Enter the Number/Letter/Word/Sentenece/Phrase To Locate: '))
         ipos= astr.find(nstr)
         npos= ipos+1
         neto=astr.count(nstr,0,len(astr))
         LTlist=re.findall(nstr,astr)
    
         if ipos==-1:
            print('NOT FOUND',  nstr, 'in', astr)
    
         else:
            print('FOUND',nstr,'in', astr)
            print('FIRST OCCURING POSITION IS: ', npos)
            print('FIRST OCCURING INDEX POSITION IS: ', ipos)
            print('TOTAL NO. OF OCCURANCE OF SUBSTRING: ', neto)
            print('Text Count: ', len(astr))
            print(LTlist)
            
            
    
    elif main=='Whitespace Remover' or main=='whitespace remover' or main=='wr' or main=='WR' or main=='3':
         lstar=input('Data On which Whitespace(s) is/are to be removed: ' )
         hstar=input('On side: ')
         #Remove Whitespace on side: left, enter 'l'; right, enter 'r'; all sides, enter 'lr'
         if hstar=='l':
             estar=lstar.lstrip()
             print(estar)
         elif hstar=='r':
             estar=lstar.rstrip()
             print(estar)
         elif hstar=='lr':
             estar=lstar.strip()
             print(estar)
         else:
             print('Please Enter A Valid Input')
    
    elif main=='Word Frequency':
         wfinp=input('Enter Text:\n')
         wdict=dict()
         w1list=wfinp.split()
         for word in w1list:
             wdict[word]=wdict.get(word,0) + 1
         print('\nWord Frequency:')
         wseries=pd.Series(wdict)
         print(wseries)

    #Continue next command from here.
    
    else:
         print('Invalid Command Request.')

VertigoZString()
