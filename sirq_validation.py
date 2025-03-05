#!/usr/bin/env python3
# SIRQ Validation Script
import numpy as np
import matplotlib.pyplot as plt
import os

RIEMANN_ZEROS = [14.1347, 21.0220, 25.0109]
RESULTS_DIR = "validation_results"

def correlate(freq):
    scaled = freq / 10
    distances = [abs(scaled - z) for z in RIEMANN_ZEROS]
    nearest = min(distances)
    return 1 / (1 + 10 * nearest)

def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    freqs = [160.2, 153.9]  # Esempio BPFI
    corrs = [correlate(f) for f in freqs]
    plt.plot(freqs, corrs, 'o-')
    plt.savefig(f"{RESULTS_DIR}/validation_summary_6205.png")
    plt.close()

if __name__ == "__main__":
    main()
