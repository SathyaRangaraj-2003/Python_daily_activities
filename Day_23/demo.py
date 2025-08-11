# print(type(5)) #=>integer class 5 is object

class Dog:
    tricks = []
    def add(self,t):
        self.tricks.append(t)
d1=Dog()
d2=Dog()
d1.add("sit")
d2.add("rollover")
print(d1.tricks)
print(d2.tricks)