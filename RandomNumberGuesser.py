import random
ranum = random.randint(1,100)
print('Starting Number: ', ranum)
missed_nums = []
def numberguess():
    num = random.randint(1,100) 
    if  num == ranum:
        print('Correctly Guessed Number: ', num)
        print('Missed Numbers: ', missed_nums) 
    elif num in missed_nums:
        numberguess()
    else:
        missed_nums.append(num)
        numberguess()
numberguess()