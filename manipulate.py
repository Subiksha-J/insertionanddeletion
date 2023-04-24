def insert(l):
        y=int(input("Element to insert "))
        z=int(input("Position to insert "))
        if(z<len(l)):
         l.append(0)
         for i in range(len(l),z,-1):
            l[i-1]=l[i-2]
         l[z-1]=y
        else:
            l.append(y)
        print(l)
        
def delete(l):
    y=int(input("Element to be deleted "))
    n=len(l)
    c=0
    while(n>0):
        if(l[n-1]==y):
            l.remove(l[n-1])
            n=n-1
        else:
            n=n-1
            pass
    if(c>0):
        print(l)
    else:
        print("Element not found")
        print(l)
def manipulate(l):
 x=int(input("1.Insert\n2.Delete\n3.Exit\nEnter your option "))
 while(x>0):
    if(x==1):
        insert(l)
        x=int(input("1.Insert\n2.Delete\n3.Exit\nEnter your option "))
    elif(x==2):
        delete(l)
        x=int(input("1.Insert\n2.Delete\n3.Exit\nEnter you option "))
    elif(x==3):
        break

n=int(input())
l=list()
for i in range(n):
    a=int(input())
    l.append(a)
manipulate(l)

