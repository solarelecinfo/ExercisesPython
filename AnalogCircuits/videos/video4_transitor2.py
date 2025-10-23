import matplotlib.pyplot as plt
import numpy as np

# Données réelles (années et nombre de transistors dans certains processeurs)
years = np.array([
    1971, 1974, 1978, 1982, 1985, 1989, 1993, 1997,
    1999, 2002, 2006, 2008, 2012, 2017, 2020, 2023
])
transistor_counts = np.array([
    2300, 6000, 29000, 120000, 275000, 1180000, 3100000, 7500000,
    24000000, 220000000, 291000000, 2300000000, 5000000000,
    10000000000, 11800000000, 58000000000
])
processors = [
    "Intel 4004", "Intel 8080", "Intel 8086", "80286", "80386",
    "80486", "Pentium", "Pentium II", "Pentium III", "Pentium 4",
    "Core 2", "Nehalem", "Ivy Bridge", "Skylake", "Tiger Lake", "Apple M2"
]

# Courbe idéale selon la loi de Moore (doublement tous les 2 ans)
moore_start_year = 1971
moore_years = np.arange(1971, 2024, 1)
moore_transistors = 2300 * 2 ** ((moore_years - moore_start_year) / 2)

# Tracé du graphe
plt.figure(figsize=(14, 7))
plt.plot(years, transistor_counts, marker='o', linestyle='-', color='green', label="Processeurs réels")
plt.plot(moore_years, moore_transistors, linestyle='--', color='blue', label="Loi de Moore (doublement/2 ans)")
plt.yscale("log")

# Annotations des processeurs
for x, y, label in zip(years, transistor_counts, processors):
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8)

plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.title("Loi de Moore vs Évolution réelle des transistors (1971–2023)")
plt.xlabel("Année")
plt.ylabel("Nombre de transistors (échelle logarithmique)")
plt.legend()
plt.tight_layout()
plt.show()
