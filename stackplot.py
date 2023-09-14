import preprocess as prep
import scatterCV as CV
import argparse
import ferrocenereference as ref
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import pandas as pd

plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.bf'] = 'Arial'
plt.rcParams['font.family'] ='Arial'
plt.rcParams['font.weight'] = 'bold'

parser = argparse.ArgumentParser(
    description="Plot cyclic voltammograms from raw data from CHI.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    prog='CV-plot',
    epilog='Thank you for using %(prog)s. Please contact Brett with any questions.',
    allow_abbrev=False
)

parser.add_argument(
    '-f',
    '--files',
    type=str,
    nargs='+',
    help='Choose file(s) to plot CV.',
    required=True
)

parser.add_argument(
    '-o',
    '--outputFile',
    default='CVPlot.png',
    type=str,
    help='Designate an output file name. Include `.png`',
    required=False
)

parser.add_argument(
    '-r',
    '--reference-files',
    nargs = '+',
    type=str,
    help='file name of the Fc/Fc+ CV you are trying to reference with.',
    required=True
)

parser.add_argument(
    '-s',
    '--size',
    type = float,
    default = 2,
    help = 'choose size of data points.',
    required = False
)

parser.add_argument(
    '-d',
    '--stack',
    type = float,
    default = 3e-5,
    help = 'Set y offset between each plot.',
    required = False
)

args = parser.parse_args()

def get_color_cycle(colors):
    color_cycle = iter(colors)
    return color_cycle

def multiRef(referenceFiles):
    refList = []
    for reference in referenceFiles:
        ref.fcReference(reference, wait_for_plot=True)
        peak1 = float(input(f'Fc peak 1 for plot: '))
        peak2 = float(input(f'Fc peak 2 for plot: '))
        refList.append((peak1, peak2))
    return refList

def main():

    colors = ['red', 'orange', 'green', 'green', 'blue', 'violet', 'black']
    color_cycle = get_color_cycle(colors)

    yShift = 0
    references = multiRef(args.reference_files)

    for i, (FileInput, color, refList) in enumerate(zip(args.files, colors, references)):

        color = next(color_cycle)
        File = prep.prep(FileInput)

        peak1, peak2 = refList

        headers = ['potential','current']
        df = pd.read_csv(File, names = headers)
        x = CV.shifting(df, peak1, peak2)
        y = df['current'] + yShift

        scatter = plt.scatter(x, y, color = color, s = args.size)
        yShift += args.stack

        ax = scatter.axes
        ax.xaxis.set_major_locator(MultipleLocator(0.5))
        ax.xaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))
        ax.yaxis.set_visible(False)
        for axis in ['top','right','left']:
            ax.spines[axis].set_visible(False)
        ax.spines['bottom'].set_linewidth(2)
        ax.set_xticklabels(ax.get_xticks(), size = 16)

    ax.add_artist(CV.scale())
    plt.gca().invert_xaxis()
    ax.set_xlabel('Potential (V)', size = 16, weight = 'bold')
    plt.savefig(args.outputFile, format='png', dpi = 300, bbox_inches = 'tight')
    plt.close()

    prep.rmTemp()


if __name__ == "__main__":
    main()
