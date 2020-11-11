name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
fdict = dict()
lst = list()
for line in handle:
    if line.startswith("From ") :
        words = line.split()
        time = words[5]
        hour = time[:2]
        lst.append(hour)

for hour in lst:
    fdict[hour] = fdict.get(hour, 0) + 1


for clock, date in sorted(fdict.items()):
    print(clock, date)
