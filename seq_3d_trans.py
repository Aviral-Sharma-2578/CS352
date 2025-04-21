import numpy as np

# Define the original point in homogeneous coordinates
orig_point = np.array([4, 2, 6, 1])

# Define translation matrices
trans1 = np.array([
    [1, 0, 0, 3],
    [0, 1, 0, -2],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
])

trans2 = np.array([
    [1, 0, 0, -2],
    [0, 1, 0, 4],
    [0, 0, 1, -3],
    [0, 0, 0, 1]
])

# Perform sequential translations
intermediate_point = trans1 @ orig_point
result_sequential = trans2 @ intermediate_point

# Compute the combined transformation matrix
combined_trans = trans2 @ trans1
result_combined = combined_trans @ orig_point

# Verify if both approaches yield the same result
print("Sequential Result:", result_sequential)
print("Combined Result:", result_combined)
