import preprocess as prep
import scatterCV as CV
import argparse
import ferrocenereference as ref
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.bf'] = 'Arial'
plt.rcParams['font.family'] ='Arial'
plt.rcParams['font.weight'] = 'bold'

parser = argparse.ArgumentParser(
    description="Plot cyclic voltammograms from raw data from CHI.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    prog = 'CV-plot',
    epilog = 'Thank you for using %(prog)s. Please contact Brett with any questions.',
    allow_abbrev= False
)

parser.add_argument(
    '-f',
    '--file',
    type = str,
    default = 'CVTestdata.txt',
    help = 'Choose file to plot CV.',
    required = True
)

parser.add_argument(
    '-o',
    '--outputFile',
    default = 'CVPlot.png',
    type = str,
    help = 'Designate an output file name. Include `.png`',
    required = False
)

parser.add_argument(
    '-r',
    '--reference-file',
    type = str,
    help = 'file name of the Fc/Fc+ CV you are trying to reference with.',
    required = True
)

parser.add_argument(
    '-s',
    '--size',
    type = float,
    default = 2,
    help = 'choose size of data points.'
)

parser.add_argument(
    '-c',
    '--color',
    type = str,
    default = 'Blue',
    help = 'Choose single color for graph.',
    required = False
)

parser.add_argument(
    '-p',
    '--peak-potentials',
    action = 'store_true',
    help = 'will produce a plot to view with peak potentials. not publishable quality.',
    required = False
)

args = parser.parse_args()

ref.fcReference(args.reference_file, wait_for_plot=True)
peak1 = float(input('Fc peak 1: '))
peak2 = float(input('Fc peak 2: '))
FileInput = args.file

File = prep.prep(FileInput)
CV.PlotCV(File, args.outputFile, peak1, peak2, args.size, color = args.color)

if args.peak_potentials:
    ydata, df = ref.dataproc(args.file)

    x = df['potential']
    y = df['current']

    xnew = CV.shifting(df, peak1, peak2)

    filteredMaxPotentials, filteredMinPotentials, filteredMaxIndices, filteredMinIndices = ref.maxmin(ydata,xnew)
    
    plt.figure()
    plt.plot(xnew, y, label='Original Data')
    plt.gca().invert_xaxis()
    ref.peakPick(ydata, filteredMaxPotentials, filteredMaxIndices, filteredMinPotentials, filteredMinIndices)
    plt.show()

prep.rmTemp()
