# 1) Calculate the sum of all the elements in the list
Dev=[4,8,1,9,6]
sum = 0
for element in Dev:
    sum += element
print("sum:",sum)

# 2) Find the smallest number
smallest= min(Dev)
print("smallest:" ,smallest)

# 3) Find the largest number
largest=max(Dev)
print("Largest:",largest)

# 4) Display list in ascending order
ace=sorted(Dev)
print("ascending:",ace)

# 5) Display list in descending order
dec=sorted(Dev,reverse=True)
print("descending:",dec)

# 6) Convert list into tuple
t=tuple(Dev)
print("list into tuple:",t)

# 7) Delete the list
# del Dev
# print(Dev)