
# try:
#     with open(filename, encoding='utf-8') as f:
#         concents = f.read()
# except FileNotFoundError:
#     print(f"the file{filename} does not exist")
# else:
#     words = concents.split()
#     num_words = len(words)
#     print(f"the file {filename} has about {num_words} words")

def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            concents = f.read()
    except FileNotFoundError:
        print(f"the file{filename} does not exist")
    else:
        words = concents.split()
        num_words = len(words)
        print(f"the file {filename} has about {num_words} words")


filename = 'alice.txt'
count_words(filename)


