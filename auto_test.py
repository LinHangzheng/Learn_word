#coding=utf-8
import xlrd 
import sys
import random

list_n = 40
not_in_xlsx = 6

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

vocabulary_array = {}

data = xlrd.open_workbook('E:/TOEFL/vocabulary.xlsx')
for sheet_n in range(len(data.sheets())):   
    sheet = data.sheets()[sheet_n]
    words = sheet.col_values(1)[1:]
    paraphrase = sheet.col_values(2)[1:]
    voc = []
    for i in range (len(words)):
        voc.append((words[i],paraphrase[i],0))
    vocabulary_array[sheet_n+not_in_xlsx] = voc
    
while (1):
    while (1):
        list_n = input('List = (press \'q\' to quit)')
        assert (not list_n == 'q'), 'quit'
        if (not is_number(list_n)):
            print ('please enter a number ')
            continue
        if (int(list_n)<7 or int(list_n)>40):
            print('please enter a number between 7-40')
            continue
        break
    list_n = int(list_n) -1
    List = vocabulary_array[list_n]
    random.shuffle(List)
    i = 0
    while i <len(List):
        print  (List[i][0])
        know =  input()
        
        # if you don't konw the word
        if (know == '1'):
            List[i]= (List[i][0],List[i][1],List[i][2]+1)
            print (List[i][1],' ',List[i][2])
            
        # if you know the word
        elif (know == '0'):
            print (List[i][1],' ',List[i][2])
            
        # if you find the last check is wrong, press d and set the last 
        # word as unknow
        elif (i >0 and know == 'd'):
            List[i-1]= (List[i-1][0],List[i-1][1],List[i-1][2]+1)
            print (List[i-1][0],' ', List[i-1][1],' ',List[i-1][2])   
            i = i-1
            
        # press q to quit the test
        elif (know == 'q'):
            break
        else:
            i -=1
        i +=1

    List = sorted(List, key=lambda x:x[2],reverse=True)

    count = 1
    while (not List[0][2] == 0):
        if (know == 'q'):
            break
        count +=1
        print ('\n========== The %i round =========='%count)
        i = 0
        while i <len(List):
            if List[i][2] == 0:
                break
            print  (List[i][0])
            know = input ()
            if (know == '1'):
                List[i]= (List[i][0],List[i][1],List[i][2]+1)
                print (List[i][1],' ', List[i][2])
            elif (know == '0'):
                List[i] = (List[i][0],List[i][1],List[i][2]-1)
                print (List[i][1],' ', List[i][2])
            elif (i >0 and know == 'd'):
                List[i-1]= (List[i-1][0],List[i-1][1],List[i-1][2]+2)
                print (List[i-1][0],' ',List[i-1][1],' ',List[i-1][2])
                i = i-1
            elif (know == 'q'):
                break
            else:
                i -=1
            i +=1
        List = sorted(List, key=lambda x:x[2],reverse=True)
