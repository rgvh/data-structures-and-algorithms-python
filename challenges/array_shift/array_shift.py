def insert_shift_array(arr, val):
  midpoint = len(arr)/2 
  if midpoint%2 == 0:
    insert_idx = int(midpoint)
  else:
    insert_idx = int(midpoint) + 1
  print('hello')
  beg_arr = arr[:insert_idx]
  end_arr = arr[insert_idx:]
  beg_arr.append(val)
  new_arr =  beg_arr + end_arr
  print(new_arr)
  return new_arr

# insert_shift_array(arr, val)