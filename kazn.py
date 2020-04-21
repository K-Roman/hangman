import random

def hangman():
    word_list=["Зеркало","Тварь","Небо"]
    word_in=random.randint(0,2)
    word=word_list[word_in]
    wrong=0
    stages = ["",
              "_______       ",
              "|             ",
              "|      |      ",
              "|      0      ",
              "|     /|\     ",
              "|     / \     ",
              "|             "]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("Добро пожаловать на казнь")
    while wrong < len(stages)-1:
        print("\n")
        msg="Введите букву: "
        char=input(msg)
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]="$"
        else:
            wrong +=1
        print((" ".join(board)))
        print("\n".join(stages[0:wrong+1]))
        if "_" not in board:
              print("Вы выиграли. Было загадано слово: ")
              print(" ".join(board))
              win=True
              break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("Вы проиграли. Было загадано слово: {}.".format(word))
hangman()
