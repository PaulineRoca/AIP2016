%
% Self-Quizz
%


(@) What does the following program do?

```python
if 2 + 2 == 5: 
	print("Sorry!")
else:
	print("Bonjour!")
```


(@) What does the following program do?

```python
state = 1
for i in range(100):
	if (state==1): 
		print 'A',
	else:
		print 'B',
	state = 1 - state
```

	 

(@) What does the following program do?

```python
n = 50
guess = input('Your guess?')

while guess != n:
	if guess > n:
		print('Too large!')
	if guess < n:
		print('Too Small!')
	guess = input('New guess?')

print("Correct!")
```


(@) What does the following program do?

```python
def prod(x):
	p = 1
	for e in x:
		p = p * e
	return p
	
prod([4, 5, 6])
```
	

(@) Write a program that prints the squares of the first 100 integers 


(@) Given a variable n, compute the sum of the first n integers


(@) Write a program that computes the sum of all the multiples of 7 below 1000


(@) Write a function that returns the product of all integers between 1 and n (is is called a factorial).


(@) Write a program that returns the 'nth' [Fibonacci number](Fibonacci numbers) F(0) = 0; F(1)=1; F(n) = F(n-1) + F(n-2) 


(@) Compute the estimate of pi using the first 1000 terms of [Wallis formula](http://en.wikipedia.org/wiki/Wallis_product). 


(@) Estimate pi using Monte Carlo simulations (taking random points in the (0,1)x(0,1) square and checking if they are in the unit circle (use the function `random.uniform`)


(@) Given a list, return the list that has the same elements in reversed order


(@) Given a list, return its unique elements (remove repeations) 


(@) Compute the frequency of occurences of words in a text file.


(@) Display all anagrams (permutations of letters) of a given word.


(@) Simulate sampling from a urn containing a given proportion of white balls. Display the histogram of the proportions in samples.


(@) Read a file containing two columns, the first containing labels and the second numbers. Compute the means associated to each label.


(@) Draw a cloud of dots at random locations on the screen (suppose you have a function dot((x,y), color)) to display a dot of color color at location (x,y) on the screen; no initialisation code)


(@) Draw a disk that moves and bounces on the screen's border.








