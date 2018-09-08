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