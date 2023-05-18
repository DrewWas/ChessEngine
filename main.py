#collums 
collums = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

#ranks
rank = [i for i in range(1,9)]


### REPLACE THESE LISTS WITH 1 DICTIONARY 
### - Each value is a list of the position ex: ['a', 1] and the key is the piece type ex: "rook"

# create 'board' with all pieces 
white_pawns = [(collums[i], rank[1]) for i in range(8)]
white_knights = [(collums[1], rank[0]), (collums[6], rank[0])]
white_rooks = [(collums[0], rank[0]), (collums[7], rank[0])]
white_bishops = [(collums[2], rank[0]), (collums[5], rank[0])]
white_queen = [(collums[3], rank[0])]
white_king= [(collums[4], rank[0])]


print("white pawns: ", white_pawns)
print("white knights: ", white_knights)
print("white rooks: ", white_rooks)
print("white bishops: ", white_bishops)
print("white queen: ", white_queen)
print("white king: ", white_king)


# get possible moves
def poss_pawn_plays(x,y, first_move=True):
    moves = []

    if first_move:
        moves.append((collums[x], rank[y]))
        moves.append((collums[x], rank[y]))
        first_move = False
    else:
        moves.append((collums[x], rank[y]))

    return moves


# get position and type of each piece 
"""This is a horrible function and needs to be improved in the future!!!!!"""

def get_pos(x,y):

   #for i in white_pawns, black_pawns: _____ --> ???? 
    for i in white_pawns:
        if i == (collums[x], rank[y]):
            print((collums[x], rank[y]), "type: pawn")
            return "pawn"

    for i in white_rooks:
        if i == (collums[x], rank[y]):
            print((collums[x], rank[y]), "type: rook")
            return "rook"

    for i in white_knights:
        if i == (collums[x], rank[y]):
            print((collums[x], rank[y]), "type: knight")
            return "knight" 
    
    for i in white_bishops:
        if i == (collums[x], rank[y]):
            print((collums[x], rank[y]), "type: bishop")
            return "bishop"

    for i in white_queen:
        if i == (collums[x], rank[y]):
           print((collums[x], rank[y]), "type: queen")
           return "queen"

    for i in white_king:
        if i == (collums[x], rank[y]):
            print((collums[x], rank[y]), "type: king")
            return "king" 
        else:
            print("No piece on that square")
            return None


def move_piece(start_col, start_rank, end_col, end_rank):
    piece = get_pos(start_col, start_rank)
    if piece == None:
        print("error")
    elif piece == 'pawn':

        #make sure move is legal --> poss_pawn_plays()
        if (collums[end_col], rank[end_rank]) in poss_pawn_plays(end_col, end_rank):
            print(True)
        else:
            print(False)
 

        #move pawn to that square by updating original list 
    


q = int(input("start column: "))
w = int(input("start rank: "))
t = int(input("end column: "))
u = int(input("end column: "))

move_piece(q,w,t,u)





"""
# move a piece and update the board 
for i in poss_pawn_moves(4, 1):
    print(i)

for i in poss_pawn_moves(4, 2):
    print(i)


#print(get_pawn_position(4, 1))
"""






