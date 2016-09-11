% 
% Info-2 / Lecture 3. 
%


# modules

Python's language can be augmented by new functions and object from modules. They are imported with the function `import`.

Example 1 (in `ipython` command line):

    import math 
	math.sin(1.3)

Example 2:

	import numpy as np
	import matplotlib.pyplot as plt
	plt.plot(np.sin(np.linspace(0, 6*np.pi, 500)))
	plt.show()

Example 3: 

	import random
	random.<TAB>
	random?
	

Note: It is easy to create one's own module: having a file `mymodule.py` in the current directory, it is possible to use `import mymodule`.

Have a look at the `turtle` module https://docs.python.org/2/library/turtle.html

EX: Write the following program in atom, save it and execute it

	import turtle
	turtle.forward(100)
	turtle.left(120)
	turtle.forward(100)
	turtle.left(120)
	turtle.forward(100)
	turtle.left(120)
	turtle.mainloop()
	
Modify this program to display a regular polygon with 'n' sides


# A few useful functions on strings

	a = "Bonjour Jean"
	len(a)
	a[2:4]
	
	a.replace("Jean", "Marc")
	a
	b = a.replace("Jean", "Marc")
	
	a = "caillou, genou, bijou"
	a.split(",")
	
	b= ['alpha', 'beta', 'gamma']
	";".join(b)

# 

Ex: 

