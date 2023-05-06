# Python
## Task 1: FIZZBUZZ
```py
for i in range(1,51):
    if i%3==0 and i%5==0:
        print("FIZZBUZZ")
    elif i%5==0:
        print("BUZZ")
    elif i%3==0:
        print("FIZZ")
    else :
        print(i)    
  ```    
 

The FizzBuzz problem is a common programming task where you need to print numbers from 1 to 50, but for multiples of 3, you print "FIZZ" instead of the number, for multiples of 5, you print "BUZZ", and for numbers that are multiples of both 3 and 5, you print "FIZZBUZZ". Here's the solution in Python:


Output:
`
1
2
FIZZ
4
BUZZ
FIZZ
7
8
FIZZ
BUZZ
11
FIZZ
13
14
FIZZBUZZ
16
17
FIZZ
19
BUZZ
FIZZ
22
23
FIZZ
BUZZ
26
FIZZ
28
29
FIZZBUZZ
31
32
FIZZ
34
BUZZ
FIZZ
37
38
FIZZ
BUZZ
41
FIZZ
43
44
FIZZBUZZ
46
47
FIZZ
49
BUZZ
`

In the above solution, we iterate over the range from 1 to 50 using a `for` loop. We use the modulus operator `%` to check if the number is divisible by 3, 5, or both. Based on the conditions, we print "FIZZ", "BUZZ", "FIZZBUZZ", or the number itself.
