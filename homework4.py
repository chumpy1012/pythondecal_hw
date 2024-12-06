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

def slicedList(list):
    slicing = slice(15)
    print(list[slicing])

slicedList(secondnumberList)

#question 2.4

def stridedList(list):
    print(list[4::5])

stridedList(secondnumberList)

#question 2.5

def negativelist(list):
    print(list[::-3])

negativelist(secondnumberList)

#question 3.1

matrixlist = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list2D = []
def create_2D_list(list):
    a = 1
    while a < 26:
        list.append(a)
        a+=1
    for number in list[0:5]:
        list1.append(number)
    for number in list[5:10]:
        list2.append(number)
    for number in list[10:15]:
        list3.append(number)
    for number in list[15:20]:
        list4.append(number)
    for number in list[20:25]:
        list5.append(number)
    list2D.append(list1)
    list2D.append(list2)
    list2D.append(list3)
    list2D.append(list4)
    list2D.append(list5)
    print(list2D)
create_2D_list(matrixlist)

#question 3.2

def questionreplace(list):
    for numberedlist in list:
        for index in range(len(numberedlist)):
            a = numberedlist[index]%3
            if a == 0:
                numberedlist[index] = "?"
    print(list)
                
questionreplace(list2D)

#question 3.3
'''
emptysumlist = []
questionlist = questionreplace(list2D)
print(questionlist)

def sumlist(list):
    for minilist in list:
        for number in minilist:
            if number != "?":
                emptysumlist.append(number)
    sum(emptysumlist)
sumlist(questionlist)
'''