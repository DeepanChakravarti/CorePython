#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 05:55:23 2019

@author: deepan1988

Selection Sort
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

Following example explains the above steps:

arr[] = 64 25 12 22 11

// Find the minimum element in arr[0...4]
// and place it at beginning
11 25 12 22 64

// Find the minimum element in arr[1...4]
// and place it at beginning of arr[1...4]
11 12 25 22 64

// Find the minimum element in arr[2...4]
// and place it at beginning of arr[2...4]
11 12 22 25 64

// Find the minimum element in arr[3...4]
// and place it at beginning of arr[3...4]
11 12 22 25 64 
"""
def fetchArgs():
    #inputArray = input('Please enter an array of input seperated by comma: ')
    inputArray = '1,2,3,25,100,97,63,7,2,9,0,6,654,123'
    try:
        inputList = inputArray.split(',')
        intList = list(map(int, inputList))
        
        if (all(isinstance(x, int) for x in intList)):
            selectionSort(intList)
        
    except Exception as e:
        print('''An error has occured while converting the 
              provided input to a list''',e)
        
def selectionSort(intList):
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
