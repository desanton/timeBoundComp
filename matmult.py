from random import seed
from random import randint
seed(1)

import numpy
sizeMat = 3
randMat1 = numpy.zeros(shape=(sizeMat,sizeMat))
randMat2 = numpy.zeros(shape=(sizeMat,sizeMat))
# iterate through rows of randmat
for i in range(sizeMat):
   # iterate through columns of rand
   for j in range(sizeMat):
       randMat1[i][j] = randint(0,5)
       randMat2[i][j] = randint(0,5)
print("First random matrix:")
for r in randMat1:
   print(r)
print(" ")
print("Second random matrix:")
for r in randMat2:
   print(r)
print(" ")

# Program to multiply two matrices using nested loops
# 3x3 matrix
result = numpy.zeros(shape=(sizeMat,sizeMat))
import time
start_time = time.time()
# iterate through rows of randMat1
for i in range(sizeMat):
   # iterate through columns of randMat2
   for j in range(sizeMat):
       # iterate through rows of Y
       for k in range(sizeMat):
           result[i][j] += randMat1[i][k] * randMat2[k][j]
elapsed_time = time.time() - start_time
print("result without numpy multiplication:")
for r in result:
   print(r)
print ("elapsed time without numpy multiplication= " + str(elapsed_time))
print(" ")

start_time = time.time()   
numpyMat = numpy.matmul(randMat1, randMat2)
elapsed_time = time.time() - start_time
print("result with numpy multiplication:")
for r in numpyMat:
   print(r)
print ("elapsed time with numpy multiplication= " + str(elapsed_time))
