start = int(input("Enter start of range"))
end = int(input("Enter end of range"))
even = []
odd = []
for i in range (start, end+1):
  if i % 2 == 0:
    even.append(i)
  else:
    odd.append(i)
print(odd)
print(even)