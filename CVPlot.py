import preprocess as prep
import scatterCV as CV
import argparse
import ferrocenereference as ref

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
    default = 12,
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

args = parser.parse_args()

ref.fcReference(args.reference_file, wait_for_plot=True)
peak1 = float(input('Fc peak 1: '))
peak2 = float(input('Fc peak 2: '))
FileInput = args.file

File = prep.prep(FileInput)
CV.PlotCV(File, args.outputFile, peak1, peak2, args.size, color = args.color)
prep.rmTemp()