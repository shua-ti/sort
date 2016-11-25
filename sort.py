#-*-coding=utf-8-*-
#/usr/bin/env python
"多种排序算法实现"
from collections import defaultdict
N=[11,2,3,22,3,45,2,34,6,78]
A=['fbsb','fahb','vsdb','vseu','vsef']
#快速排序
#列表类型 +
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

#归并排序
#从中间位置将数据一份为二，使其成为平衡的递归调用
def mergesort(seq):
    mid = len(seq) // 2
    left,right = seq[:mid],seq[mid:]
    if len(left)>1: left= mergesort(left)
    if len(right)>1:right=mergesort(right)
    res =[]
    while left and right:
        if left[-1] >= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()         #res[]中元素从大到小排列，left/right有一个为空
    return left+right+res

#插入排序
#根据归纳 将 ith 元素插入 (i-1)有序序列中
def insertsort_rec(seq,i):
    if i==1: return
    insertsort_rec(seq,i-1)
    j = i-1
    while j > 0 and seq[j] < seq[j-1]:
        seq[j] ,seq[j-1] = seq[j-1],seq[j]
        j -= 1

#插入排序迭代
def insertionsort_iter(seq):
    for j in range(1,len(seq)): #[1,n-1]
        val = seq[j]
        while j > 0 and val < seq[j-1]:
            seq[j] = seq[j-1]  #避免多次交换操作
            j-=1
        seq[j] = val

#选择排序-
def selectionsort_rec(seq,i):
    if i==1:return
    max_j = 0
    for j in range(1,i):
        if seq[j] > seq[max_j]:max_j = j
    seq[i-1],seq[max_j] = seq[max_j],seq[i-1]
    selectionsort_rec(seq,i-1)

def selectionsort_iter(seq):
    length = len(seq)
    for i in range(length-1):
        min_j = i
        for j in range(i+1,length):
            if seq[j] < seq[min_j]: min_j = j
        seq[i],seq[min_j] = seq[min_j],seq[i]

#计数排序
#单字符排序
def countingsort(A,key=lambda x:x):
    B,C = [],defaultdict(list)
    for x in A:
        C[key(x.lower())].append(x)
    for k in range(97,123):
        B.extend(C[chr(k)])
    return B
#计数排序，相同长度字符串排序
def countsort(A):
    B = A
    for i in range(len(A[0])-1,-1,-1):
        B = countingsort(B,lambda str:str[i])
    return B
if __name__=="__main__":
    print countsort(A)

