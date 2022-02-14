
NUM_ROWS = 18
NUM_COLS = 9
AVAIL = '-'
BOOKED = 'X'
PASS = 'P'
W_ROW = 2.5
MAX_MEMBER = 162

def placeSeats(row, col, depth, marks, optCols, optRows, tmpCols,  tmpRows, member_cnt, config_data, seatTable):
    # global min_marks, optCols, optRows        
    min_marks = config_data['min_marks']
    if( min_marks <= marks):
        return

    if(depth == member_cnt):
        min_marks = marks
        config_data['min_marks'] = min_marks
        for i in range(member_cnt):
            optRows[i] = tmpRows[i]
            optCols[i] = tmpCols[i]

        # print("----------------",min_marks)
        # print(optRows, optCols)
        
        return

    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            if(seatTable[i][j]==AVAIL):
                seatTable[i][j] = BOOKED            
                tmpRows[depth] = i
                tmpCols[depth] = j
                if(depth == 0):
                    placeSeats(i, j, depth+1, i, optCols, optRows, tmpCols,  tmpRows, member_cnt, config_data, seatTable)
                else:
                    placeSeats(i, j, depth+1, marks+W_ROW*abs(row-i) + abs(col-j), optCols, optRows, tmpCols,  tmpRows, member_cnt, config_data, seatTable)
                seatTable[i][j] = AVAIL


def get_str_col(x):
    return{
        0: 'A', 1: 'B',  3: 'C',   4: 'D',  5: 'E',  7: 'F',  8: 'G',
    }[x]

def get_seat_str(row,col):
    return str(row+1) + get_str_col(col)

def main():
    ###################### Initialize ####################
    seatTable = []  #Table initialize

    member_cnt = 0
    min_marks = 10000000
    optCols =[0]*MAX_MEMBER
    optRows =[0]*MAX_MEMBER
    tmpCols=[0]*MAX_MEMBER
    tmpRows=[0]*MAX_MEMBER

    ######################  Main Program              ########################
    print("WELCOME TO MARS AIR SEATING\n")

    for i in range(NUM_ROWS):  # seat initailize
        column = [AVAIL]*NUM_COLS
        column[2] = PASS
        column[6] = PASS
        seatTable.append(column)
    
    config_data={
        'min_marks': min_marks
    }

    while True:
        print("How many passengers in your group?", end =" "), # input number of user
        member_cnt = int(input())

        min_marks = MAX_MEMBER * MAX_MEMBER
        config_data['min_marks'] = min_marks

        placeSeats(0, 0, 0, 0, optCols, optRows, tmpCols,  tmpRows, member_cnt, config_data, seatTable)

        new_book_list=[]
        for i in range(member_cnt):
            seatTable[optRows[i]][optCols[i]] = BOOKED
            new_book_list.append(get_seat_str(optRows[i], optCols[i]))
        
        new_book_list.sort()

        print("Seating assignments:", end =" ")
        for i in range(member_cnt):
            print(new_book_list[i], end = " ")
        print("\n\n")

    

main()