a=10
result= a>9 and a<10 #logical operator
print("result of",a,">9 and ",a,"<10:",result) 

a=10
result= a>5 or a<10 #logical operator
print("result of",a,">9 or ",a,"<10:",result)

a=10
result= not(a>5 and a<10)  #logical operator 
print("result of",a,">9 not  ",a,"<10:",result)