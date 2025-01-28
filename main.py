import pandas as pd
import csv


def convert():
    excel_file = pd.read_excel("test.xlsx")
    excel_file.to_csv("test.csv", index=None, header=True)
    df = clear_csv("test.csv")
    clear_dop(df)
    clear_usd(df)


def clear_csv(filename):
   csv_file = pd.read_csv(filename, skiprows=1)
   print(csv_file)

   data = pd.DataFrame(csv_file)
   print(data)
   
   # drop first 2 colums
   cf = data.drop(data.columns[[0, 1, 4]], axis=1)
   print(cf)

   # rename columns
   cf = cf.rename(columns={cf.columns[0]: 'date', cf.columns[1]: 'payee', cf.columns[2]: 'memo', cf.columns[4]: 'outflow', cf.columns[5]: 'inflow'})
   print(cf)

   # remove negatives from inflow column
   outflows = cf['inflow']
   new_outflows = outflows.apply(abs)

   cf['inflow'] = new_outflows
   print(cf)

   return cf

def clear_dop(df):
    # drop non RD transactions
    cr = df.loc[df['Moneda'] == 'RD']
    cf = cr.drop('Moneda', axis=1)
    cf.to_csv('test-dop.csv',index=False)

def clear_usd(df):
    # drop non US transactions
    cr = df.loc[df['Moneda'] == 'US']
    cf = cr.drop('Moneda', axis=1)
    cf.to_csv('test-usd.csv',index=False)

if __name__ == '__main__':
    convert()
    


