% Programming quizz
% Christophe@Pallier.org
% 2013 Sep, 1



(@) What does the following program do?

```python
if 2 + 2 == 5: 
	print("Sorry!")
else:
	print("Bonjour!")
```

#ifdef ANSWERS

*Answer:* It prints 'Bonjour!'

- - -

#endif

(@) What does the following program do?

```python
state = 1
for i in range(100):
	if (state==1): 
		print('A')
	else:
		print('B')
	state = 1 - state
```


#ifdef ANSWERS

*Answer:* It prints a sequence of alternating As and Bs.	 

- - -

#endif


(@) What does the following program do?

```python
n = 50
guess = input('Your guess?')

while guess != n:
	if guess > n:
		print('Too high!')
	if guess < n:
		print('Too low!')
	guess = input('New guess?')

print("Correct!")
```

#ifdef ANSWERS

*Answer:* It asks the user to guess the number fifty, helping him by telling when his guess os too large or to small.

- - -

#endif



(@) What does the following program do?

```python
def prod(x):
	p = 1
	for e in x:
		p = p * e
	return p
	
prod([4, 5, 6])
```

#ifdef ANSWERS

*Answer:* It prints the product of 4, 5 and 6, that is, 120

- - -

#endif



(@) Write a program that prints the squares of the first 100 non null integers 

#ifdef ANSWERS

*Answer 1:* 

```python
for i in range(1,101):
	print i*i
```

*Answer 2 (more pythonic):* 

```python
print( [i*i for i in range(1, 101)] )
```

- - -

#endif



(@) Given a variable n, compute the sum of the first n integers

#ifdef ANSWERS

*Answer 1:*

```python
s = 0
for i in range(1, n+1):
	s = s + i
print(s)
```

*Answer 2:*

```python
sum([i for i in range(1, n+1)])
```

- - -

#endif



(@) Write a program that computes the sum of all integers less or equal to n, except multiples of 10.


#ifdef ANSWERS

*Answer 1:*

```python
n = 1000
s = 0
for i in range(n+1):
	if (i % 10) != 0:
		s = s + i
print(s)
```

*Answer 2:*

```python
 sum([x for x in range(1001) if x%10 != 0])
```

- - -

#endif



(@) Write a function that returns the product of all integers between 1 and n (is is called a factorial).

#ifdef ANSWERS



*Answer 1:*

```python
def fact(n):
	p = 1
	for x in range(1,n+1):
		p = x * p
	return p

print(fact(5))
```

*Answer 2:*

```python
def fact(n):
	if n <= 1:
		return 1
	else:
		return n * fact(n - 1)

print(fact(5))
```


- - -

#endif



(@) Write a program that returns the 'nth' [Fibonacci number](Fibonacci numbers) F(0) = 0; F(1)=1; F(n) = F(n-1) + F(n-2) 


#ifdef ANSWERS

*Answer 1:*

```python
def fib(n):
	return n if n < 2 else fib(n-2) + fib(n-1)

print(fib(30))
```

Yet, read [ http://en.literateprograms.org/Fibonacci_numbers_%28Python%29 ]

- - -

#endif


(@) Compute the estimate of pi using the first 1000000 terms of [Wallis formula](http://en.wikipedia.org/wiki/Wallis_product). 


#ifdef ANSWERS

```python
p = 1.0
for i in range(1, 1000001):
	p = p * 4 * i * i /(4* i *i - 1)
print(2*p)
```

- - -

#endif

(@) Estimate pi/4, the area of a quarter unit circle, using Monte Carlo simulations (taking random points in the (0,1)x(0,1) square and checking if they are in the unit circle (use the function `random.uniform`)


#ifdef ANSWERS

*Answer 1:*


```python
import random
p = 0
n = 1000000
for i in range(n):
	x = random.uniform(0,1)
	y = random.uniform(0,1)
	if (x*x+y*y)<1:
		p = p + 1
print(4*(1.0*p)/n)
```

*Answer 2:*

```python
import numpy as np
n = 1000000
x = np.random.uniform(0,1,n)
y = np.random.uniform(0,1,n)
print(4*np.mean(x*x + y*y < 1.0))
```

- - -

#endif

(@) Given a list, return the list that has the same elements in reversed order

#ifdef ANSWERS

*Answer 1:*

```python
def rev(l):
	r = []
	for i in range(len(l)):
		r.append(l[len(l)-i-1])
	return r
	
print(rev(['a', 'b', 'c', 'd']))
```

*Answer 2:*

```python
def rev(l):
	r = l
	r.reverse()
	return r
	
print(rev(['a', 'b', 'c', 'd']))
```
 
- - -

#endif

(@) Given a list, return its unique elements (remove repeations) 

#ifdef ANSWERS


```python
def unique(l):
	u = []
	for x in l:
		if not(x in u):
			u.append(x)
	return u
```
	


- - -

#endif


(@) Compute the frequency of occurences of words in a text file.


(@) Display all anagrams (permutations of letters) of a given word.


(@) Simulate sampling from a urn containing a given proportion of white balls. Display the histogram of the proportions in samples.


(@) Read a file containing two columns, the first containing labels and the second numbers. Compute the means associated to each label.


(@) Draw a cloud of dots at random locations on the screen (suppose you have a function dot((x,y), color)) to display a dot of color color at location (x,y) on the screen; no initialisation code)


(@) Draw a disk that moves and bounces on the screen's border.








