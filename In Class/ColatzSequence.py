longest_seq = 0
longest_sew_orig = 0

for n in range(2,1000):
    if n % 1000 == 1:
        print(n / 100000 * 100, "%")
    orig = n
    while n > 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = n*3 + 1
            
    if count > longest_seq:
        longest_seq = count
        longest_seq_orig = orig

print("The longest sequnce I've seen is:", longest_seq, "starting from", longest_seq_orig)