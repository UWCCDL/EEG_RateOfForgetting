#!/usr/bin/env python
import mne
import mne.channels
import mne.viz
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import gridspec
import numpy as np
import pandas as pd
import string


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

i = 1

for task in ["Vocabulary", "Maps"]:
    sub = data.loc[lambda x: x.material == task]
    gs = gridspec.GridSpec(2, 6, width_ratios=[1, 1, 1, 1, 1, 0.15]) 

    for band in ['Theta', 'Alpha', 'Low Beta', 'Upper Beta', 'High Beta']:
        subsub = sub.loc[lambda x: x.Band == band]
        montage = mne.channels.make_standard_montage(kind="standard_1020")
        info = mne.create_info(ch_names = list(subsub.Channel),
                               sfreq = 128.0,
                               ch_types = "eeg",
                               montage = montage)
        if (i == 6):
            i = i + 1

        axs = plt.subplot(gs[i-1])
        f = mne.viz.plot_topomap(data = subsub.r, 
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
            
        
        if i < 6:
            if i == 3:
                plt.title("Vocabulary", **fontbold)
        
        elif i > 6:
            if i == 9:
                plt.title("Maps", **fontbold)
            axs.set_xlabel(band, **font)
            
        i = i + 1

    axs = plt.subplot(gs[5])
    norm = mpl.colors.Normalize(vmin=-0.5, vmax=0.5)
    cb1 = mpl.colorbar.ColorbarBase(axs, cmap=plt.get_cmap("RdBu_r"), #antelope,
                                    norm=norm,
                                    orientation='vertical')
    cb1.set_label(r"""Correlation with $\alpha$""", **font)
    plt.tight_layout()        
    
fig.savefig("topo_correlations_eyes_closed.png")

