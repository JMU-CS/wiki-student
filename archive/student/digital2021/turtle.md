# Python Turtle Art, DIGITAL 2021

[Python Turtle Sandbox](http://pythonsandbox.com/turtle)

``` py
## square version 1 (algorithm)

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)


## square version 2 (iteration/loop)

for i in range(4):
    t.forward(100)
    t.right(90)


## square version 3 (abstraction/function)

def square(size):
    for i in range(4):
        t.forward(size)
        t.right(90)

t.speed(0)
for i in range(10):
    square(i*10)


## square version 4 (recursion)

def square(size):
    for i in range(4):
        t.forward(size)
        t.right(90)

def fractal(size):
    if size > 2:
        square(size)
        for i in range(4):
            fractal(size/3)
            t.forward(size)
            t.right(90)

t.speed(0)
fractal(200)


## tree fractal

def tree(size):
    if size < 10:
        t.forward(size)
        t.backward(size)
        return
    t.forward(size)
    t.left(30)
    tree(size*0.7)
    t.right(60)
    tree(size*0.7)
    t.left(30)
    t.backward(size)

t.pencolor("green")
t.setheading(90)
t.speed(0)
tree(100)


## fern fractal

def fern(size):
    if size > 3:
        t.forward(size)
        t.right(95)
        fern(size*0.4)
        t.left(190)
        fern(size*0.4)
        t.right(100)
        fern(size*0.8)
        t.left(5)
        t.backward(size)

t.pencolor("green")
t.speed(0)
fern(50)


## snowflake fractal

def snowflake(size):
    if size < 10:
        t.forward(size)
    else:
        snowflake(size/3)
        t.left(60)
        snowflake(size/3)
        t.right(120)
        snowflake(size/3)
        t.left(60)
        snowflake(size/3)

t.pencolor("blue")
t.speed(0)
t.setheading(90)
for i in range(3):
    snowflake(100)
    t.right(120)


## pythagoras triangle fractal

from math import sqrt

def pythagoras(size):
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()
    if size > 5:
        s = size*sqrt(2)/2
        t.forward(size)
        t.left(45)
        pythagoras(s)
        t.right(90)
        t.forward(s)
        pythagoras(s)
        t.backward(s)
        t.left(45)
        t.backward(size)

t.speed(0)
t.setheading(90)
pythagoras(50)


## sierpinski triangle fractal

from math import sqrt

def sierpinski(x, y, size):
    if size < 10:
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.begin_fill()
        for i in range(3):
            t.forward(size)
            t.left(120)
        t.end_fill()
    else:
        h = sqrt(3) * size / 4
        sierpinski(x,       y,  size/2)
        sierpinski(x+size/2,y,  size/2)
        sierpinski(x+size/4,y+h,size/2)

t.speed(0)
sierpinski(-100,-100,200)
```
