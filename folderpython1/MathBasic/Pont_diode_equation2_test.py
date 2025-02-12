import numpy as np
import matplotlib.pyplot as plt


def drawCurve(valeur_max_axe_X):
    R1_values = np.linspace(100, valeur_max_axe_X, 100)
    R2_values = np.linspace(100, valeur_max_axe_X, 100)
    R1, R2 = np.meshgrid(R1_values, R2_values)
    vout_reg = calculateVoutRegulateur(R1, R2)

    # Afficher les statistiques
    print(f"Min de vout_reg: {np.min(vout_reg)}")
    print(f"Max de vout_reg: {np.max(vout_reg)}")
    print(f"Mean de vout_reg: {np.mean(vout_reg)}")
    # Afficher quelques échantillons
    print(f"Échantillons de vout_reg: {vout_reg[0:5, 0:5]}")


    plt.figure(figsize=(10, 6))
    cp = plt.contourf(R1, R2, vout_reg, cmap='viridis')
    plt.colorbar(cp)
    plt.xlabel('R1 (Ohms)')
    plt.ylabel('R2 (Ohms)')
    plt.title('Tension de sortie du régulateur en fonction de R1 et R2')
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
def calculateVripple_peakpeak(C,RL):
    vp_rect, frect = getRectificationValues("full_rectifier", 10, 50)
    vr_pp = vp_rect * (1/(frect*RL*C))
    vdc = vp_rect * (1-1/(2*frect*RL*C))
    ripple_factor= vr_pp/vdc

    print(f"vp_rect = {vp_rect}, frect = {frect}, vripple_pp = {vr_pp},vDC={vdc},ripple_factor={ripple_factor}")
    return [ vr_pp,vdc,ripple_factor ]



def calculateVoutRegulateur(R1,R2):
    # APROXIMATIVE vout_reg=1.25*(1+R2/R1)
    vout_reg=1.25*(1+R2/R1)+R2*50e-6
    vin_filtre=vout_reg+4
    print(f"vout_reg = {vout_reg},vin_filtre ={vin_filtre} \n")

    return vout_reg

def Main():
    calculateVripple_peakpeak(2000e-6,220)
    #calculateVoutRegulateur(220,2400)
    calculateVoutRegulateur(218,2400)
    drawCurve(3000)


if __name__ == "__main__":
    Main()
