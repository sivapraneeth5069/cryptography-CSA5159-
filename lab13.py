import numpy as np
P = np.array([[7, 4],      # HE
              [11, 15]])   # LP
C = np.array([[0, 19],     # AT
              [2, 10]])    # CK
det = int(round(np.linalg.det(P))) % 26
for i in range(26):
    if (det * i) % 26 == 1:
        det_inv = i
        break
adj = np.array([[P[1][1], -P[0][1]],
                [-P[1][0], P[0][0]]])
P_inv = (det_inv * adj) % 26
K = np.dot(C, P_inv) % 26
print("Recovered Key Matrix:")
print(K.astype(int))