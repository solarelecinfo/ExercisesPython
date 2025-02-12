import numpy as np
import matplotlib.pyplot as plt


def drawCurve(R1, value):
    R2_values = np.arange(100, 1001, 10)
    vout_regs = []
    vin_filtres = []
    R1_fixed = R1  # Valeur fixe de R1 pour simplifier le tracé

    for R2 in R2_values:
        vout_reg, vin_filtre = calculateVoutRegulateur(R1_fixed, R2)
        vout_regs.append(vout_reg)
        vin_filtres.append(vin_filtre)

    plt.figure(figsize=(10, 6))
    plt.plot(R2_values, vout_regs, label=f'R1 = {R1_fixed} Ohms')
    plt.plot(R2_values, vin_filtres, label=f'Vin_filtre (R1 = {R1_fixed} Ohms)')
    plt.xlabel('R2 (Ohms)')
    plt.ylabel('Tension de sortie (V)')
    plt.title('Tension de sortie du régulateur en fonction de R2')
    plt.legend()
    plt.grid(True)
    if value == 2:
        plt.show()
    plt.pause(0.1)


def drawCurveRectifier(C1):
    RL_values = np.arange(100, 1001, 10)
    vr_pp_array = []
    vdc_array = []
    ripple_factor_array = []

    for RL in RL_values:
        vr_pp, vdc, ripple_factor = calculateVripple_peakpeak_pourcentage(C1, RL)
        vr_pp_array.append(vr_pp)
        vdc_array.append(vdc)
        ripple_factor_array.append(ripple_factor)

    plt.figure(figsize=(12, 10))

    # Sous-graphe pour VRPP et VDC
    plt.subplot(2, 1, 1)
    plt.plot(RL_values, vr_pp_array, label=f'VRPP C1 = {C1} Farads')
    plt.plot(RL_values, vdc_array, label=f'VDC C1 = {C1} Farads')
    plt.xlabel('RL (Ohms)')
    plt.ylabel('Tension de sortie (V)')
    plt.title('Tension de sortie V rectifié et filtré en fonction de RL')
    plt.legend()
    plt.grid(True)

    # Sous-graphe pour Ripple Factor
    plt.subplot(2, 1, 2)
    plt.plot(RL_values, ripple_factor_array, label=f'Ripple Factor C1 = {C1} Farads', color='green')
    plt.xlabel('RL (Ohms)')
    plt.ylabel('Ripple Factor')
    plt.title(f'Ripple Factor en fonction de RL pour C1 = {C1} Farads')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()
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


def calculateVripple_peakpeak(C, RL):
    vp_rect, frect = getRectificationValues("full_rectifier", 10, 50)
    vr_pp = vp_rect * (1 / (frect * RL * C))
    vdc = vp_rect * (1 - 1 / (2 * frect * RL * C))
    ripple_factor = vr_pp / vdc

    print(
        f"RL={RL},C={C},vp_rect = {vp_rect}, frect = {frect}, vripple_pp = {vr_pp},vDC={vdc},ripple_factor={ripple_factor}")
    return [vr_pp, vdc, ripple_factor]
def calculateVripple_peakpeak_pourcentage(C, RL):
    vp_rect, frect = getRectificationValues("full_rectifier", 10, 50)
    vr_pp = vp_rect * (1 / (frect * RL * C))
    vdc = vp_rect * (1 - 1 / (2 * frect * RL * C))
    ripple_factor = 100*(vr_pp / vdc)

    print(
        f"RL={RL},C={C},vp_rect = {vp_rect}, frect = {frect}, vripple_pp = {vr_pp},vDC={vdc},ripple_factor={ripple_factor}")
    return [vr_pp, vdc, ripple_factor]

def calculateVoutRegulateur(R1, R2):
    # APROXIMATIVE vout_reg=1.25*(1+R2/R1)
    vout_reg = 1.25 * (1 + R2 / R1) + R2 * 50e-6
    vin_filtre = vout_reg + 4
    print(f"R1={R1},R2 ={R2},vout_reg = {vout_reg},vin_filtre ={vin_filtre} \n")

    return [vout_reg, vin_filtre]


def Main():
    calculateVripple_peakpeak(2000e-6, 220)
    calculateVoutRegulateur(330, 990)
    # drawCurve(500,3)
    # drawCurve(300,3)
    # drawCurve(220,2)
    drawCurveRectifier(100e-6)


if __name__ == "__main__":
    Main()
