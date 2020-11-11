var = 0
alpha = dict()
beta = list()
fn = input("Enter a file name:")
try:
    ofile = open(fn)
except:
    print("File cannot be opened:", fn)
    quit()
for line in ofile:
    #print(line)
    words = line.split()
    #print(words)
    for word in words:
        for letter in word:
            if letter.isalpha():
                alpha[letter.lower()] = alpha.get(letter.lower(), 0) + 1
print(sorted([(v,k)for k, v in alpha.items()],reverse = True))
