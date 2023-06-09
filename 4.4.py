import math

#Aufgabe a

def maxNumber(num1, num2, num3):
    return max(int(num1), int(num2), int(num3))

print(maxNumber(1, 17, 10))

#Aufgabe b

def Summe(values):
    return sum(values)

print(Summe([1, 2, 3, 4, 5, 6]))

#Aufgabe c
def umgekehrt(word):
    i = len(word)
    backwards = ''
    
    while i > 0:
        backwards += word[i-1]
        i -= 1
    
    return backwards
    
print(umgekehrt('Steven'))

#Aufgabe d

def Fakultät(num):
    if int(num) > 0:
        return math.factorial(num)
    else:
        print("Bitte eine positive Zahl angeben")

print(Fakultät(23))

#Aufgabe e

def ganzeZahlen(nums):
    list = []
    
    for i in nums:
       if i % 2 == 0:
           list += [i]
    
    return list
            
        
print(ganzeZahlen([1, 2, 4, 6, 7, 10, 14, 15, 16, 17, 18]))

#Aufgabe f

def Palindrom(word):
    i = len(word)
    backwards = ''
    
    while i > 0:
        backwards += word[i-1]
        i -= 1
    
    if backwards.lower() == word.lower():
        return True
    else:
        return False
    
print(Palindrom('Emily'))

#Aufgabe g

def Dreieck(n):
    nZeile = ''
    k = n
    while k >= 0:
        nZeile += str((math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))) + " "
        k -= 1
    return nZeile
        
print(Dreieck(7))
        

#Aufgabe h

def Wörter(words):
    sortedList = sorted(words.split('-'))
        
    return '-'.join(sortedList)
    
print(Wörter('beta-alpha-delta-gamma-epsilon'))