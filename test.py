from functions import *

def assert(id, expected, actual)
    if expected != actual: print "FAIL: " + id
    else: print "PASSED: " + id

id = "sum_function_01_test"
assert(id, 5, sum_function(2, 3))

id = "sum_function_02_test"
assert(id, 5, sum_function(3, 2))

id = "sum_function_03_test"
assert(id, 70.5, sum_function(2.0, 68.5))

id = "sub_function_01_test"
assert(id, 12, sub_function(15, 3))

id = "sub_function_02_test"
assert(id, -5, sub_function(-3, 2))

id = "sub_function_03_test"
assert(id, 150, sub_function(300, 150))
