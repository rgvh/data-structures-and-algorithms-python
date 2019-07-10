from array_shift import insert_shift_array

def test_basic():
  assert insert_shift_array

def test_even_list_lenght():
  assert insert_shift_array([10,9,7,6], 8) == [10,9,8,7,6]

def test_odd_list_lenght():
  assert insert_shift_array([1,2,4], 3) == [1,2,3,4]

def test_expected_failure():
  assert insert_shift_array([1,3],2) != [3,1,2]
