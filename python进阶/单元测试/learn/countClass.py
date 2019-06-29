class Count(object):
   def add(self,x,y):
     x+=y
    
     return x
   def sub(self,x,y):
     x-=y
    
     return x 
if __name__ == "__main__":
    c=Count()
    print(c.add(4,5))