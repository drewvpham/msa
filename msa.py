# MULTIPLES
for num in range(1, 1001):
        if num % 2 is not 0:
            print num


for num in range(5, 1000001):
        if num % 5 == 0:
            print num

# SUM LIST
a = [1, 2, 5, 10, 255, 3]
sum=0
for num in a:
    sum+=num
print sum



# AVERAGE LIST
a = [1, 2, 5, 10, 255, 3]
sum=0
for num in a:
    sum+=num/len(a)
print sum
