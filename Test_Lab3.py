import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending_REQ_01():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending_REQ_02():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_more_than_10_REQ_03():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 20, 40, 50, 80, 13, 15]
    result = Lab3.bubble_sort(input_arr, 3)
    expected = 1
    assert (result == expected)


def test_array_empty_REQ_04():
    input_arr = []
    result = Lab3.bubble_sort(input_arr, 3)
    expected = 0
    assert (result == expected)

def test_bubble_sort_invalid_REQ_05():
    input_arr = [1, 2, 3, 4] #FUNCTION RUNS PERFECTLY WITH ARRAY ["A", "B", "C"] returning Value of 2 but fails when numbers will fail it
    result = Lab3.bubble_sort(input_arr, 1)
    assert (result == 2)




