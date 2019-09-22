#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 23:14:35 2019

@author: deepan1988

Bubble Sort

Bubble Sort
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
Example:
First Pass:
( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.

Second Pass:
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.

Third Pass:
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
"""

def fetchArgs():
    #inputArray = input('Please enter an array of input seperated by comma: ')
    inputArray = '1,2,3,25,100,97,63,7,2,9,0,6,654,123'
    try:
        inputList = inputArray.split(',')
        intList = list(map(int, inputList))
        
        if (all(isinstance(x, int) for x in intList)):
            bubbleSort(intList)
        
    except Exception as e:
        print('''An error has occured while converting the 
              provided input to a list''',e)
        
def bubbleSort(intList):
    arrayLen = len(intList)
    for i in range(0,arrayLen):
        if (i == arrayLen - 1):
            break
        for j in range(i,arrayLen):
            if intList[i] > intList[j]:
                intList[i],intList[j] = intList[j],intList[i] 
            
    print(intList)
        
        

if (__name__ == '__main__'):
    fetchArgs()
