file = 'file.txt'
max_data = []
data = []
lm = 0

with open(file, 'r') as f:
    text = f.read()
    for i in f:
        l = len(i)
        if l > lm:
            