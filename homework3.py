#question 1

'''def compute_power(x,y):
    while y>0:
        x = x
        print(x)
        y-=1

compute_power(2,3)
'''
#question 2

readings = [15, 14, 17, 20, 23, 28, 20]
def temperatureRange(readings):
    a = min(readings)
    b = max(readings)
    print((a, b))

temperatureRange(readings)

#question 3

def isWeekend(day):
    day = [1,2,3,4,5,6,7]
    for number in day:
        if number>5:
            print("True")
        else:
            print("False")
    
isWeekend(5)

#question 4

def fuel_efficiency(distance, fuel):
    efficiency = distance/fuel
    print(efficiency)

fuel_efficiency(70, 21.5)

#question 5

def decodeNumbers(n):
    last_digit = n%10
    n = n/10
    n = int(n)
    print(str(last_digit) + str(n))

decodeNumbers(12345)

#question 6

#6.1

nums = [2024, 98, 131, 2, 3, 72]
'''def find_min_with_for_loop(nums):
    for number in nums:
        
'''

#6.2

'''def find_min_with_while_loop(numberlist):
    while 

'''
#question 7



text = "UC Berkeley, founded in 1868!"

def vowel_and_consonant_count(text):
    a = 0
    b = 0
    consonants = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for letter in text:
        if letter.isalpha() == True:
            print(letter)
            for consonant in consonants:
                if letter == consonant:
                    a += 1
                else:
                    b += 1
        else:
            b -= 1
    vowel_and_consonant_tuple = (a,b) 
    print(vowel_and_consonant_tuple)
vowel_and_consonant_count(text)
