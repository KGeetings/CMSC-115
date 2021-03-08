x = []

for i in range(10):
    if i % 2 == 1:
        x.append(i*i)

x = [i*i for i in range(10) if i % 2 == 1]
