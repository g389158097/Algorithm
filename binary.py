def binary_search(list,item):#二分查找要点必须有序
  low=0
  high=len(list)-1
  while low <= high:
    mid=int((low+high)/2)
    guess=list[mid]
    if guess==item:
      return mid
    elif guess>item:
      high=mid-1
    else:
     low=mid+1
  return 'none	'
	  
my_list=[1,3,5,7,9]
print(binary_search(my_list,10))
