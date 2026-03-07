Recursion in Python

1. What is Recursion?
  Recursion is a programming technique where a function calls itself to solve a  prolem. Instead of solving the whole problem at once, it solves smaller version of the same problem.

  Example:
  function -> calls itself -> calls itself -> stops when condition reached

2. Components of Recursion
  Every recursive function has two parts.
  Base case
    The condition where recursion stops.
  Recursive case
    The part where the function calls itself.

3. Factorial using recursion:
  Formula:
  n! = n x (n-1)!
  Example:
  5! = 5 x 4 x 3 x 2 x 1
  Code:
  def factorial(n):
    if n==1:
      return 1
    else:
      return n*factorial(n-1)
  num=int(input("Enter number: "))
  print("Factorial: ",factorial(num))

4. Fibonacci Series using Recursion:
  Rule:
  F(n)=F(n-1)+F(n-2)
  Sequence:
  0 1 1 2 3 5 8 13
  Code:
  def fibonacci(n):
    if n<=1:
      return n
    else:
      return fibonacci(n-1) + fibonacci(n-2)
  n=int(input("Enter position: "))
  print("Fibonacci number: ",fibonacci(n))

5. Sum of Natural Numbers using Recursion:
  Example:
  1+2+3+4+5
  Code:
  def sum_numbers(n):
    if n==0:
      return 0
    else:
      return n+sum_numbers(n-1)
   num=int(input("Enter number: "))
   print("Sum: ",sum_numbers(num))

6. Reverse a String using Recursion
  Code:
  def reverse_string(text):
    if len(text) ==0:
      return text
    else:
      return reverse_string(text[1:])+text[0]
   word=input("Enter  text: ")
   print("Reversed: ",reverse_string(word))

7. Why Recursion is Important?
   Recursion is widely used in:
   -> tree traversal
   -> graph algorithms
   -> divide and conquer algorithms
   -> sorting algorithms
   -> searching algorithms
   Example:
   -> quick sort
   -> merge sort
   -> binary search
