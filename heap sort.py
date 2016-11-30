#-*-coding=utf-8-*-
#/usr/bin/env python
"基于二分堆实现堆排序"

array =[11,22,10,4,5,23,25,19,10]
def heapify(array,i,n):
    j = 2*i+1           #j初始为当前节点的左子节点
    while j<n:
        if j+1 < n and array[j]<array[j+1]:
            j+=1
        if array[i] < array[j]:
            array[i],array[j]=array[j],array[i] #当前节点和较大的子节点swap
            i=j
            j=2*i+1
        else:
            break

#构建堆
def heap_build(array):
    size = len(array)
    for i in range(size//2 -1,-1,-1):#从最后叶节点的父节点开始执行下滤
        heapify(array,i,size)

def heap_sort(array):
    size = len(array)
    heap_build(array)
    for i in range(size-1):
        array[0],array[size-1]= array[size-1],array[0]
        size -=1
        heapify(array,0,size)

if __name__ == "__main__":
    heap_build(array)
    print array