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


# this is chart 1 for a download speed column
plt.figure(figsize=(10, 6))
plt.hist(df['d_1'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.title("Distribution of d_1 (Download Speed)")
plt.xlabel("Download Speed (Mbps)")
plt.ylabel("Frequency")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Save the histogram in the charts folder i made
plt.savefig("charts/d1_histogram.png")
plt.show()

# Chart 2: Boxplot to compare a bumch of speeds
d_columns = [f'd_{i}' for i in range(1, 9)]  # List: ['d_1', 'd_2', ..., 'd_8']

plt.figure(figsize=(12, 8))
# Create a boxplot for each of my columns
plt.boxplot([df[col] for col in d_columns], tick_labels=d_columns, patch_artist=True)
plt.title("Boxplot Comparison of d_1 to d_8 (Download Speeds)")
plt.xlabel("Column")
plt.ylabel("Download Speed (Mbps)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Save the boxplot as a PNG file in the 'charts' folder
plt.savefig("charts/d_columns_boxplot.png")
plt.show()

####ALLLLL DONNENENENENE