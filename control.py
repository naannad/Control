from string import*


def unique_content(string):
    symbols = ascii_letters + digits + punctuation + whitespace

    letters = []
    for i in range(len(string)):
        if string[i].lower() in symbols:
            letters.append(string[i])

    return len(set(letters))


print(unique_content('Hello, World!'))