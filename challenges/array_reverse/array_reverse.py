lst = [1, 2 ,3, 4, 5]  ## sample list

def reverse_lst(arr):
  new_lst = []
  for i in range(1, len(lst)+1):
    new_lst.append(lst[-i])
    # print(new_lst)
  print(new_lst)

reverse_lst(lst)