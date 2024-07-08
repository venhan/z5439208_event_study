'''Code challenge quiz 4 - yf_example3 under toolkit project folder'''

'''First step: importing the different modules that is saved in PyCharm under toolkit'''
import os
import toolkit_config as cfg
import yf_example2

'''Second step: Defining the function with its mandatory parameter "year"'''
def qan_prc_to_csv(year):
    tic = 'QAN.AX'
    start=f'{year}-01-01'
    end=f'{year}-12-31'
    pth = os.path.join(cfg.DATADIR, f'qan_prc_{year}.csv')
    df = yf_example2.yf_prc_to_csv(tic=tic, pth=pth, start=start, end=end)

if __name__ == "__main__":
    year = 2020
    qan_prc_to_csv(year)



