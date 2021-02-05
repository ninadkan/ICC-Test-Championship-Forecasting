# Reading an xlsx file and creating an matrix multiplication across. 
import pandas as pd
inputFileName='./ICC-Test-Championship.xlsx'
outputFileName='./result.csv'
dataIndiaEngland = pd.read_excel(inputFileName, sheet_name='India-England-Forecast')
dataIndiaEngland = dataIndiaEngland[['India', 'England',  'India PCT','England PCT']]
dataSAAustralia = pd.read_excel(inputFileName, sheet_name='SouthAfrica-Australia-Forecast')
dataSAAustralia = dataSAAustralia[['South Africa', 'Australia', 'Australia PCT']]
colName='tmp'
dataIndiaEngland[colName]=1
dataSAAustralia[colName]=1
dfOutput= pd.merge(dataIndiaEngland,dataSAAustralia , on=[colName])
dfOutput=dfOutput.drop(colName, axis=1)
dfOutput.to_csv(outputFileName)
   