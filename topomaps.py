#!/usr/bin/env python
#activate mne
import mne
import mne.channels
import mne.viz
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import gridspec
import numpy as np
import pandas as pd
import string

#from matplotlib.colors import LinearSegmentedColormap, ListedColormap, Colormap


bands = {"Delta" : "0 - 3.5Hz",
         "Theta" : "4 - 7.5Hz",
         "Alpha" : "8 - 12.5Hz",
         "LowBeta" : "13 - 14.5Hz",
         "UpperBeta" : "15 - 17.5Hz",
         "HighBeta" : "18 - 29.5Hz",
         "Gamma" : "30 - 40Hz",
         "CombinedBeta" : "13-30Hz"}

def expand_camel(str):
    "Expands a camel notation string"
    word = str[0]
    for char in str[1:]:
        if char in string.ascii_lowercase:
            word += char
        else:
            word += " "
            word += char
    return word


# Read the data
data = pd.read_csv("correlations_channel_band_eyes_closed.csv")
font = {'fontname' : 'FreeSans',
        'fontweight' : 'normal',
        'fontsize' : 15}


fontbold = {'fontname' : 'FreeSans',
            'fontweight' : 'bold',
            'fontsize' : 16}


plt.rcParams['font.sans-serif'] = ['FreeSans']

fig = plt.figure(figsize=(13, 5))
#fig = plt.figure(figsize=(26, 10))
i = 1

for task in ["Vocabulary", "Maps"]:
    sub = data.loc[lambda x: x.material == task]
    print(task)
    gs = gridspec.GridSpec(2, 6, width_ratios=[1, 1, 1, 1, 1, 0.15]) 
    for band in ['Theta', 'Alpha', 'Low Beta', 'Upper Beta', 'High Beta']:
        subsub = sub.loc[lambda x: x.Band == band]
        montage = mne.channels.make_standard_montage(kind="standard_1020")
        print(list(subsub.Channel))
        info = mne.create_info(ch_names = list(subsub.Channel),
                               sfreq = 128.0,
                               ch_types = "eeg",
                               montage = montage)
        if (i == 6):
            i = i + 1

        axs = plt.subplot(gs[i-1])
        f=mne.viz.plot_topomap(data = subsub.r, 
                               axes = axs,
                               pos = info,
                               mask = np.array([True for x in subsub.r]).reshape((14,1)),
                               vmin = -0.5,
                               vmax = +0.5,
                               show = False,
                               show_names = True,
                               res = 1000,
                               names = subsub.Channel,
                               outlines = "head",
                               contours = 10,
                               image_interp = "nearest",
                               cmap = plt.get_cmap("RdBu_r"),
                               mask_params = dict(marker='o', markerfacecolor='w',
                                                  markeredgecolor='k', linewidth=0,
                                                  markersize=14))
            
        bname = band.replace("_", "")
        if i < 6:
            if i == 3:
                plt.title("Vocabulary", **fontbold)
        
        elif i > 6:
            if i == 9:
                plt.title("Maps", **fontbold)
            axs.set_xlabel(expand_camel(bname), **font)
            
        i = i + 1

    axs = plt.subplot(gs[5])
    norm = mpl.colors.Normalize(vmin=-0.5, vmax=0.5)
    cb1 = mpl.colorbar.ColorbarBase(axs, cmap=plt.get_cmap("RdBu_r"), #antelope,
                                    norm=norm,
                                    orientation='vertical')
    cb1.set_label(r"""Correlation with $\alpha$""", **font)
    plt.tight_layout()        
    
fig.savefig("topo_correlations_eyes_closed.png")

