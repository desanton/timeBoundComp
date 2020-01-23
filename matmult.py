from random import seed
from random import randint
seed(1)

import numpy
sizeMat = [10, 100, 400]
elapsedTimeMult = [0, 0, 0]
elapsedTimeNumpy = [0, 0, 0]
index = 0

for mm in sizeMat:
   print ("mm = ", str(mm))
   randMat1 = numpy.zeros(shape=(mm,mm))
   randMat2 = numpy.zeros(shape=(mm,mm))
   # iterate through rows of randmat
   for i in range(mm):
      # iterate through columns of rand
      for j in range(mm):
          randMat1[i][j] = randint(0,5)
          randMat2[i][j] = randint(0,5)
   # print("First random matrix:")
   # for r in randMat1:
   #    print(r)
   # print(" ")
   # print("Second random matrix:")
   # for r in randMat2:
   #    print(r)
   # print(" ")

   # Program to multiply two matrices using nested loops
   # 3x3 matrix
   result = numpy.zeros(shape=(mm,mm))
   import time
   start_time = time.time()
   # iterate through rows of randMat1
   for i in range(mm):
      # print ("i = ", str(i))
      # iterate through columns of randMat2
      for j in range(mm):
          # iterate through rows of Y
          for k in range(mm):
              result[i][j] += randMat1[i][k] * randMat2[k][j]
   elapsed_time = time.time() - start_time
   # print("result without numpy multiplication:")
   # for r in result:
   #    print(r)
   print ("elapsed time without numpy multiplication= " + str(elapsed_time))
   elapsedTimeMult[index] = elapsed_time

   start_time = time.time()   
   numpyMat = numpy.matmul(randMat1, randMat2)
   elapsed_time = time.time() - start_time
   # print("result with numpy multiplication:")
   # for r in numpyMat:
   #    print(r)
   print ("elapsed time with numpy multiplication= " + str(elapsed_time))
   print(" ")

   elapsedTimeNumpy[index] = elapsed_time

   index = index + 1
   
import matplotlib.pyplot as plt

# Initialize the figure and axes
fig, ax = plt.subplots(1, figsize=(8, 6))

# Set the title for the figure
fig.suptitle('Matrix multiplication with and without numpy', fontsize=15)

# Draw all the lines in the same plot, assigning a label for each one to be
# shown in the legend
ax.plot(sizeMat, elapsedTimeMult, color="red", label="without numpy")
ax.plot(sizeMat, elapsedTimeNumpy, color="green", label="with numpy")

# Add a legend with title, position it on the lower right (loc) with no box framing (frameon)
ax.legend(loc="lower right", title="Legend Title", frameon=False)

# Show the plot
plt.show()

quit()

