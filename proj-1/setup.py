from board import Board

num = 0

with open('test.txt','r') as f:

  puzzle_contents= f.read()
  print(puzzle_contents)

with open('test.txt','r') as f:

  for line in f:
    num += 1
  print("There is:", num, " Puzzles")

with open('test.txt','r') as f:

  lst= [] #empty list
  for line in f:
    for word in line.split():
        lst.append(word)  
print (lst)

count=0
BoardsList=[]

with open('test.txt','r') as f:
  counter = 1
  depth = 1
  size = 0
  state =2
  for i in range (len(lst)):
        if i == 0 :
          BoardsList.append(Board(counter,lst[i+depth],lst[i],lst[i+state]))
        elif i < num:
          depth+=2
          size+=2
          state+=2
          counter+=1
          print(type(lst[i+state]))
          print(lst[i+state])
          BoardsList.append(Board(counter,lst[i+depth],lst[i+size],lst[i+state]))
          print(BoardsList[i].maxD)
          #BoardsList.append(Board(counter,lst[i+depth],lst[i],str(lst[i+state])))
 
#with open('test.txt') as f:
 #   content = f.readlines()
# remove whitespace characters like `\n` at the end of each line
#content = [x.strip() for x in content]
#print (content[0]) 

  def atGoal(state):
    for row in state:   # loop through each value in the board's state (2D array)
      for val in row:
        if val != 0:
          return False  # if there is a single 1 in the matrix return False
    return True         # otherwise return True