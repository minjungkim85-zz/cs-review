import numpy as np

# ASCII
a = 97
data = np.random.randint(26,size=(20),dtype='uint32') + a
data = np.char.mod('%c', data)
data.sort()

# Iterate over data and create dictionary
counts = {}
for letter in data:
    if letter in counts:
        counts[letter] += 1
    else:
        counts[letter] = 1

# Make reverse dictionary
rev = {}
for lets,cts in counts.items():
    knownlets = rev.setdefault(cts,[])
    knownlets.append(lets)


print(' '.join(data))
print(counts)
print(rev)
