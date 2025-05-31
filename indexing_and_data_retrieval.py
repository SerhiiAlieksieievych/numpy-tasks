import numpy as np

chessboard = np.indices((8, 8)).sum(axis=0) % 2

row3 = chessboard[2]
print("3-й рядок шахівниці:", row3)

col5 = chessboard[:, 4]
print("5-й стовпець шахівниці:", col5)

subarray3x3 = chessboard[:3, :3]
print("Підмасив 3x3 з верхнього лівого кута:\n", subarray3x3)
