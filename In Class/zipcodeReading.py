f = open("zipcode-data.csv", "r")

total = 0
firstLineRead = False


for line in f:
    if not firstLineRead:
        firstLineRead = True
        continue
    columns = line.split(",")
    zipcode = columns[0].strip('"')
    state = columns[3].strip('"')
    if len(columns[10]) > 0:
        population = int(columns[10])
    else:
        population = 0
    
    if state == "IA":
        total += population
        
print(total)