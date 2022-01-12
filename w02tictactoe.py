# a1 = "1"
# a2 = "2"
# a3 = "3"
# b1 = "4"
# b2 = "5"
# b3 = "6"
# c1 = "7"
# c2 = "8"
# c3 = "9"

squares = [1,2,3,4,5,6,7,8,9]
breaker = "-+-+-"

def active_letter(turn):
    if turn == 0:
        active_letter = "x"
        turn = 1
    else:
        active_letter = "o"
        turn = 0
    return active_letter

def square_chooser(letter, ttt_list=squares):   
    looper = True
    while looper: 
        try:
            choice = int(input(f"{letter}'s turn to choose a square (1-9): "))
            if choice in ttt_list:
                index = ttt_list.index(choice)
                ttt_list.pop(index)
                ttt_list.insert(index, letter)
                looper = False
            else:
                print("Invalid entry.")
        except:
            print("Invalid entry! (1-9 only)")           
    return ttt_list


def win_checker(letter, ttt_list, winner):
    if ttt_list[0] == ttt_list[1] == ttt_list[2]:
        print(f"{letter} wins!")
        winner = True
    elif ttt_list[3] == ttt_list[4] == ttt_list[5]:
        print(f"{letter} wins!")
        winner = True       
    elif ttt_list[6] == ttt_list[7] == ttt_list[8]:
        print(f"{letter} wins!")
        winner = True
    elif ttt_list[0] == ttt_list[4] == ttt_list[8]:
        print(f"{letter} wins!")
        winner = True
    elif ttt_list[2] == ttt_list[4] == ttt_list[6]:
        print(f"{letter} wins!")
        winner = True
    elif ttt_list[0] == ttt_list[4] == ttt_list[6]:
        print(f"{letter} wins!")
        winner = True
    elif ttt_list[0] == ttt_list[3] == ttt_list[6]:
        print(f"{letter} wins!")
        winner = True
    elif ttt_list[1] == ttt_list[4] == ttt_list[7]:
        print(f"{letter} wins!")
        winner = True
    elif ttt_list[2] == ttt_list[5] == ttt_list[8]:
        print(f"{letter} wins!")
        winner = True
    else:
        letter = letter
    return winner




def printboard():
    print(f"{squares[0]}|{squares[1]}|{squares[2]}\n{breaker}\n{squares[3]}|{squares[4]}|{squares[5]}\n{breaker}\n{squares[6]}|{squares[7]}|{squares[8]}")

# def printboard():
#     print(f"{a1}|{a2}|{a3}\n{breaker}\n{b1}|{b2}|{b3}\n{breaker}\n{c1}|{c2}|{c3}")

def main():
    win = False
    turn_number = 0
    while win == False:
        letter = active_letter(turn_number)
        square_chooser(letter)
        printboard()
        if turn_number == 0:
            turn_number = 1
        else:
            turn_number = 0
        win = win_checker(letter, squares, win)

main()