# Plotting cyclic voltammetry data from CHI software

Process cyclic voltammetry data from CHI software in publishable quality.

1. [How to download everything.](#how-to-download-everything-personal-preference-on-virtual-env-setup)
2. [Setting up Python, Mamba, and virtual environments](#setting-up-python-mamba-and-virtual-environments)
3. [Downloading the CV Plot CLI program](#downloading-the-cv-plot-cli-program)
4. [Running the CV plotter](#running-the-cv-plotter)
5. [Arguments for cvplot.py](#arguments-for-cvplotpy)
6. [Arguments for multiplot.py](#arguments-for-multiplotpy)
7. [Citations](#citations)
8. [Known Limitations](#known-limitations)


## How to download everything (personal preference on virtual env setup)

*Note*: If you are familiar with python virtual environments, you can ignore the first section on setting up virtual environments, save **step 6** for package dependencies. Personally, I prefer to use Mamba for my virtual environments, which is a conda wrapper (and what I will write about below). If you are unfamiliar with virtual environments, just know that this will help keep dependencies separate and prevent possible problems in the future.

### Setting up Python, Mamba, and virtual environments
- *Note*: This virtual environment is the same as for my [uv-vis-plot](https://github.com/BardenB/uv-vis-plot).

1. Download [python](https://www.python.org/downloads/) for your appropriate OS. Default settings should be fine.
2. Download [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge) for your appropriate OS. Follow any instructions. Default settings should be fine. From this point forward, I use the miniforge prompt that comes with the install but you can use any command prompt.
3. If you ever get lost in setting up Mambaforge, check out their [documentation](https://mamba.readthedocs.io/en/latest/index.html), or reach out to me.
4. It is time to create our virtual environment that will be used for this program. You can use `mamba create -n plotenv` which will create a virtual environment called `plotenv`. You can name it whatever you want. I suggest keeping environment names easy.
    - If you forget the name of the environments you have, type `mamba env list` and this list will show you what virtual environments are managed by Mamba/conda.
    - At this stage, you could also add the packages to install as you create the environment, but we will do that in a later step.
5. To activate the virtual environment we want to use, simply type `mamba activate plotenv` and allow the environment to activate.
    - At the end of the session, I feel it good habit to deactivate the environment, although it is not necessary. To deactivate, type `mamba deactivate`
6. Now it is time to install packages we need into this environment that are not automatically included in base python. Type the following `mamba install matplotlib pandas numpy` to install these three packages. Follow on screen prompts.
    - This will download all of the most recent versions of these packages, which all work.


### Downloading the CV Plot CLI program
1. If you know git and have a GitHub account, you can just clone the repo and skip to the next section.
2. If you do not know git and/or don't have a GitHub account, there is a green button that says `Code` close to the top right corner. Click that button, and then click `download Zip`. Once you do that, unzip the file and you're all set.  
**You do not need a github account to download this program.**

### Running the CV plotter

Once the virtual environment is active and packages installed, it is now possible to run the CV plotting program in order to get your voltammograms.

1. To start, you must make sure your command prompt (whichever you use), is in the directory of the program.  To do that, open the folder you unzipped (in this case, the folder will be named `cv-plot`), and copy the file path. in the command prompt, type `cd` followed by a space followed by pasting the file path. You will most likely have to hit `ctrl + shift + V` rather than a typical paste. Now your command line will be in the correct folder. Depending on where you put it, you might not need the whole file path, but if you're not familiar with command line commands, just do the full path.
2. If you are familiar with CLI programs, you can find the arguments below. Happy plotting!
3. To plot a single CV with all default settings, type `python cvplot.py -f \path\to\input -r \path\to\reference -o \path\to\output` where `\path\to\x` is replaced with the actual paths to the respective txt files. See the `-f` argument below on how to write that out.
    - *Note*: Current limitation: you must have all text files in this directory, and therefore you don't need the full path. This is an easy fix, I'm just lazy.
    - ***Remember that no directory or file can contain a space if you do a full path to the file.***
4. If you hit enter after typing step 3, a plot will be generated and shown on your screen. This is your $Fc/Fc^+$ reference spectra. You should know which peaks are your ferrocene, and you only need to know those two numbers.  Write them down or memorize them. 
5. Once you have these two numbers, simply close that plot window. **You cannot move on before closing this window.** The program will continue and ask you for those two numbers, one at a time. Type in one number, hit enter, type the second, and hit enter again when asked.
6. If you want to overlay multiple sets of data, you can use `multiplot.py` instead of `cvplot.py`. See notes on arguments below. Otherwise, it works exactly the same.
7. Be aware that each time you run the same input file, it will automatically overwrite the output png to the most recent one. If you do not want that to happen, change the name of the previous run first. ***Future update, but not high priority***
8. Once the plot is to your liking, you can simply use the png however you want. Post-processing can be done however you like (I know most of us use PowerPoint).
    - I currently have dpi set to 300, which is plenty for most purposes. You can change it if you want.
9. Happy plotting!

## Arguments for cvplot.py

- `-f` or `--file` <span style = "color :red"> **Required**</span>
    - You must include the file name here. If it is not located in the same directory as `UVVisCLI.py`, you must put the full path. On Windows, right click on the file you want to process and click `Copy as path` or `Ctrl + shift + c`. You can leave the quotes when pasted. This argument can take one or more files to process. Separate files by a space only.
- `-o` or `--outputFile` <span style = "color :red"> **Required**</span>
    - you can rename the output plot to whatever you feel appropriate here.
- `-r` or `--reference-file` <span style = "color :red"> **Required**</span>
    - This is the file name of the ferrocene scan. 
- `-c` or `--color`
    - The color of the plotted data. This does not change axes, only data.
    - example: `-r purple`
    - Default is blue
- `-s` or `--size`
    - This flag allows you to update the thickness of the data points.
    - Default is 12, however I have found 8-16 all look okay.

## Arguments for multiplot.py

There are only a couple changes between `cvplot.py` and `multiplot.py` that you need to be aware of.
- `-f` or `--files` <span style = "color :red"> **Required**</span>
    - now, the long flag is files rather than file, and allows for an infinite amount of files (you'll break your computer trying to an infinite amount though).
- `-c` is no longer available as an option, as it automatically cycles through the rainbow.

#### Citations

- If you use this program to produce plots, it would be greatly appreciated to cite by including the github repository as a citation (https://github.com/BardenB/cv-plot). Nothing else asked from me (to stay compliant with MIT I think). 
- Matplotlib requires citing, which can be found [here](https://matplotlib.org/stable/users/project/citing.html).
- pandas requires citing, which can be found [here](https://pandas.pydata.org/about/citing.html).

#### License

Assume MIT license for now, clarification and changes may come in the future if necessary. 

#### Known Limitations
- Files must be in this directory to work, due to the nature of the temp file system I have set up. Sorry.
- Currently, when stacking plots, the color is automatically updated to rotate through the rainbow, plus black. I will change that feature to be customizable IFF people ask.
- Running the same input file will automatically overwrite any plots and data output files that may generate. I will work on a way to update that such that a number or something is added to the end of the file to prevent overwriting. This is not high priority. Just rename if you need to run multiple times.
