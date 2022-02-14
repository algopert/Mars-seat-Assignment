
from pickle import FALSE


NUM_ROWS = 18
NUM_COLS = 9
AVAIL = '-'
BOOKED = 'X'
PASS = 'P'
W_ROW = 2
seatTable = []  #Table initialize
member_cnt = 0
min_marks = 10000000

for i in range(NUM_ROWS):
    column = []
    for j in range(NUM_COLS):
        column.append(AVAIL)
    column[2] = PASS
    column[6] = PASS
    seatTable.append(column)



def full(cnt):
    pp = 0
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            if(seatTable[i][j]==AVAIL):
                pp += 1
            if(pp>=cnt):
                return FALSE

    return True

def next_seat(rr, cc):
    dmin = 10000
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            if((seatTable[i][j]==AVAIL) and (W_ROW*abs(rr-i) + abs(cc-j) < dmin)):
                dmin = W_ROW*abs(rr-i) + abs(cc-j)
                new_row = i
                new_col = j
    
    return dmin, new_row, new_col



def placeSeats(row, col, mem_cnt, marks):
    if(min_marks> marks):
        return

    if(mem_cnt == member_cnt):
        min_marks = marks
        for i in range(member_cnt):
            return






    seatTable[row][col] = BOOKED
    dm, new_r, new_c = next_seat(row,col)
    placeSeats(new_r, new_c, mem_cnt+1, marks+dm)
    seatTable[row][col] = AVAIL
    


        
        


print("WELCOME TO MARS AIR SEATING\n")

# while(1)
print("How many passengers in your group?", end =" "),

# take input from user
member_cnt = int(input())



