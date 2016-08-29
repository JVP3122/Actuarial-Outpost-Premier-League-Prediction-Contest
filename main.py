import pandas as pd
import numpy as np

df = pd.read_excel('AOPremLeague.xlsx',sheetname='AOPremLeague')

table = np.empty([20,1])
table = ['Manchester City','Chelsea','Manchester United','Everton','Hull City','Middlesbrough','Tottenham Hotspur','Arsenal','Leicester City',
                     'West Bromwich Albion','Liverpool','West Ham United','Burnley','Swansea City','Southampton','Sunderland','Crystal Palace','Watford','Bournemouth',
                     'Stoke City']

output_columns = ['Entry','Total',
                  'TB1','TB2','TB3','TB4','TB5','TB6','TB7','TB8','TB9','TB10','TB11','TB12','TB13','TB14','TB15','TB16','TB17','TB18','TB19','TB20',
                  'TBVal1', 'TBVal2', 'TBVal3', 'TBVal4', 'TBVal5', 'TBVal6', 'TBVal7', 'TBVal8', 'TBVal9','TBVal10', 'TBVal11', 'TBVal12', 'TBVal13', 'TBVal14', 'TBVal15', 'TBVal16', 'TBVal17', 'TBVal18', 'TBVal19', 'TBVal20']

team_val = pd.DataFrame(index=table,columns=df.columns.values)

standings = pd.DataFrame(columns=output_columns)

standings['Entry'] = df.columns.values

for entry in df.columns.values:
    total_val = 0
    row = 0
    for team in table:
        table_difference = abs(float(table.index(team)) - float(df[entry].loc[df[entry] == team].index.values))/2
        if row == 0:
            team_val.ix[row, entry] = table_difference
        else:
            team_val.ix[row,entry] = team_val.ix[row-1,entry] + table_difference
        total_val += table_difference
        row += 1

    standings['Total'][standings['Entry'] == entry] = total_val

for row in range(len(standings)):
    for col in range(20,len(output_columns)-2):
        standings.ix[row,col+2] = team_val.ix[col-20,row]

for row in range(len(standings)):
    for col in range(len(output_columns)-22):
        standings.ix[row,col+2] = df.ix[col,row]

del output_columns[0]
del output_columns[1:21]

value_columns = ['TBVal1', 'TBVal2', 'TBVal3', 'TBVal4', 'TBVal5', 'TBVal6', 'TBVal7', 'TBVal8', 'TBVal9','TBVal10', 'TBVal11', 'TBVal12', 'TBVal13', 'TBVal14', 'TBVal15', 'TBVal16', 'TBVal17', 'TBVal18', 'TBVal19', 'TBVal20']

standings.sort_values(output_columns,inplace=True)

standings.reset_index(inplace=True,drop=True)

standings.drop(value_columns,axis=1,inplace=True)

standings.to_excel('standings.xlsx',sheet_name='AOPremLeague')
print standings