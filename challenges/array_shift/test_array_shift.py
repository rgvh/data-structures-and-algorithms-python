from array_shift import insert_shift_array

def test_basic():
  assert insert_shift_array([1,2,4], 3) == [1,2,3,4]
