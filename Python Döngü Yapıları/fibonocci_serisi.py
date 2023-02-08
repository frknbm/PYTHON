print("""*************
      fibonacci serisi
*************      
    """)

a=1
b=1
fibonacci=[a,b]
for i in range(20):
    a,b=b,a+b
    print("a degeri:",a,"b degeri:",b)
    fibonacci.append(b)

print(fibonacci)
