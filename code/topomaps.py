#!/usr/bin/env python
import mne
import sys
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import gridspec
import numpy as np
import pandas as pd
import string


if __name__ == "__main__":
    infile = sys.argv[1]
    # Read the data
    data = pd.read_csv(infile)
    rtype = pd.unique(data.Recording)[0]   # Eyes Open / Eyes Closed
    font = {'fontname' : 'FreeSans',
            'fontweight' : 'normal',
            'fontsize' : 15}


    fontbold = {'fontname' : 'FreeSans',
                'fontweight' : 'bold',
                'fontsize' : 16}


    plt.rcParams['font.sans-serif'] = ['FreeSans']

    fig = plt.figure(figsize=(13, 6))

    i = 1

    for task in ["Vocabulary", "Maps"]:
        sub = data.loc[lambda x: x.material == task]
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
                    plt.title("%s\n%s" % ("Vocabulary", rtype), **fontbold)
        
            elif i > 6:
                if i == 9:
                    plt.title("%s\n%s" % ("Maps", rtype), **fontbold)
                axs.set_xlabel(band, **font)
            
            i = i + 1

        axs = plt.subplot(gs[5])
        norm = mpl.colors.Normalize(vmin=-0.5, vmax=0.5)
        cb1 = mpl.colorbar.ColorbarBase(axs, cmap=plt.get_cmap("RdBu_r"), #antelope,
                                    norm=norm,
                                    orientation='vertical')
        cb1.set_label(r"""Correlation with $\alpha$""", **font)
        plt.tight_layout()        
    
    fig.savefig("topo_correlations_%s.png" % (rtype.lower().replace(" ", "_")))
