file = 'file.txt'
max_data = []
data = []

with open(file, 'r') as f:
    text = f.read()
    for i in f:
        if 