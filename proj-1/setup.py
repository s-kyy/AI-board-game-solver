

num = 0

with open('test.txt','r') as f:

  puzzle_contents= f.read()
  print(puzzle_contents)

with open('test.txt','r') as f:

  for line in f:
    num += 1
  print("There is:", num, " Puzzles")
  
  


  
  

    

    