#question 2.1

numberList = []
a = 0
while a<21:
    numberList.append(a)
    a += 1
print(numberList)

''' 
i got the error "Traceback (most recent call last):
  File "/Users/thomasjumper/Desktop/pythondecal_hw/homework4.py", line 14, in <module>
    numberList.append(0, a)
TypeError: list.append() takes exactly one argument (2 given) " because i accidentally put 0, a in the append because i thought it was a different function so i just replaced it with a

also got a second error because my while function kept on going because i accidentally put =+ instead of += so i just changed it
'''
#question 2.2

def squareList(list):
    newlist = []
    for i in list:
        a = i**2
        newlist.append(a)
    return newlist
secondnumberList = squareList(numberList)
print(secondnumberList)

#question 2.3

def slicedList(someList):
    slicing = slice(15)
    print(someList[slicing])

slicedList(secondnumberList)

#question 2.4

def stridedList(aList):
    print(aList[4::5])

stridedList(secondnumberList)

#question 2.5

