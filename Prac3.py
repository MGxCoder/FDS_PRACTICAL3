bname=[]
cost=[]
print("Enter Name Of Books && Cost Hit Enter 2 times ")
while True:
    data=input()
    if data=="":
        break
    else:
        data=data.split()
        bname.append(data[0])
        cost.append(int(data[1]))
       
       
print(bname)
print(cost)

def dup():
    d =len(data)
    print("After Duplicate name deleted")
    for i in range (0,d):
        for j in range(i+1,d):
            if bname[i]==bname[j]:
                del bname[j]
                del cost[j]
            d=len(bname)

    for i in range(0,len(bname)):
        print(bname[i],"",cost[i])
    print()


def Sorting():
    c=len(cost)
    for i in range(0,c):
        for j in range (i+1,c):
            if cost[i]>cost[j]:
                temp=bname[i]
                temp1=cost[i]
                bname[i]=bname[j]
                cost[i]=cost[j]
                bname[j]=temp
                cost[j]=temp1
    print("After Sorting")
    for i in range(0,len(bname)):
        print(bname[i],"",cost[i])
    print()
 
def count():
    count=0
    c=len(cost)
    print("List Of book having cost greater  than 500 ")
    for i in range(0,c):
        if cost[i]>500:
            count=count+1
            print("Book Name",bname[i])
            print("Cost",cost[i])
    print("Total Number :",count)
    print()

def less():
    list=[]
    list1=[]
   
    print("List Of book having cost less than 500 ")
    for i in range(0,len(cost)):
        if cost[i]<500:
            list.append(bname[i])
            list1.append(cost[i])
    for i in range(0,len(list)):
        print(list[i],"",list1[i])
    print()
       
dup()
Sorting()
count()
less()