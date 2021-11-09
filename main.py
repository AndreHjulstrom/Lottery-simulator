import random
Lottery_list = []
Guess_list = []
count = 0
def lottery():
    Lottery_list = [[],[],[]]
    Guess_list = [[],[],[]]
    count = 0
    count2 = 0
    count3 = 0
    count4 = 0
    while count<1000001:
        count += 1
        for i in range(3):
            Lottery_list[i] = random.randint(0,9)
            Guess_list[i] = random.randint(0,9)
        #print(Lottery_list)
        #print(Guess_list)
        if Lottery_list[0] == Guess_list[0] and Lottery_list[1] != Guess_list[1] and Lottery_list[2] != Guess_list[2]:
            count2 += 1
        if Lottery_list[1] == Guess_list[1] and Lottery_list[0] != Guess_list[0] and Lottery_list[2] != Guess_list[2]:
            count2 += 1
        if Lottery_list[2] == Guess_list[2] and Lottery_list[0] != Guess_list[0] and Lottery_list[1] != Guess_list[1]:
            count2 += 1
        if Lottery_list[0] == Guess_list[0] and Lottery_list[1] == Guess_list[1]:
            count3 += 1
        if Lottery_list[1] == Guess_list[1] and Lottery_list[2] == Guess_list[2]:
            count3 += 1
        if Lottery_list[0] == Guess_list[0] and Lottery_list[2] == Guess_list[2]:
            count3 += 1
        if Lottery_list[0] == Guess_list[0] and Lottery_list[1] == Guess_list[1] and Lottery_list[2] == Guess_list[2]:
            count4 += 1
    print("1 number correct: " + str(count2))
    print("2 numbers correct: " + str(count3))
    print("all 3 numbers correct: " + str(count4))
    print("profit: " + str(count*10-(count2*20+count3*100+count4*1000)))
lottery()
