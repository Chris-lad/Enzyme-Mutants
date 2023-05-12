import os
import pandas as pd


# constants
FILENAMES = ['AF-A0A3G4RHW3-F1-model_v4', 'AF-P0ABQ4-F1-model_v4', 'AF-P0DP23-F1-model_v4',
             'AF-P04035-F1-model_v4', 'AF-P08397-F1-model_v4', 'AF-P12931-F1-model_v4',
             'AF-P23458-F1-model_v4', 'AF-P35520-F1-model_v4', 'AF-P35557-F1-model_v4',
             'AF-P42898-F1-model_v4', 'AF-P51580-F1-model_v4', 'AF-P60484-F1-model_v4',
             'AF-P63165-F1-model_v4', 'AF-P63279-F1-model_v4', 'AF-Q9ES00-F1-model_v4',
             'AF-Q9H3S4-F1-model_v4', 'AF-Q9NV35-F1-model_v4', 'AF-Q9NZ01-F1-model_v4',
             'AF-Q9Y617-F1-model_v4', 'AF-Q499G7-F1-model_v4']

def main():
    for file in FILENAMES:
        if not os.path.exists(file+'.csv'):
            df = pd.read_csv(file+'.txt', sep='\s+', names=['Chain','Positions','Residues','Distance',
                                                     'Accessibility', 'Torsion'], index_col=False)
            df['Total'] = df['Distance'] + df['Accessibility'] + df['Torsion']
            #print(df)
            df.to_csv(file+'.csv', index=False)
if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()































