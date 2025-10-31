from self_py_fun.Quiz3Fun import *

# You can use this .py script to perform debugging task.
sample_arr_1 = np.array([1,2,3,4,5])
d_1 = round(compute_D_partial(sample_arr_1), 2)
d_2 = round(compute_D_correct(sample_arr_1), 2)

print(d_1)
print(d_2)
# The correct d_1 should be 5.66.
