# dissonance_quantification.py
# Zhihan Yang
# 11 Feb 2019
# please run the project using Atom and Hydrogen for the use of Jupyter kernels

# <codecell>
from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
# import inspect
# inspect.getfile(pd)

# <codecell>
# frequencies present in each tone clusters
g1_freqs = [466.1637615, 479.8234024, 493.8833013, 508.3551866, 523.2511306, 538.5835591, 554.365262, 570.609404, 587.3295358, 604.5396049, 622.2539674, 640.4874005]
g2_freqs = [587.3295358, 604.5396049, 622.2539674, 640.4874005, 659.2551138, 678.5727632, 698.4564629, 718.9227994, 739.9888454, 761.6721737, 783.990872, 806.963558]
g3_freqs = [554.365262, 570.609404, 587.3295358, 604.5396049, 622.2539674, 640.4874005, 659.2551138, 678.5727632, 698.4564629, 718.9227994, 739.9888454, 761.6721737]
g4_freqs = [783.990872, 806.963558, 830.6093952, 854.9481082, 880, 905.7859682, 932.327523, 959.6468047, 987.7666025, 1016.710373, 1046.502261, 1077.167118]
g5_freqs = [415.3046976, 427.4740541, 440, 452.8929841, 466.1637615, 479.8234024, 493.8833013, 508.3551866, 523.2511306, 538.5835591]
g6_freqs = [880, 905.7859682, 932.327523, 959.6468047, 987.7666025, 1016.710373, 1046.502261, 1077.167118, 1108.730524, 1141.218808]
g7_freqs = [329.6275569, 339.2863816, 349.2282314, 359.4613997, 369.9944227, 380.8360868, 391.995436, 403.481779, 415.3046976, 427.4740541]
g8_freqs = [391.995436, 403.481779, 415.3046976, 427.4740541, 440, 452.8929841, 466.1637615, 479.8234024]

# <codecell>
# frequencies present in each section, combinations of tone clusters
s1_freqs = g5_freqs
s2_freqs = g3_freqs + g5_freqs
s3_freqs = g1_freqs + g3_freqs + g5_freqs + g8_freqs
s4_freqs = g1_freqs + g3_freqs + g6_freqs + g8_freqs
s5_freqs = g1_freqs + g3_freqs + g6_freqs + g7_freqs + g8_freqs
s6_freqs = g2_freqs + g3_freqs + g6_freqs + g7_freqs + g8_freqs
s7_freqs = g2_freqs + g4_freqs + g6_freqs + g7_freqs + g8_freqs

# <codecell>
# convert list of frequencies in each section to pandas DataFrames
s1_freqs_df = pd.DataFrame(s1_freqs).T
s2_freqs_df = pd.DataFrame(s2_freqs).T
s3_freqs_df = pd.DataFrame(s3_freqs).T
s4_freqs_df = pd.DataFrame(s4_freqs).T
s5_freqs_df = pd.DataFrame(s5_freqs).T
s6_freqs_df = pd.DataFrame(s6_freqs).T
s7_freqs_df = pd.DataFrame(s7_freqs).T

# <codecell>
# define score function according to Hermann von Helmholtz's definition of roughness / dissonance
def score(x, y):
    result = round(abs(float(x) - float(y)),2)
    if result <= 32:
        return result / 33
    elif result <= 132:
        return -(1/(132-33)) * result + 4/3
    else:
        return 0

def abs_between(x, y):
    return abs(x - y)

# <codecell>
# obtain only the scores in the upper triangle of the "correlation" matrix
g1_corr = pd.DataFrame(g1_freqs).T.corr(method=abs_between)
new = []
for i in np.triu(g1_corr,k=1).flatten():
    if i!=0:
        new.append(i)

# <codecell>
# plot a histogram of all possible frequency differences with quarter-tones
plt.hist(new, bins=8, rwidth=0.9)
plt.title("All Possible Frequency Differences with Quarter-Tones")
plt.xlabel("Bins of Frequency Differences Between Pitches")
plt.ylabel("Counts")
plt.xticks(np.arange(0, 181, 20))
plt.yticks(np.arange(0, 21, 2))
plt.savefig("Histogram of Frequency Differences with Quarter-Tones")
plt.show()

# <codecell>
# plot a histogram of all possible frequency differences without quarter-tones
g1_e_freqs = [466.1637615, 493.8833013, 523.2511306, 554.365262, 587.3295358, 622.2539674]

g1_e_corr = pd.DataFrame(g1_e_freqs).T.corr(method=abs_between)
new_e = []
for i in np.triu(g1_e_corr,k=1).flatten():
    if i!=0:
        new_e.append(i)

plt.hist(new_e, bins=8, rwidth=0.9)
plt.title("All Possible Frequency Differences with No Quarter-Tones")
plt.xlabel("Bins of Frequency Differences Between Pitches")
plt.ylabel("Counts")
plt.xticks(np.arange(0, 181, 20))
plt.yticks(np.arange(0, 21, 2))
plt.savefig("Histogram of Frequency Differences with No Quarter-Tones")
plt.show()

# <codecell>
# quantify dissonance
s1_corr = s1_freqs_df.corr(method=score)
s2_corr = s2_freqs_df.corr(method=score)
s3_corr = s3_freqs_df.corr(method=score)
s4_corr = s4_freqs_df.corr(method=score)
s5_corr = s5_freqs_df.corr(method=score)
s6_corr = s6_freqs_df.corr(method=score)
s7_corr = s7_freqs_df.corr(method=score)

# <codecell>
# define a function for plotting
def plot_hist_from_corr(corr):
    bins = np.linspace(0, 1, 11) # 11 bin boundaries for 10 buckets
    digitized = np.triu(np.digitize(corr, bins), k=1)

    for_plot=[]
    for i in digitized.flatten():
        if i == 5 or i == 6 or i == 7 or i == 8 or i == 9 or i == 10: # only items above the diagonal
            for_plot.append(i)

    plt.hist(for_plot, rwidth=0.8, bins=np.arange(1, 12)-0.5) # have to be 12, otherwise 11-0.5=10.5, 10s will not actually be allowed
    plt.xticks(np.arange(1, 12)) # to show 10 more clearly
    plt.yticks(np.arange(0, 90, 10))
    plt.show()

# <codecell>
# plot histograms showing distributions of roughness / dissonance across different sections

def easy_plot(corr, n):
    plt.hist(np.array(np.triu(corr, k=1)).flatten(), bins=np.arange(0.1, 1.1, 0.1))
    plt.yticks(np.arange(0, 81, 10))
    plt.xlabel("Roughness")
    plt.ylabel("Counts")
    plt.title("Roughness of Section {0}".format(n))
    plt.savefig("img{0}".format(n))
    plt.show()

easy_plot(s1_corr, 1)
easy_plot(s2_corr, 2)
easy_plot(s3_corr, 3)
easy_plot(s4_corr, 4)
easy_plot(s5_corr, 5)
easy_plot(s6_corr, 6)
easy_plot(s7_corr, 7)

















# end
