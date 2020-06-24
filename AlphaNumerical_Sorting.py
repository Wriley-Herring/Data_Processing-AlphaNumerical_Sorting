'''

@author: wrileyherring
'''

#O(n) sorting algorithm

def sortA(filename):
    
    #open input file
    file = open(filename,'r')
    
    #read in file
    lines = file.readlines()
    
    #encode dictionary 
    encodeList = {
        
        'a': '01',
        'b': '02',
        'c': '03',
        'd': '04',
        'e': '05',
        'f': '06',
        'g': '07',
        'h': '08',
        'i': '09',
        'j': '10',
        'k': '11',
        'l': '12',
        'm': '13',
        'n': '14',
        'o': '15',
        'p': '16',
        'q': '17',
        'r': '18',
        's': '19',
        't': '20',
        'u': '21',
        'v': '22',
        'w': '23',
        'x': '24',
        'y': '25',
        'z': '26'
        }
    # decode list
    decodeList = {
        
        '01': 'a',
        '02': 'b',
        '03': 'c',
        '04': 'd',
        '05': 'e',
        '06': 'f',
        '07': 'g',
        '08': 'h',
        '09': 'i',
        '1': 'a',
        '2': 'b',
        '3': 'c',
        '4': 'd',
        '5': 'e',
        '6': 'f',
        '7': 'g',
        '8': 'h',
        '9': 'i',
        '10': 'j',
        '11': 'k',
        '12': 'l',
        '13': 'm',
        '14': 'n',
        '15': 'o',
        '16': 'p',
        '17': 'q',
        '18': 'r',
        '19': 's',
        '20': 't',
        '21': 'u',
        '22': 'v',
        '23': 'w',
        '24': 'x',
        '25': 'y',
        '26': 'z'
        }
    
    #set maximum size
    k = lines.pop(0)
    
    #extract max word size
    k = k[-4:-1]
    
    #set max size
    maxValue = ''
    for letter in k:
        
        maxValue = maxValue + encodeList[letter.lower()]
        
    #initialize words list
    wordsArray = [0] * (int(maxValue)+1)
    words =[]
    
    #fill word list with values and remove line spacing
    for line in lines:
        line = line.rstrip()
        words.append(line)
    
    #join into master string     
    words = " ".join(words)
    
    #split string into list of words
    words = words.split(" ")
    
    
    #encode words and mark in array if present
    for word in words:
        
        if len(word) > 0:
            encodeValue = ''
        
            for letter in word:
            
                encodeValue += encodeList[letter.lower()]
            
            #add cushion 00's
            if len(encodeValue) == 2:
                encodeValue += '0000'
            elif len(encodeValue) == 4:
                encodeValue += '00'
            else:
                pass
            wordsArray[int(encodeValue)] += 1
            
    #initialize sorted list 
    sortedList =[]
   
    
    i = 0 
    #parse through array
    for index in range(int(maxValue)+1):
        
        
        
        if wordsArray[index] != 0:
            
            #decode word size if 5 digits
            if len(str(index)) == 5:
                
                
                for j in range(wordsArray[index]):
                    
                    
                    index = str(index)
                    
                    #decode first letter
                    decodedWord = ''
                    letterIn = index[0]
                    decodedLetter = decodeList[letterIn] 
                    decodedWord += decodedLetter
                    k = 1
                    
                    #decode remaining letters 
                    for num in range(2):
                            
                            
                            
                        letterIn = index[k] + index[k + 1]
                        if letterIn == '00':
                            pass
                        else:
                            decodedLetter = decodeList[letterIn]
                                
                            decodedWord += (decodedLetter)
                                
                            k+=2
                    
                    #add line spacing every 10 words      
                    if i > 10:
                                   
                        sortedList.append(decodedWord)
                        sortedList.append('\n') 
                        i = 1
                        
                    else:
                        sortedList.append(decodedWord)      
            
                    i += 1
            # decode words that are six digits long
            else:
                
                for j in range(wordsArray[index]):
                    
                    index = str(index)
                    
                    #parse through three sets of codes 
                    k = 0
                    decodedWord = ''
                    for num in range(3):
                        
                        #check if word has a cushion    
                        letterIn = index[k] + index[k + 1]
                        if letterIn == '00':
                            pass
                        else:
                            decodedLetter = decodeList[letterIn]
                                
                            decodedWord += (decodedLetter)
                                
                            k+=2
                    
                    #add line spacing every 10 characters          
                    if i  == 10:
                                  
                        sortedList.append(decodedWord)
                        sortedList.append('\n') 
                        i = 1
                    else:
                        sortedList.append(decodedWord) 
                            
                    
                    i += 1
    
    #join sorted list into string 
    sortedList = " ".join(sortedList)
    
    #create output file
    outFile = filename.replace("in","out")
    outFile = outFile.replace(".txt","a.txt")
    
    #write sorted list to output file
    out = open(outFile,"w+")
    out.write(sortedList)

    
