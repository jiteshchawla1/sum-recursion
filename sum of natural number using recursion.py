def recur_sum(n):
     if n<=1:
          return n
     else:
          return n+recur_sum(n-1)
num=int(input("enter a number "))
if num<0:
     print("enter a +ve number")
else:
     print("enter a number ", recur_sum(num))
     
