'''
INF601 - Programming in Python
Assignment #
I,     (Jim Pinto)    , affirm that the work submitted for this
assignment is entirely my own. I have not engaged in any form of
academic dishonesty, including but not limited to cheating, plagiarism,
or the use of unauthorized materials. I have neither provided nor
 received unauthorized assistance and have accurately cited all sources
 in adherence to academic standards. I understand that failing to comply
 with this integrity statement may result in consequences, including
 disciplinary actions as determined by my course instructor and
 outlined in institutional policies. By signing this statement,
 I acknowledge my commitment to upholding the principles of academic
 integrity.
'''

import pandas as pd
import matplotlib.pyplot as plt
import os

# Creating the charts folder if it isn't there
if not os.path.exists("charts"):
    os.makedirs("charts")

# Loading the dataset im using
df = pd.read_csv("fcc_broadband.csv")

# Displaying a preview of my dataframe i entered and its columns
print("Dataset Preview:")
print(df.head())
print("\nColumns in the dataset:")
print(df.columns)