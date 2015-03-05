sumset = []
for i in range(1000):
    if ((i % 3) == 0) or ((i % 5) == 0):
        sumset.append(i)
print sum(sumset)
