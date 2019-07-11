from array_binary_search import lst_binary_search

def test_basic():
  assert lst_binary_search

def test_even_list_length():
  assert lst_binary_search([3,4,7,10,16,27], 4) == 1

def test_odd_list_length():
  assert lst_binary_search([1,5,7,9,11], 11) == 4

def test_not_in_list():
  assert lst_binary_search([1,3],2) == -1

def test_empty_list():
  assert lst_binary_search([],2) == -1