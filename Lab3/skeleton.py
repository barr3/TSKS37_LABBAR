import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Given parameters
N_MC = 10
R = [1,2,3]
SIGMA2 = [0,10,20]
ALPHA = 0.01
GAMMA = 0.5
NUM_ITER = 25
T_RECONSTRUCT = 0.25
T_EDGE = 0.35

# ======================================================= #
# Load image here.
# ------------------------------------------------------- #

# ======================================================= #
# Convert to gray scale here.
# ------------------------------------------------------- #

# ======================================================= #
# Detect edges here.
# ------------------------------------------------------- #

# ======================================================= #
# Reproduce figure with image, gray scale and edges here.
# ------------------------------------------------------- #

# ======================================================= #
# Compress and reconstruct here, store the 9 reconstructed 
# images.
# ------------------------------------------------------- #

# ======================================================= #
# Run Monte Carlo simulation here to compute the average 
# error for each case.
for n in range(N_MC):
# EVERY RANDOM VARIABLE HAS TO BE CREATED INSIDE THIS LOOP
	for r in R:
		pass
		for sigma_2 in SIGMA2:
			print(r, sigma_2)
			# ================================================= #
			# Compress here
			# ------------------------------------------------- #
			
			# ================================================= #
			# Reconstruct here
			for i in range(NUM_ITER):
				pass
			# ------------------------------------------------- #
# ------------------------------------------------------- #

# ======================================================= #
# 3x3 sub plot here.
# ------------------------------------------------------- #