import turtle
import time
risotto=turtle.Pen()
risotto.speed(0)
numberofdacircles=int(turtle.numinput("number of da circles","how many in your risotto",6))
for x in range(numberofdacircles):
    risotto.circle(100)
    risotto.left(360/numberofdacircles)
time.sleep(5)