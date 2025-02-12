import numpy as np
import matplotlib.pyplot as plt


def drawCurve(R1,value):
    R2_values= np.arange(100, 3001, 10)
    vout_regs = []
    vin_filtres = []
    R1_fixed = R1  # Valeur fixe de R1 pour simplifier le tracé

    for R2 in R2_values:
        vout_reg,vin_filtre = calculateVoutRegulateur(R1_fixed, R2)
        vout_regs.append(vout_reg)
        vin_filtres.append(vin_filtre)

    plt.figure(figsize=(10, 6))
    plt.plot(R2_values, vout_regs, label=f'Vout_reg (R1 = {R1_fixed} Ohms)')
    plt.plot(R2_values, vin_filtres, label=f'Vin_filtre (R1 = {R1_fixed} Ohms)')
    plt.xlabel('R2 (Ohms)')
    plt.ylabel('Tension de sortie (V)')
    plt.title('Tension de sortie du régulateur en fonction de R2')
    plt.legend()
    plt.grid(True)
    if value == 2: #Permet de afficher plusieurs graphs de suite en empechant la fin du programme
        plt.show()
    plt.pause(0.1)


    """
    vin_sec - Voltage AC NON RMS - voltage secondaire  du transformateur
    fin - frequence du signal HZ
    """
def getRectificationValues(type, vin_sec, fin):
    vp = 0
    frec = 0
    if type == "full_rectifier":
        vp = vin_sec - 1.4
        frec = 2 * fin
    return [vp, frec]


    """
    vp - Voltage AC NON RMS - voltage peak  rectifier apres le pont de diodes half ou full
    vr_pp - Voltage AC NON RMS PEAK-PEAK- voltage de ripple après filtre
     """
def calculateFrequence(RA,RB,C1):
    f=1.44/((RA+2*RB)*C1)

    print(f"f={f},RA = {RA}, RB = {RB}, C1 = {C1}")
    return  f


def calculateDutyCycle(RA, RB, C1):
    f = 1.44 / ((RA + 2 * RB) * C1)
    th = 0.693 * (RA + RB) * C1
    tl = 0.693 * RB * C1
    T = th + tl
    fclone = 1 / T

    print(f"f={f},RA = {RA}, RB = {RB}, C1 = {C1} ,th={th} ,tl={tl} ,fclone= {fclone}")
    return f

def calculateVoutRegulateur(R1,R2):
    # APROXIMATIVE vout_reg=1.25*(1+R2/R1)
    vout_reg=1.25*(1+R2/R1)+R2*50e-6
    vin_filtre=vout_reg+4
    print(f"R1={R1},R2 ={R2},vout_reg = {vout_reg},vin_filtre ={vin_filtre} \n")

    return [vout_reg,vin_filtre]

def calculateFrequence(RA,RB,C1):
    f=1.44/((RA+2*RB)*C1)

    print(f"f={f},RA = {RA}, RB = {RB}, C1 = {C1}")
    return  f
def Main():

    print(f"section 3------------------------------------------------------------")
    for i in range(1, 10000, 100):
        #calculateFrequence(10000, i, 0.0001)
        calculateDutyCycle(10000, i, 0.0001)

    #drawCurve(1000,3)


if __name__ == "__main__":
    Main()
