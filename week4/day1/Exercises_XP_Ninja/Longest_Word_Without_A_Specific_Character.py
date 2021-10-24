sentence = input("Enter a sentence without A letter !")
letter = "A"
while letter in sentence:
    print("Wrong ! Enter another sentence ! ")
    sentence = input("Enter a sentence without A letter !")
else:
    if len(sentence) == 50:
        print("Congratulation you did it !")
    else:
        print("loser")
