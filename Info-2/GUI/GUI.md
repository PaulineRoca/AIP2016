% Graphical interfaces
%
%


# Tk

## Example 1

```python
from Tkinter import *

def hello(): 
	print 'Hello, world'

win = Tk() 
win.title('Hello, Tkinter! ')
win.geometry('200x100') 

btn = Button(win, text='Hello ', command=hello)
btn.pack(expand=YES, fill=BOTH)

mainloop()
```

## Example 2: A converter 

from http://www.tkdocs.com/tutorial/firstexample.html

See converter.py

## Example 3: Oscilloscope

Run dualscope.py

(you need the module PyQt4.Qwt5 which is difficult to install)


## Pygame

Illusory motion



