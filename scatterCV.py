import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import matplotlib.offsetbox
from matplotlib.lines import Line2D
import pandas as pd
from statistics import mean

class AnchoredVScaleBar(matplotlib.offsetbox.AnchoredOffsetbox):
    def __init__(self, size=1, extent = 0.03, label="", loc=2, ax=None,
                pad=0.4, borderpad=0.5, ppad = 0, sep=2, prop=None, 
                frameon=True, linekw={}, **kwargs):
        if not ax:
            ax = plt.gca()
        trans = ax.get_yaxis_transform()
        size_bar = matplotlib.offsetbox.AuxTransformBox(trans)
        line = Line2D([0,0],[size,0], **linekw)
        hline1 = Line2D([-extent/2.,extent/2.],[0,0], **linekw)
        hline2 = Line2D([-extent/2.,extent/2.],[size,size], **linekw)
        size_bar.add_artist(line)
        size_bar.add_artist(hline1)
        size_bar.add_artist(hline2)


        txt = matplotlib.offsetbox.TextArea(label, textprops = {'fontsize': 16})

        self.vpac = matplotlib.offsetbox.VPacker(children=[size_bar,txt],  
                                align="center", pad=ppad, sep=sep) 
        matplotlib.offsetbox.AnchoredOffsetbox.__init__(self, loc, pad=pad, 
                borderpad=borderpad, child=self.vpac, prop=prop, frameon=frameon,
                **kwargs) 

def referenceCV(peak1,peak2):
    numbers = [peak1,peak2]
    average = mean(numbers)
    return average

def PlotCV(File, outputFile, peak1,peak2):
    file = File
    output = outputFile
    headers = ['potential','current']
    df = pd.read_csv(file, names = headers)

    x = df['potential']
    y = df['current']
    
    df['shiftedPotential'] = df['potential'].apply(lambda x:x - referenceCV(peak1,peak2))
    scatter = plt.scatter(df['shiftedPotential'],y, s = 8, color = 'blue')
    ax = scatter.axes
    plt.gca().invert_xaxis()
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_visible(False)
    ob = AnchoredVScaleBar(size=1e-5, label="10 uA", loc=2, frameon=False,
                    pad=1,sep=4, linekw=dict(color="Black"))

    ax.add_artist(ob)
    for axis in ['top','right','left']:
        ax.spines[axis].set_visible(False)
    ax.spines['bottom'].set_linewidth(2)
    ax.set_xticklabels(ax.get_xticks(), size = 16)
    plt.savefig(output, format='png', dpi = 300, bbox_inches = 'tight')