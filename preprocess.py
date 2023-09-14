"""Process input txt files from CHI software into usable data."""
import pandas as pd
import re
import os

rmFiles = []

def prep(FileInput):
      File = FileInput
      csvFile = File[:-4]+'.csv'
      txtFile = File[:-4]+'temp'+'.txt'
      csvFileFinalized = File[:-4]+'Final'+'.csv'
      ch = "Current/A\n"
      rmFiles.append(csvFile)
      rmFiles.append(txtFile)
      rmFiles.append(csvFileFinalized)

      with open(File, 'r') as content:
            with open(txtFile,'w') as outcontent:
                  txt = content.read()
                  newtxt = re.sub('.*'+ch,'',txt, flags = re.DOTALL)
                  outcontent.write(newtxt)

      dataframe = pd.read_csv(txtFile, delimiter = ',')
      dataframe.to_csv(csvFile, index = False)

      with open(csvFile, 'r')as fileone:
            with open(csvFileFinalized, 'w') as filetwo:
                  material = fileone.readlines()[1:]
                  filetwo.writelines(material)
                  return csvFileFinalized


def rmTemp():
      for file in rmFiles:
            os.remove(file)