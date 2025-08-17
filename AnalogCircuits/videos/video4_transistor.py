import matplotlib.pyplot as plt
import numpy as np

# Années et nombre approximatif de transistors dans des processeurs emblématiques
years = np.array([
    1971, 1974, 1978, 1982, 1985, 1989, 1993, 1997,
    1999, 2002, 2006, 2008, 2012, 2017, 2020, 2023
])

transistor_counts = np.array([
    2300,          # Intel 4004 (1971)
    6000,          # Intel 8080 (1974)
    29000,         # Intel 8086 (1978)
    120000,        # Intel 80286 (1982)
    275000,        # Intel 80386 (1985)
    1180000,       # Intel 80486 (1989)
    3100000,       # Pentium (1993)
    7500000,       # Pentium II (1997)
    24000000,      # Pentium III (1999)
    220000000,     # Pentium 4 (2002)
    291000000,     # Intel Core 2 (2006)
    2300000000,    # Nehalem (2008)
    5000000000,    # Ivy Bridge (2012)
    10000000000,   # Skylake (2017)
    11800000000,   # Tiger Lake (2020)
    58000000000    # Apple M2 (2023)
])

# Création du graphique
plt.figure(figsize=(12, 6))
plt.plot(years, transistor_counts, marker='o', linestyle='-', color='green', label="Nombre de transistors")
plt.yscale("log")  # Échelle logarithmique pour mieux visualiser l'évolution exponentielle
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.title("Loi de Moore : évolution du nombre de transistors (1971–2023)")
plt.xlabel("Année")
plt.ylabel("Nombre de transistors (log10)")
plt.legend()
plt.tight_layout()
plt.show()