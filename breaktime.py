import time
import webbrowser

n = 1
print("This program started on "+time.ctime())
while n <= 3:	 
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=oX6_v3xuuk8")
	n = n + 1
