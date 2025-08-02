#activity_01
#fibonacci()

def fibonacci():
	f = 0
	s = 1
	yield f
	yield s
	while True:
		t = f + s
		yield t
		f = s
		s = t
fib = fibonacci()
print(next(fib))
print(next(fib))
print(next(fib))
