import numpy as np
import matplotlib.pyplot as plt


#Resolution d'un systeme A*X=B
def resolveLinear3x3(matrice_array, results_array):
    #Conversion de standard array vers np array
    matrice_np=np.array(matrice_array) # matrice coefficiants A
    result_np=np.array(results_array) # matrice solutions B
    #SOLUTION SYSTEME: A^(-1)*B=X
    matrice_inverse = np.linalg.inv(matrice_np)
    solutions = np.dot(matrice_inverse, result_np)
    print("solution is="+str(solutions)+ " length is="+str(len(solutions)))

    for value in range(0,len(solutions)):
        print("X"+str(value)+"="+str(solutions[value]))

    return solutions

def resolveLinear3x3_ots(matrice_array, results_array):
    #Conversion de standard array vers np array
    matrice_np=np.array(matrice_array)
    result_np=np.array(results_array)
    #SOLUTION SYSTEM AX=B directe
    solutions = np.linalg.solve(matrice_np, result_np)
    print("solution OTS is="+str(solutions)+ " length is="+str(len(solutions)))

    for value in range(0,len(solutions)):
        print("X"+str(value)+"="+str(solutions[value]))

    return solutions

def calculateM(x2, y2, x1, y1):
    m = (y2 - y1) / (x2 - x1)
    b = y2 - m * x2
    print("la pente f(x)= " + str(m) + "X" + " +" + str(b))
    return [m, b]


def Main():
    coefficients = (
        [0.5833, -0.3333, -0.25],
        [-0.3333, 1.4762, -0.1429],
        [-0.25, -0.1429, 0.5929]
    )
    results = (
        [-11],
        [3],
        [25]
    )
    resolveLinear3x3(coefficients,results)
    resolveLinear3x3_ots(coefficients,results)


if __name__ == "__main__":
    Main()
