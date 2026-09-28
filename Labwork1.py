choose = int(input("Choose exercise: "))
if choose == 1:
    r=int(input("Enter circle radius?"))
    print("Circle area =",3.14*r*r)
if choose == 2:
    c=int(input("Enter the temperature in Celcius?"))
    print(c," (C) =",(c*9/5)+32,"(F)")
if choose == 3:
    n=int(input("Enter a number?"))
    ans=0
    for i in range(1,n+1):
        if n%i==0:
            ans+=1
    if ans==2:
        print(n,"is a prime number")
    else:
        print(n,"is a NOT prime number")
if choose == 4:
    n=int(input("Enter a number?"))
    sum=0
    for i in range (1,n-1):
        if n%i==0:
            sum+=i
    if sum==n:
        print(n,"is a perfect number")
    else:
        print(n,"is a NOT perfect number")
if choose == 5:
    color=input("What is your favourite color?")
    lst=input("Enter color list:").split()
    if color in lst:
        index=lst.index(color)
        print("Your color is at index",index,"in my list")
    else:
        print("Sorry, I could not find your color")
if choose == 6:
    range1=range(0,7)
    range2=range(1,11,3)
    range3=range(5,0,-1)
    range4=range(6,-3,-2)
    print(list(range1))
    print(list(range2))
    print(list(range3))
    print(list(range4))
if choose == 7:
    s=input()
    def remove_dollar_sign(s):
        return s.replace("$","")
    print(remove_dollar_sign(s))
if choose == 8:
    l=list(map(int,input("Enter the list:").split()))
    def extract_even(l):
        ans=[]
        for i in l:
            if i%2==0:
                ans.append(i)
        return ans
    print(extract_even(l))
if choose == 9:
    def factorial(n):
        fac=1
        for i in range(1,n+1):
            fac*=i
        return fac
    n=int(input("Enter a number:"))
    print(factorial(n))
if choose == 10:
    def divisors(n):
        lst=[]
        for i in range(1,n+1):
            if n%i==0:
                lst.append(i)
        return lst
    n=int(input("Enter a number:"))
    print(divisors(n))
if choose == 11:
    x1=int(input())
    y1=int(input())
    x2=int(input())
    y2=int(input())
    d=((x2-x1)**2+(y2-y1)**2)**0.5
    print("Distance between (",x1,",",y1,") and (",x2,",",y2,") is",round(d,2) )    
if choose == 12:
    def pattern(m,n):
        for i in range(m):
            if i==0 or i==m-1:
                print("* "*n)
            else:
                print("* " + "  "*(n-2) + "*")
        print()
    m=int(input())  
    n=int(input())
    pattern(m,n)