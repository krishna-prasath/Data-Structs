lt=[]
def push(a):
    lt.append(a)
def pop():
     if len(lt)!=0:
        lt.remove(lt[-1])
b=int(input("no of elem to be pushed"))
for i in range(b):
    a=int(input("enter the elem to be pushed"))
    push(a)
c=int(input("no of elem to be poped"))
for i in range(c):
   pop()
  
print(lt)
