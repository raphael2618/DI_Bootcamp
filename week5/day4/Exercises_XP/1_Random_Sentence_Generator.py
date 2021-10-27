# with open('sowpods') as f:
#     contents = f.read()
#     print(contents)

# with open('sowpods', 'r') as f:
#     listl = []
#     for line in f:
#         strip_lines = line.strip()
#         listli = strip_lines.split("\n")
#         print(listli)
#         m = listl.append(listli)
#     print(listl)
def get_words_from_file():
    a_file = open("sowpods", "r")

    list_of_lists = [(line.strip()).split() for line in a_file]

    a_file.close()

    return list_of_lists


def get_random_sentence(length):
    length = input("How long do you want the sentence to be ?")
    if 2 < length < 20:
        res = get_words_from_file()
        sentence = []
        for i in res:
            while i < length:
                length(i).lower()
                sentence.append(i)
        print(sentence)
    else:
        pass


if __name__ == '__main__':
    print("The program will open the sowpods.txt file then iterate into it and take the number that the user has "
          "enter then make a sentence of the number display the sentence")
