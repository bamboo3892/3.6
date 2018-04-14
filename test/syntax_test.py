import numpy as np

pos1 = np.array([400, 400])
pos2 = np.array([20, 20])
pos3 = pos1 - pos2
print(pos3)


vec = np.array([1, 1])
print(np.cross(vec, [0, -1]))
print((-1 if np.cross(vec, [0, -1]) > 0 else 1) *
      np.arccos(np.dot(vec, [0, -1]) / np.linalg.norm(vec)))
