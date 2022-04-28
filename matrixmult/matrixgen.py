#generate a 100x100 matrix
import random
with open('matrix1.txt', 'w') as f:
    for j in range (0,10):
      for i in range (0,10):
        num = random.randint(0, 10)
        f.write(str(num))
        f.write(" ")
      f.write("\n")
