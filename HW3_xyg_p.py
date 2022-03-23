# x：抛出的硬币序列
# P(x0|A) -> p_xA[0]
# P(x0|B) -> p_xB[0]
# P(A|x0) -> P_Ax[0]
# P(B|x0) -> P_Bx[0]

theta_A = [0.60]
theta_B = [0.50]

x = [5, 9, 8, 4, 7]

p_xA = [0 for l in range(5)]
p_xB = [0 for l in range(5)]

P_Ax = [0 for l in range(5)]
P_Bx = [0 for l in range(5)]

ahs = 0
ats = 0
bhs = 0
bts = 0

A_H_sum = [ ]
A_T_sum = [ ]
B_H_sum = [ ]
B_T_sum = [ ]

m = 0
while True:
    
    for i in range(5):
        p_xA[i] = theta_A[m] ** x[i] * (1 - theta_A[m]) ** (10 - x[i])
        p_xB[i] = theta_B[m] ** x[i] * (1 - theta_B[m]) ** (10 - x[i])

        P_Ax[i] = round(p_xA[i] / (p_xA[i] + p_xB[i]), 2)
        P_Bx[i] = 1 - P_Ax[i]

    for k in range(5):
        ahs += round(P_Ax[k] * x[k], 1)
        ats += round(P_Ax[k] * (10 - x[k]), 1)
        bhs += round(P_Bx[k] * x[k], 1)
        bts += round(P_Bx[k] * (10 - x[k]), 1)
        
    A_H_sum.append(ahs)
    A_T_sum.append(ats)
    B_H_sum.append(bhs)
    B_T_sum.append(bts)

    ahs = 0
    ats = 0
    bhs = 0
    bts = 0

    theta_A.append(round(A_H_sum[m] / (A_H_sum[m] + A_T_sum[m]), 2))
    theta_B.append(round(B_H_sum[m] / (B_H_sum[m] + B_T_sum[m]), 2))

    if theta_A[m + 1] == theta_A[m] and theta_B[m + 1] == theta_B[m]:
        print("theta_A = %f" %theta_A[m])
        print("theta_B = %f" %theta_B[m])
        break
    m += 1



    
