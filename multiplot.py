import preprocess as prep
import scatterCV as CV
import argparse
import ferrocenereference as ref
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import pandas as pd


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
    '--reference-file',
    type=str,
    help='file name of the Fc/Fc+ CV you are trying to reference with.',
    required=True
)

parser.add_argument(
    '-s',
    '--size',
    type = float,
    default = 12,
    help = 'choose size of data points.',
    required = False
)

args = parser.parse_args()

def get_color_cycle(colors):
    color_cycle = iter(colors)
    return color_cycle

def main():

    ref.fcReference(args.reference_file, wait_for_plot=True)
    peak1 = float(input('Fc peak 1: '))
    peak2 = float(input('Fc peak 2: '))

    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'black']
    color_cycle = get_color_cycle(colors)

    for FileInput, color in zip(args.files, colors):
        color = next(color_cycle)
        File = prep.prep(FileInput)
        
        headers = ['potential','current']
        df = pd.read_csv(File, names = headers)
        x = CV.shifting(df, peak1, peak2)
        y = df['current']

        scatter = plt.scatter(x, y, color = color, s = args.size)
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

    plt.savefig(args.outputFile, format='png', dpi = 300, bbox_inches = 'tight')
    
    prep.rmTemp()


if __name__ == "__main__":
    main()
