# Symbols are VAXE, where E is the 3 horizonal line one
# V=0 A=1 X=2 E=3
Cogoal = 0
Coboard = [[1,2,1],
           [3,2,3],
           [2,0,2]]

Lgoal = 1
Lboard = [[1,1,1],
          [1,1,1],
          [1,1,3]]

Rgoal = 2
Rboard = [[3,1,0],
          [0,2,0],
          [3,1,0]]

Crgoal = 3
Crboard = [[1,2,0],
          [1,2,2],
          [1,1,1]]

def pp(a):
  for x in a:
    print(x)

# matrix to swap position r,c 2 values
def fix(r,c):
  m = [[0,0,0],[0,0,0],[0,0,0]]
  for i in range(3):
    for j in range(3):
      val = ((i==r)+(j==c))
      if val == 1:
        m[i][j] = 3
      else:
        m[i][j] = 2
  return m

# add matrix
def add(m1, m2):
  return [[(a+b)%4 for a,b in zip(c,d)] for c,d in zip(m1,m2)]

# add several matrices
def m_add(*m):
  return reduce(add, m)

def apply_hit(m, r, c, times=1):
  for i in range(3):
    for j in range(3):
      if i==r or j==c:
        m[i][j]= (m[i][j]+times)%4

# modify board m with the hits given in matrix m_hits
def apply_hits(m, m_hits):
  for i in range(3):
    for j in range(3):
      if m_hits[i][j] > 0:
        apply_hit(m, i, j, m_hits[i][j])

# print out a solution for a given board and goal
# solution may not be minimal
def solve(board, goal):
  #make the goal 0
  board = [[(x-goal)%4 for x in y] for y in board]
  first_set = [[x%2 for x in y] for y in board]
  # apply first set of moves to board
  apply_hits(board, first_set)
  next_set = [[0,0,0],[0,0,0],[0,0,0]]
  for i in range(3):
    for j in range(3):
      if board[i][j] == 2:
        next_set = add(next_set, fix(i,j))
  pp(add(first_set,next_set))

  apply_hits(board,next_set)
  print("Sanity check: (Should be all 0's")
  pp(board)

print("Logistics")
solve(Lboard, Lgoal)
print("Revelation")
solve(Rboard, Rgoal)
print("Crew Quarters")
solve(Crboard, Crgoal)
print("Communion")
solve(Coboard, Cogoal)
