# This script prints the integers from 1 to 100. For multiples of three print “Fizz” instead , and for the multiples
# of five print “Buzz”. For numbers which are multiples of both print “FizzBuzz”

for i in range (1, 101):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else: print(i)