# O(n^2) algorithm
def sortB(filename):
    
    #open input file
    file = open(filename,'r')
    
    #read in file
    lines = file.readlines()
    
    #encode dictionary 
    encodeList = {
        
        'a': '01',
        'b': '02',
        'c': '03',
        'd': '04',
        'e': '05',
        'f': '06',
        'g': '07',
        'h': '08',
        'i': '09',
        'j': '10',
        'k': '11',
        'l': '12',
        'm': '13',
        'n': '14',
        'o': '15',
        'p': '16',
        'q': '17',
        'r': '18',
        's': '19',
        't': '20',
        'u': '21',
        'v': '22',
        'w': '23',
        'x': '24',
        'y': '25',
        'z': '26'
        }
    # decode list
    decodeList = {
        
        '01': 'a',
        '02': 'b',
        '03': 'c',
        '04': 'd',
        '05': 'e',
        '06': 'f',
        '07': 'g',
        '08': 'h',
        '09': 'i',
        '1': 'a',
        '2': 'b',
        '3': 'c',
        '4': 'd',
        '5': 'e',
        '6': 'f',
        '7': 'g',
        '8': 'h',
        '9': 'i',
        '10': 'j',
        '11': 'k',
        '12': 'l',
        '13': 'm',
        '14': 'n',
        '15': 'o',
        '16': 'p',
        '17': 'q',
        '18': 'r',
        '19': 's',
        '20': 't',
        '21': 'u',
        '22': 'v',
        '23': 'w',
        '24': 'x',
        '25': 'y',
        '26': 'z'
        }
    
    #set maximum size
    k = lines.pop(0)
    
    #extract max word size
    k = k[-4:-1]
    
    #set max size
    maxValue = ''
    for letter in k:
        
        maxValue = maxValue + encodeList[letter.lower()]
        
    #initialize words list
    wordsArray = [0] * (int(maxValue)+1)
    words =[]
    
    #fill word list with values and remove line spacing
    for line in lines:
        line = line.rstrip()
        words.append(line)
    
    #join into master string     
    words = " ".join(words)
    
    #split string into list of words
    words = words.split(" ")
    
    #unsorted list
    sortList = []
    
    #encode words and mark in array if present
    for word in words:
        
        if len(word) > 0:
            encodeValue = ''
        
            for letter in word:
            
                encodeValue += encodeList[letter.lower()]
            
            
            if len(encodeValue) == 2:
                encodeValue += '0000'
            elif len(encodeValue) == 4:
                encodeValue += '00'
            else:
                pass
            sortList.append(int(encodeValue))
   
    listLength = len(sortList)
    
   #traverse array element by element
    for i in range(listLength-1):
        #move through elements for every element
        for j in range(listLength -i -1):
            
            #if element is found to be greater than thr next
            #swap the elements
            if sortList[j] > sortList[j+1]:
                
                sortList[j], sortList[j+1] = sortList[j+1], sortList[j]
    
    
    #initialize sorted list
    sortedList = []
    
    
    # decode each word
    i = 0
    for word in sortList:
        
        #decode word that contains 5 digits
        if len(str(word)) == 5:

            word = str(word)
                    
            #decode first letter
            decodedWord = ''
            letterIn = word[0]
            decodedLetter = decodeList[letterIn] 
            decodedWord += decodedLetter
            k = 1
                    
            #decode remaining letters 
            for num in range(2):
                            
                            
                            
                letterIn = word[k] + word[k + 1]
                if letterIn == '00':
                    pass
                else:
                    decodedLetter = decodeList[letterIn]
                                
                    decodedWord += (decodedLetter)
                                
                    k+=2
             
             
             #add line spacing every 10 words               
            if i == 10:
                         
                sortedList.append(decodedWord)
                sortedList.append('\n') 
                i = 0
                
            else:
                sortedList.append(decodedWord)      
        
            
        else:
            
            #decode word that has 6 digits
            
            word = str(word)
            k = 0
            decodedWord = ''
            for num in range(3):
                             
                letterIn = word[k] + word[k + 1]
                
                #check if word has a cushion
                if letterIn == '00':
                    pass
                else:
                    decodedLetter = decodeList[letterIn]
                                
                    decodedWord += (decodedLetter)
                                
                    k+=2
            
             #add line spacing every 10 words                   
            if i == 10:          
                sortedList.append(decodedWord)
                sortedList.append('\n')
                i = 1
                
            else:
                sortedList.append(decodedWord) 
                            
        i += 0
                        
            
               
    #join sorted list into string 
    sortedList = " ".join(sortedList)
    
    #create output file
    outFile = filename.replace("in","out")
    outFile = outFile.replace(".txt","b.txt")
    
    #write sorted list to output file
    out = open(outFile,"w+")
    out.write(sortedList)                
        
if __name__ == '__main__':
    
    #sort in10.txt with sortA
    sortA("in_abc10.txt")
    
    #sort in100.txt with sortA
    sortA("in_abc100.txt")

    #sort in10.txt with sortB
    sortB("in_abc10.txt")
    
    #sort in100.txt with sortB
    sortB("in_abc100.txt")
