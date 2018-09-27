import math

def insertsort(k):
	for i in range(len(k)):
		key = k[i]
		j = i - 1
		while (j >= 0) and (k[j] > key):
			k[j+1] =k[j]
			j-=1
		k[j+1] = key
	print(k)

def merge(k,l,m,r):
	print(k,l,m,r)
	left = k[l:m]
	right = k[m:r]
	mergeli = []
	i,j,k = 0,0,0
	print(i,j,len(left),len(right))

	while (i<len(left)) and (j<len(right)):
		if left[i] < right[j]:
			mergeli.append(left[i])
			i+=1
		else:
			mergeli.append(right[j])
			j+=1
		k+=1

	while (i<len(left)):
		mergeli.append(left[i])
		i +=1
	while (j<len(right)):
		mergeli.append(right[j])
		j+=1
	print(mergeli)

def mergesort(k,l,r):
	if (l<r):
		mid = math.floor((l+r)/2)
		mergesort(k,l, mid)
		mergesort(k,mid+1,r)
		merge(k,l,mid,r)

def maxheap(k):
	print(k)
	flag,i,n = True,0,len(k)
	while flag:
		if (2*i+1 < n) and (k[i] < k[2*i+1]):
			tmp = k[2*i+1]
			k[2*i+1] = k[i]
			k[i] = tmp
			i = 2*i+1
			if i > n:
				flag = False
		elif (2*i+2 < n) and (k[i] < k[2*i+2]):
			tmp = k[2*i+2]
			k[2*i+2] = k[i]
			k[i] = tmp
			i = 2*i+2
			if i > n:
				flag = False
		else:
			flag = False
		print(i)
		print(k)
	print(k)

# mergesort([6,5,4,3,1,2],0,5)
# maxheap([1,2,3,4,56])

def partition(a,s,e):
	pindex = s
	pivot = a[e]
	# print("pri", pivot)

	for i in range(s,e):
		if (a[i] <= pivot):
			tmp = a[i]
			a[i] = a[pindex]
			a[pindex]=tmp
			pindex +=1
			# print("ind", a)
	tmp = a[pindex]
	a[pindex] = a[e]
	a[e] = tmp
	return pindex



def qsort(a, s,e):
	print(s,e)
	if s<e:
		p = partition(a,s,e)
		print(p,a)
		qsort(a,s,p-1)
		qsort(a,p+1,e)
		print(a)

# a = list(range(1,100000000))
# b = sorted(a)
# print(len(b))
qsort([6,5,4,3,1,2],0,5)


#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#Example:
#
#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp,temp1 = l1,l2
        one,two = "",""
        while True:
            if temp.next == None:
                one = str(temp.val) + one 
                break
            one = str(temp.val) + one
            temp = temp.next
            
        while True:
            if temp1.next == None:
                two = str(temp1.val) + two 
                break
            two = str(temp1.val) + two 
            temp1 = temp1.next
        three = str(int(one) + int(two))
        four = (list(reversed(three)))
        return list(map(int, four))
