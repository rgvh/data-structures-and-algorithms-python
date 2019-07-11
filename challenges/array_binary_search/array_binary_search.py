def lst_binary_search(lst,key):
  start = 0
  end = len(lst)
  while start < end:
      mid = (start + end)//2
      if lst[mid] > key:
        end = mid
      if lst[mid] < key:
        start = mid + 1
      if lst[mid] == key:
        print(mid)
        return(mid)
  print(-1)
  return(-1)
