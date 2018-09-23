#stack datastructure python

class stack():
 def __init__(self):
  self.i = -1
  self.a = []

 def push(self, k):
   self.i+=1
   self.a.append(k)
   print(self.a)

 def pop(self):
    if self.i ==-1:
     temp = "empty"
    else:
     temp = self.a[self.i]
     del self.a[self.i]
     self.i-=1
    print(temp,self.a)

 def print(self):
     while self.i > -1:
      self.pop()



a = stack()
a.push(10)
a.push(15)
a.push(23)
a.push(1)
# a.print()
a.pop()
