### Portfolio Optiimization
### Sean Welleck | 2014
#
# Finds an optimal allocation of stocks in a portfolio,
# satisfying a minimum expected return.
# The problem is posed as a Quadratic Program, and solved
# using the cvxopt library.
# Uses actual past stock data, obtained using the stocks module.
import math
import numpy as np
import pandas as pd
import datetime
import cvxopt
from cvxopt import matrix, solvers
import matplotlib.pyplot as plt
##########################
import warnings
warnings.filterwarnings('ignore')
warnings.warn('DelftStack')
warnings.warn('Do not show this message')
#####################
solvers.options['show_progress'] = False        # !!!

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

#from cvxopt import solvers
#import stocks
import numpy as np
import pandas as pd
import datetime

import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm

# c = cvxopt.matrix([0, -1], tc='d')
# print('c: ', c)
# c = numpy.matrix(c)
# print('c: ', c)
#
# c = cvxopt.matrix([0, -1])
# print('c: ', c)
# G = cvxopt.matrix([[-1, 1], [3, 2], [2, 3], [-1, 0], [0, -1]], tc='d')
# print('G: ', G)
##################
xDir = r'D:\\Users\\ggu\\Documents\\GU\\MultiRiskFactorModel\\DATA\\'
xSPXT = pd.read_csv(xDir + 'xSPXT.txt')
xSPXT['DATE'] = pd.to_datetime(xSPXT['DATE'], format='%m/%d/%Y')
xBondTR = pd.read_csv(xDir + 'xBondTR.txt')
xBondTR['DATE'] = pd.to_datetime(xBondTR['DATE'], format='%m/%d/%Y')
#xBondTR.rename(columns={'LBUSTRUU': 'BondTR'},inplace=True)
xAAPL = pd.read_csv(xDir + 'xAAPL.txt')
xAAPL['DATE'] = pd.to_datetime(xAAPL['DATE'], format='%m/%d/%Y')
xAGG = pd.read_csv(xDir + 'xAGG.txt')
xAGG['DATE'] = pd.to_datetime(xAGG['DATE'], format='%m/%d/%Y')
xCCY = pd.read_csv(xDir + 'xCCY.txt')
xCCY['DATE'] = pd.to_datetime(xCCY['DATE'], format='%m/%d/%Y')
xCOMM = pd.read_csv(xDir + 'xCOMM.txt')
xCOMM['DATE'] = pd.to_datetime(xCOMM['DATE'], format='%m/%d/%Y')
xCREDIT = pd.read_csv(xDir + 'xCREDIT.txt')
xCREDIT['DATE'] = pd.to_datetime(xCREDIT['DATE'], format='%m/%d/%Y')
xFTLS = pd.read_csv(xDir + 'xFTLS.txt')
xFTLS['DATE'] = pd.to_datetime(xFTLS['DATE'], format='%m/%d/%Y')
xHFRIEMNI = pd.read_csv(xDir + 'xHFRIEMNI.txt')
xHFRIEMNI['DATE'] = pd.to_datetime(xHFRIEMNI['DATE'], format='%m/%d/%Y')
xPRBAX = pd.read_csv(xDir + 'xPRBAX.txt')
xPRBAX['DATE'] = pd.to_datetime(xPRBAX['DATE'], format='%m/%d/%Y')
xPRWAX = pd.read_csv(xDir + 'xPRWAX.txt')
xPRWAX['DATE'] = pd.to_datetime(xPRWAX['DATE'], format='%m/%d/%Y')
xSPLPEQTY = pd.read_csv(xDir + 'xSPLPEQTY.txt')
xSPLPEQTY['DATE'] = pd.to_datetime(xSPLPEQTY['DATE'], format='%m/%d/%Y')
xSPX = pd.read_csv(xDir + 'xSPX.txt')
xSPX['DATE'] = pd.to_datetime(xSPX['DATE'], format='%m/%d/%Y')
xSPY = pd.read_csv(xDir + 'xSPY.txt')
xSPY['DATE'] = pd.to_datetime(xSPY['DATE'], format='%m/%d/%Y')
xTSLA = pd.read_csv(xDir + 'xTSLA.txt')
xTSLA['DATE'] = pd.to_datetime(xTSLA['DATE'], format='%m/%d/%Y')
xUS3M = pd.read_csv(xDir + 'xUS3M.txt')
xUS3M['DATE'] = pd.to_datetime(xUS3M['DATE'], format='%m/%d/%Y')
xUS10Y = pd.read_csv(xDir + 'xUS10Y.txt')
xUS10Y['DATE'] = pd.to_datetime(xUS10Y['DATE'], format='%m/%d/%Y')
xHYG = pd.read_csv(xDir + 'xHYG.txt')
xHYG['DATE'] = pd.to_datetime(xHYG['DATE'], format='%m/%d/%Y')
xCPI = pd.read_csv(xDir + 'xCPI.txt')
xCPI['DATE'] = pd.to_datetime(xCPI['DATE'], format='%m/%d/%Y')
xHYTR = pd.read_csv(xDir + 'xLF98TRUU.txt')
xHYTR['DATE'] = pd.to_datetime(xHYTR['DATE'], format='%m/%d/%Y')
xTIPS = pd.read_csv(xDir + 'xLBUTTRUU.txt')
xTIPS['DATE'] = pd.to_datetime(xTIPS['DATE'], format='%m/%d/%Y')
xGMWAX = pd.read_csv(xDir + 'xGMWAX.txt')
xGMWAX['DATE'] = pd.to_datetime(xGMWAX['DATE'], format='%m/%d/%Y')
xCashConst = pd.read_csv(xDir + 'xCashConst.txt')
xCashConst['DATE'] = pd.to_datetime(xCashConst['DATE'], format='%m/%d/%Y')
xS5INFT = pd.read_csv(xDir + 'xS5INFT.txt')
xS5INFT['DATE'] = pd.to_datetime(xS5INFT['DATE'], format='%m/%d/%Y')
x7030TR = pd.read_csv(xDir + 'x7030TR.txt')
x7030TR['DATE'] = pd.to_datetime(x7030TR['DATE'], format='%m/%d/%Y')
xUSCredit = pd.read_csv(xDir + 'xLUCRTRUU.txt')
xUSCredit['DATE'] = pd.to_datetime(xUSCredit['DATE'], format='%m/%d/%Y')
xSHY = pd.read_csv(xDir + 'xSHY.txt')
xSHY['DATE'] = pd.to_datetime(xSHY['DATE'], format='%m/%d/%Y')
xTIP = pd.read_csv(xDir + 'xTIP.txt')
xTIP['DATE'] = pd.to_datetime(xTIP['DATE'], format='%m/%d/%Y')
xAMZN = pd.read_csv(xDir + 'xAMZN.txt')
xAMZN['DATE'] = pd.to_datetime(xAMZN['DATE'], format='%m/%d/%Y')
xFB = pd.read_csv(xDir + 'xFB.txt')
xFB['DATE'] = pd.to_datetime(xFB['DATE'], format='%m/%d/%Y')
xVIAC = pd.read_csv(xDir + 'xVIAC.txt')
xVIAC['DATE'] = pd.to_datetime(xVIAC['DATE'], format='%m/%d/%Y')
xGOOG = pd.read_csv(xDir + 'xGOOG.txt')
xGOOG['DATE'] = pd.to_datetime(xGOOG['DATE'], format='%m/%d/%Y')
xLQD = pd.read_csv(xDir + 'xLQD.txt')
xLQD['DATE'] = pd.to_datetime(xLQD['DATE'], format='%m/%d/%Y')
xMDY = pd.read_csv(xDir + 'xMDY.txt')
xMDY['DATE'] = pd.to_datetime(xMDY['DATE'], format='%m/%d/%Y')
xMSFT = pd.read_csv(xDir + 'xMSFT.txt')
xMSFT['DATE'] = pd.to_datetime(xMSFT['DATE'], format='%m/%d/%Y')
xRLV = pd.read_csv(xDir + 'xRLV.txt')
xRLV['DATE'] = pd.to_datetime(xRLV['DATE'], format='%m/%d/%Y')
xRLG = pd.read_csv(xDir + 'xRLG.txt')
xRLG['DATE'] = pd.to_datetime(xRLG['DATE'], format='%m/%d/%Y')
xRIY = pd.read_csv(xDir + 'xRIY.txt')
xRIY['DATE'] = pd.to_datetime(xRIY['DATE'], format='%m/%d/%Y')
xRMV = pd.read_csv(xDir + 'xRMV.txt')
xRMV['DATE'] = pd.to_datetime(xRMV['DATE'], format='%m/%d/%Y')
xRMC = pd.read_csv(xDir + 'xRMC.txt')
xRMC['DATE'] = pd.to_datetime(xRMC['DATE'], format='%m/%d/%Y')
xRDG = pd.read_csv(xDir + 'xRDG.txt')
xRDG['DATE'] = pd.to_datetime(xRDG['DATE'], format='%m/%d/%Y')
xRUJ = pd.read_csv(xDir + 'xRUJ.txt')
xRUJ['DATE'] = pd.to_datetime(xRUJ['DATE'], format='%m/%d/%Y')
xRTY = pd.read_csv(xDir + 'xRTY.txt')
xRTY['DATE'] = pd.to_datetime(xRTY['DATE'], format='%m/%d/%Y')
xRUO = pd.read_csv(xDir + 'xRUO.txt')
xRUO['DATE'] = pd.to_datetime(xRUO['DATE'], format='%m/%d/%Y')

##########################################
xDF = xSPX.copy()
xDF = pd.merge(xDF, xSPXT, on=['DATE'], how='left')
xDF = pd.merge(xDF, xBondTR, on=['DATE'], how='left')
xDF = pd.merge(xDF, xAAPL, on=['DATE'], how='left')
xDF = pd.merge(xDF, xAGG, on=['DATE'], how='left')
xDF = pd.merge(xDF, xCCY, on=['DATE'], how='left')
xDF = pd.merge(xDF, xCOMM, on=['DATE'], how='left')
xDF = pd.merge(xDF, xCREDIT, on=['DATE'], how='left')
xDF = pd.merge(xDF, xFTLS, on=['DATE'], how='left')
###xDF = pd.merge(xDF, xHFRIEMNI, on=['DATE'], how='left')
xDF = pd.merge(xDF, xPRBAX, on=['DATE'], how='left')
xDF = pd.merge(xDF, xPRWAX, on=['DATE'], how='left')
xDF = pd.merge(xDF, xSPLPEQTY, on=['DATE'], how='left')
xDF = pd.merge(xDF, xSPY, on=['DATE'], how='left')
xDF = pd.merge(xDF, xTSLA, on=['DATE'], how='left')
xDF = pd.merge(xDF, xUS3M, on=['DATE'], how='left')
xDF = pd.merge(xDF, xUS10Y, on=['DATE'], how='left')
xDF = pd.merge(xDF, xHYG, on=['DATE'], how='left')
xDF = pd.merge(xDF, xHYTR, on=['DATE'], how='left')
xDF = pd.merge(xDF, xTIPS, on=['DATE'], how='left')
xDF = pd.merge(xDF, xGMWAX, on=['DATE'], how='left')
xDF = pd.merge(xDF, xCashConst, on=['DATE'], how='left')
xDF = pd.merge(xDF, xS5INFT, on=['DATE'], how='left')
xDF = pd.merge(xDF, x7030TR, on=['DATE'], how='left')
xDF = pd.merge(xDF, xUSCredit, on=['DATE'], how='left')
xDF = pd.merge(xDF, xSHY, on=['DATE'], how='left')
xDF = pd.merge(xDF, xTIP, on=['DATE'], how='left')
xDF = pd.merge(xDF, xAMZN, on=['DATE'], how='left')
xDF = pd.merge(xDF, xFB, on=['DATE'], how='left')
xDF = pd.merge(xDF, xVIAC, on=['DATE'], how='left')
xDF = pd.merge(xDF, xGOOG, on=['DATE'], how='left')
xDF = pd.merge(xDF, xLQD, on=['DATE'], how='left')
xDF = pd.merge(xDF, xMDY, on=['DATE'], how='left')
xDF = pd.merge(xDF, xMSFT, on=['DATE'], how='left')
xDF = pd.merge(xDF, xRLV, on=['DATE'], how='left')
xDF = pd.merge(xDF, xRLG, on=['DATE'], how='left')
xDF = pd.merge(xDF, xRIY, on=['DATE'], how='left')
xDF = pd.merge(xDF, xRMV, on=['DATE'], how='left')
xDF = pd.merge(xDF, xRMC, on=['DATE'], how='left')
xDF = pd.merge(xDF, xRDG, on=['DATE'], how='left')
xDF = pd.merge(xDF, xRUJ, on=['DATE'], how='left')
xDF = pd.merge(xDF, xRTY, on=['DATE'], how='left')
xDF = pd.merge(xDF, xRUO, on=['DATE'], how='left')

#####################################################################
# xEndDate_0 = pd.to_datetime('10/1/2018')
# xDF = xDF.loc[xDF['DATE']<xEndDate_0]
# ################ forward fill the missing equity trading dates ############
xDF['BondTR'].fillna(method='ffill', inplace=True)
xDF['HYTR'].fillna(method='ffill', inplace=True)
xDF['TIPS'].fillna(method='ffill', inplace=True)
xDF['LQD'].fillna(method='ffill', inplace=True)
xDF['SPLPEQTY'].fillna(method='ffill', inplace=True)
#################################
################Calculating SI returns here ##################################
for k in range(1,4):
    if k==1:
        # 2 year, buffer -10%, x1.5, cap = 21%, hard buffer note!
        xCap = 0.21 #0.21 #0.21  #1000 #0.21   #1000  #0.21
        xBuffer = -0.10000  ####-0.10  #-0.25   #-0.30   #-0.25
        xTerm = 2  #2  #4  #6   #4 #2  #3 # years
        xAmount = 100
        xLever = 1.500  #1.5  #1.15
        xBufferType = "H"  #"T"  # "H" for regular Buffer; "G" for Geared Buffer (or Barrier); "T" for Trigger Buffer!
    elif k == 2:
        # 4 years, buffer -25%, no leverage and no cap, barrier buffer note!
        xCap = 10000
        xBuffer = -0.250000
        xTerm = 4
        xAmount = 100
        xLever = 1.00
        xBufferType = "T"
    elif k==3:
        # 6 years, buffer -30%, x1.15 leverage and no cap, barrier buffer note!
        xCap = 10000  # 0.21 #0.21  #1000 #0.21   #1000  #0.21
        xBuffer = -0.300000  ####-0.10  #-0.25   #-0.30   #-0.25
        xTerm = 6
        xAmount = 100
        xLever = 1.1500  # 1.5  #1.15
        xBufferType = "T"  # "T"  # "H" for regular Buffer; "G" for Geared Buffer (or Barrier); "T" for Trigger Buffer!

    xDF['SPX_rtn_term'] = xDF['SPX'].pct_change(xTerm*252)
    xDF.loc[xDF['SPX_rtn_term'] > 0, 'SI' + (str)(xTerm) + '_rtn_term'] = xDF['SPX_rtn_term'] * xLever
    xDF.loc[xDF['SPX_rtn_term']* xLever > xCap, 'SI' + (str)(xTerm) + '_rtn_term'] = xCap
    xDF.loc[(xDF['SPX_rtn_term']<=0) & (xDF['SPX_rtn_term']>=xBuffer), 'SI'+(str)(xTerm)+'_rtn_term'] = 0
    if (xBufferType=='H'):
        xDF.loc[(xDF['SPX_rtn_term']<xBuffer),'SI'+(str)(xTerm)+'_rtn_term'] = xDF['SPX_rtn_term'] - xBuffer
    elif (xBufferType=='T'):
        xDF.loc[(xDF['SPX_rtn_term']<xBuffer),'SI'+(str)(xTerm)+'_rtn_term'] = xDF['SPX_rtn_term']
    elif (xBufferType=='G'):
        xK = 1 / (1+xBuffer)
        xDF.loc[(xDF['SPX_rtn_term']<xBuffer),'SI'+(str)(xTerm)+'_rtn_term'] = xK * (xDF['SPX_rtn_term'] - xBuffer)

    xDF['SI'+(str)(xTerm)+'_pct_ch_Y'] = (1+xDF['SI'+(str)(xTerm)+'_rtn_term'])**(1/xTerm) - 1
    xDF['SI'+(str)(xTerm)+'_pct_ch_Q'] = (1+xDF['SI'+(str)(xTerm)+'_rtn_term'])**(1/(xTerm*4)) - 1
    xDF['SI'+(str)(xTerm)+'_pct_ch_M'] = (1+xDF['SI'+(str)(xTerm)+'_rtn_term'])**(1/(xTerm*12)) - 1
    xDF['SI'+(str)(xTerm)+'_pct_ch_D'] = (1+xDF['SI'+(str)(xTerm)+'_rtn_term'])**(1/(xTerm*252)) - 1

###########################
#########################################
xSPX_2 = xSPX.copy()
xSPX_2['month']=xSPX_2.DATE.dt.month
xSPX_2['year']=xSPX_2.DATE.dt.year
xSPX_2['diff']=xSPX_2.month.diff(-1)
xSPX_2['month-year']=xSPX_2.month.astype('string')+'-'+xSPX_2.year.astype('string')
xSPX_2 = xSPX_2.loc[xSPX_2['diff']!=0]
##### equity market neutral index (monthly) ######
xHFRIEMNI['month']=xHFRIEMNI.DATE.dt.month
xHFRIEMNI['year']=xHFRIEMNI.DATE.dt.year
###xHFRIEMNI['diff']=xHFRIEMNI.month.diff(-1)
xHFRIEMNI['month-year']=xHFRIEMNI.month.astype('string')+'-'+xHFRIEMNI.year.astype('string')
xHFRIEMNI.rename(columns={'DATE': 'DATE0'},inplace=True)
#xHFRIEMNI['LS_1y_pct_ch']=xHFRIEMNI['HFRIEMNI'].pct_change(12)
xHFRIEMNI = pd.merge(xHFRIEMNI, xSPX_2[['DATE','month-year']], on=['month-year'],how='left')
xDF = pd.merge(xDF, xHFRIEMNI[['DATE','HFRIEMNI']], on=['DATE'], how='left')
##### CPI index (monthly) ######
xCPI['month']=xCPI.DATE.dt.month
xCPI['year']=xCPI.DATE.dt.year
xCPI['month-year']=xCPI.month.astype('string')+'-'+xCPI.year.astype('string')
xCPI.rename(columns={'DATE': 'DATE0'},inplace=True)
#xCPI['LS_1y_pct_ch']=xCPI['HFRIEMNI'].pct_change(12)
xCPI = pd.merge(xCPI, xSPX_2[['DATE','month-year']], on=['month-year'],how='left')
xDF = pd.merge(xDF, xCPI[['DATE','CPI']], on=['DATE'], how='left')
###########
xDF = pd.merge(xDF, xSPX_2[['DATE','month-year','diff']], on=['DATE'], how='left')
xDF_M = xDF.loc[xDF['diff']!=0]
xDF_M = xDF_M.loc[xDF_M['diff'].notnull()]
xDF_M.reset_index(drop=True, inplace=True)
xDF_M['RealBondTR'] = xDF_M['BondTR']/xDF_M['CPI']
xDF_M['quarter'] = xDF_M['DATE'].dt.quarter
xDF_M['diff_Q']=xDF_M.quarter.diff(-1)
######################################################

#########################################
xDF['SPXT_pct_ch_D']=xDF['SPXT'].pct_change()
xDF['BondTR_pct_ch_D']=xDF['BondTR'].pct_change()
xDF['AAPL_pct_ch_D']=xDF['AAPL'].pct_change()
xDF['AGG_pct_ch_D']=xDF['AGG'].pct_change()
xDF['CCY_pct_ch_D']=xDF['CCY'].pct_change()
xDF['COMM_pct_ch_D']=xDF['COMM'].pct_change()
xDF['CREDIT_pct_ch_D']=xDF['CREDIT'].pct_change()
xDF['FTLS_pct_ch_D']=xDF['FTLS'].pct_change()
xDF['HFRIEMNI_pct_ch_D']=xDF['HFRIEMNI'].pct_change()
xDF['PRBAX_pct_ch_D']=xDF['PRBAX'].pct_change()
xDF['PRWAX_pct_ch_D']=xDF['PRWAX'].pct_change()
xDF['SPLPEQTY_pct_ch_D']=xDF['SPLPEQTY'].pct_change()
xDF['SPX_pct_ch_D']=xDF['SPX'].pct_change()
xDF['SPY_pct_ch_D']=xDF['SPY'].pct_change()
xDF['TSLA_pct_ch_D']=xDF['TSLA'].pct_change()
xDF['US3M_pct_ch_D']=xDF['US3M'].pct_change()
xDF['US10Y_pct_ch_D']=xDF['US10Y'].pct_change()
xDF['HYG_pct_ch_D']=xDF['HYG'].pct_change()
xDF['HYTR_pct_ch_D']=xDF['HYTR'].pct_change()
xDF['TIPS_pct_ch_D']=xDF['TIPS'].pct_change()
xDF['GMWAX_pct_ch_D']=xDF['GMWAX'].pct_change()
xDF['CashConst_pct_ch_D']=xDF['CashConst'].pct_change()
xDF['S5INFT_pct_ch_D']=xDF['S5INFT'].pct_change()
xDF['7030TR_pct_ch_D']=xDF['7030TR'].pct_change()
xDF['USCredit_pct_ch_D']=xDF['USCredit'].pct_change()
xDF['SHY_pct_ch_D']=xDF['SHY'].pct_change()
xDF['TIP_pct_ch_D']=xDF['TIP'].pct_change()
xDF['AMZN_pct_ch_D']=xDF['AMZN'].pct_change()
xDF['FB_pct_ch_D']=xDF['FB'].pct_change()
xDF['VIAC_pct_ch_D']=xDF['VIAC'].pct_change()
xDF['GOOG_pct_ch_D']=xDF['GOOG'].pct_change()
xDF['LQD_pct_ch_D']=xDF['LQD'].pct_change()
xDF['MDY_pct_ch_D']=xDF['MDY'].pct_change()
xDF['MSFT_pct_ch_D']=xDF['MSFT'].pct_change()
xDF['RLV_pct_ch_D']=xDF['RLV'].pct_change()
xDF['RLG_pct_ch_D']=xDF['RLG'].pct_change()
xDF['RIY_pct_ch_D']=xDF['RIY'].pct_change()
xDF['RMV_pct_ch_D']=xDF['RMV'].pct_change()
xDF['RMC_pct_ch_D']=xDF['RMC'].pct_change()
xDF['RDG_pct_ch_D']=xDF['RDG'].pct_change()
xDF['RUJ_pct_ch_D']=xDF['RUJ'].pct_change()
xDF['RTY_pct_ch_D']=xDF['RTY'].pct_change()
xDF['RUO_pct_ch_D']=xDF['RUO'].pct_change()

############### new portfolio #########
################
xY_col = 'SPLPEQTY'
xY_col = 'FTLS'
xY_col = 'CashConst'
xY_col = 'PRWAX'
xY_col = 'GMWAX'
xY_col = 'PRBAX'
xY_col = 'SI'
xY_col = '7030TR'

xY_col = 'SPY'
xY_col = 'SHY'
xY_col = 'TIP'
xY_col = 'AGG'
xY_col = 'HYG'
xY_col = 'TSLA'
xY_col = 'AAPL'

xCoef_table = pd.DataFrame()
xRiskExp_Current = pd.DataFrame()
xRiskConcentration_Current = pd.DataFrame()
##################
xW1=0.75
xW2=0.25
xW3=0.0  #0.10
#xW4=0.15
#xDF['NewPort_pct_ch_D'] =xW1* xDF[xY_col + '_pct_ch_D'] + xW2*xDF['BondTR_pct_ch_D']
#xDF['NewPort_pct_ch_D'] =xW1* xDF[xY_col + '_pct_ch_D'] + xW2*xDF['TIPS_pct_ch_D']
#xDF['NewPort_pct_ch_D'] =xW1* xDF[xY_col + '_pct_ch_D'] + xW2*xDF['BondTR_pct_ch_D']+ xW3*xDF['SI2_pct_ch_D']
xDF['NewPort_pct_ch_D'] =xW1* xDF[xY_col + '_pct_ch_D'] + xW2*xDF['BondTR_pct_ch_D']+ xW3*xDF['SI2_pct_ch_D']
#xDF['NewPort_pct_ch_D'] =xW1* xDF[xY_col + '_pct_ch_D'] + xW2*xDF['SPXT_pct_ch_D']+ xW3*xDF['SI2_pct_ch_D']
#xDF['NewPort_pct_ch_D'] =xW1* xDF[xY_col + '_pct_ch_D'] + xW2*xDF['SI2_pct_ch_D']+ xW3*xDF['TIPS_pct_ch_D']+ xW4*xDF['HYTR_pct_ch_D']

xDF['NewPort'] = (1+xDF['NewPort_pct_ch_D']).cumprod()

############### Yearly ########################
xDF['SPXT_pct_ch_Y']=xDF['SPXT'].pct_change(252)
xDF['BondTR_pct_ch_Y']=xDF['BondTR'].pct_change(252)
xDF['AAPL_pct_ch_Y']=xDF['AAPL'].pct_change(252)
xDF['AGG_pct_ch_Y']=xDF['AGG'].pct_change(252)
xDF['CCY_pct_ch_Y']=xDF['CCY'].pct_change(252)
xDF['COMM_pct_ch_Y']=xDF['COMM'].pct_change(252)
xDF['CREDIT_pct_ch_Y']=xDF['CREDIT'].pct_change(252)
xDF['FTLS_pct_ch_Y']=xDF['FTLS'].pct_change(252)
xDF['HFRIEMNI_pct_ch_Y']=xDF['HFRIEMNI'].pct_change(252)   #need to calculate YoY from Monthly data pct_change(12)!!!
xDF['PRBAX_pct_ch_Y']=xDF['PRBAX'].pct_change(252)
xDF['PRWAX_pct_ch_Y']=xDF['PRWAX'].pct_change(252)
xDF['SPLPEQTY_pct_ch_Y']=xDF['SPLPEQTY'].pct_change(252)
xDF['SPX_pct_ch_Y']=xDF['SPX'].pct_change(252)
xDF['SPY_pct_ch_Y']=xDF['SPY'].pct_change(252)
xDF['TSLA_pct_ch_Y']=xDF['TSLA'].pct_change(252)
xDF['US3M_pct_ch_Y']=xDF['US3M'].pct_change(252)
xDF['US10Y_pct_ch_Y']=xDF['US10Y'].pct_change(252)
xDF['HYG_pct_ch_Y']=xDF['HYG'].pct_change(252)
xDF['HYTR_pct_ch_Y']=xDF['HYTR'].pct_change(252)
xDF['TIPS_pct_ch_Y']=xDF['TIPS'].pct_change(252)
xDF['GMWAX_pct_ch_Y']=xDF['GMWAX'].pct_change(252)
xDF['CashConst_pct_ch_Y']=xDF['CashConst'].pct_change(252)
xDF['S5INFT_pct_ch_Y']=xDF['S5INFT'].pct_change(252)
xDF['7030TR_pct_ch_Y']=xDF['7030TR'].pct_change(252)
xDF['USCredit_pct_ch_Y']=xDF['USCredit'].pct_change(252)
xDF['SHY_pct_ch_Y']=xDF['SHY'].pct_change(252)
xDF['TIP_pct_ch_Y']=xDF['TIP'].pct_change(252)
xDF['AMZN_pct_ch_Y']=xDF['AMZN'].pct_change(252)
xDF['FB_pct_ch_Y']=xDF['FB'].pct_change(252)
xDF['VIAC_pct_ch_Y']=xDF['VIAC'].pct_change(252)
xDF['GOOG_pct_ch_Y']=xDF['GOOG'].pct_change(252)
xDF['LQD_pct_ch_Y']=xDF['LQD'].pct_change(252)
xDF['MDY_pct_ch_Y']=xDF['MDY'].pct_change(252)
xDF['MSFT_pct_ch_Y']=xDF['MSFT'].pct_change(252)
xDF['RLV_pct_ch_Y']=xDF['RLV'].pct_change(252)
xDF['RLG_pct_ch_Y']=xDF['RLG'].pct_change(252)
xDF['RIY_pct_ch_Y']=xDF['RIY'].pct_change(252)
xDF['RMV_pct_ch_Y']=xDF['RMV'].pct_change(252)
xDF['RMC_pct_ch_Y']=xDF['RMC'].pct_change(252)
xDF['RDG_pct_ch_Y']=xDF['RDG'].pct_change(252)
xDF['RUJ_pct_ch_Y']=xDF['RUJ'].pct_change(252)
xDF['RTY_pct_ch_Y']=xDF['RTY'].pct_change(252)
xDF['RUO_pct_ch_Y']=xDF['RUO'].pct_change(252)
############### overwrite to create the EXACT 70/30 returns #############
xDF['7030TR_pct_ch_Y']=0.7*xDF['SPXT_pct_ch_Y']+0.3*xDF['BondTR_pct_ch_Y']
xDF['3070TR_pct_ch_Y']=0.3*xDF['SPXT_pct_ch_Y']+0.7*xDF['BondTR_pct_ch_Y']
xDF['30AAPL30MSFT20AMZN20GOOGTR_pct_ch_Y'] = 0.3*xDF['AAPL_pct_ch_Y'] + 0.3*xDF['MSFT_pct_ch_Y'] +0.2*xDF['AMZN_pct_ch_Y'] +0.2*xDF['GOOG_pct_ch_Y']
xDF['30SPY30MDY20AGG20LQDTR_pct_ch_Y'] = 0.3*xDF['SPY_pct_ch_Y'] + 0.3*xDF['MDY_pct_ch_Y'] +0.2*xDF['AGG_pct_ch_Y'] +0.2*xDF['LQD_pct_ch_Y']
#xDF['85AAPL15SHY_pct_ch_Y'] = 0.70*xDF['AAPL_pct_ch_Y']+0.15*xDF['SHY_pct_ch_Y']+0.15*xDF['SI4_pct_ch_Y']
#########################################################################
xDF['NewPort_pct_ch_Y']=xDF['NewPort'].pct_change(252)

xDF['Inflation_pct_ch_Y'] = xDF['BondTR_pct_ch_Y'] - xDF['TIPS_pct_ch_Y']
xDF['RealBondTR_pct_ch_Y'] = xDF['BondTR_pct_ch_Y'] - xDF['TIPS_pct_ch_Y']

# xDF['NewPort_pct_ch_Y']=xW1*xDF['SPY_pct_ch_Y'] + xW2*xDF['SI2_pct_ch_Y']
xDF['NewPort_pct_ch_Y']=xW1*xDF['3070TR_pct_ch_Y'] + xW2*xDF['SI2_pct_ch_Y']
#xDF['NewPort_pct_ch_Y']=xW1*xDF['SPY_pct_ch_Y'] + xW2*xDF['BondTR_pct_ch_Y']+ xW3*xDF['SI2_pct_ch_Y']  # case #1
#xDF['NewPort_pct_ch_Y']=xW1*xDF[xY_col+'_pct_ch_Y'] + xW2*xDF['BondTR_pct_ch_Y']+ xW3*xDF['SI2_pct_ch_Y']  # case #1
#xDF['NewPort_pct_ch_Y']=xW1*xDF['AGG_pct_ch_Y'] + xW2*xDF['SPXT_pct_ch_Y']+ xW3*xDF['SI2_pct_ch_Y']  # case #2
#xDF['NewPort_pct_ch_Y']=xW1*xDF['HYG_pct_ch_Y'] + xW2*xDF['SPXT_pct_ch_Y']+ xW3*xDF['SI2_pct_ch_Y']  # case #3
#xDF['NewPort_pct_ch_Y']=xW1*xDF[xY_col+'_pct_ch_Y'] + xW2*xDF['SPXT_pct_ch_Y']+ xW3*xDF['SI2_pct_ch_Y']+ xW4*xDF['BondTR_pct_ch_Y']  # case #3

# xDF['NewPort_pct_ch_Y']=xW1*xDF[xY_col+'_pct_ch_Y'] + xW2*xDF['SHY_pct_ch_Y']+ xW3*xDF['SI4_pct_ch_Y']  # case #1
# xDF['NewPort_pct_ch_Y']=xW1*xDF[xY_col+'_pct_ch_Y'] + xW2*xDF['SHY_pct_ch_Y'] #+ xW3*xDF['SI4_pct_ch_Y']  # case #1
# xDF['NewPort_pct_ch_Y']=xW1*xDF[xY_col+'_pct_ch_Y'] + xW2*xDF['AGG_pct_ch_Y'] #+ xW3*xDF['SI4_pct_ch_Y']  # case #1
#xDF['NewPort_pct_ch_Y']=xW1*xDF[xY_col+'_pct_ch_Y'] + xW2*xDF['SPY_pct_ch_Y'] + xW3*xDF['SI6_pct_ch_Y']  # case #1

#xDF['NewPort_pct_ch_Y']=xW1*xDF['PRWAX_pct_ch_Y'] + xW2*xDF['BondTR_pct_ch_Y']+ xW3*xDF['SI2_pct_ch_Y']

############################
xDF_M = pd.merge(xDF_M,xDF[['DATE','NewPort']],on=['DATE'],how='left')
######################
xCols_pct = xDF.columns[xDF.columns.str.contains(pat = '_pct_ch')]

xDF2=xDF[xCols_pct].copy()

xCorrelations = xDF2.corr()
xStdDev=xDF2.std()
xMean = xDF2.mean()
xCorrelations.to_csv(xDir+'xCorrelations.txt')
xStdDev.to_csv(xDir+'xStdDev.txt')
xMean.to_csv(xDir+'xMean.txt')
########### model portfolios #########
CONS_E=0.2
MODCONS_E=0.4
MOD_E=0.6
MODGROW_E=0.75
GROW_E=0.9
MAXGROW_E=0.98

#xMP=xDF[['DATE','SPXT','SPXT_pct_ch_D','SPXT_pct_ch_Y','BondTR','BondTR_pct_ch_D','BondTR_pct_ch_Y']].copy()
xMP=xDF[['DATE','SPXT_pct_ch_D','BondTR_pct_ch_D',xY_col+'_pct_ch_D','NewPort_pct_ch_D','NewPort_pct_ch_Y']].copy()
xMP.rename(columns={xY_col+'_pct_ch_D':'Current_pct_ch_D','NewPort_pct_ch_D':'New_pct_ch_D'},inplace=True)
xMP['CONS_pct_ch_D']=CONS_E*xMP['SPXT_pct_ch_D']+(1-CONS_E)*xMP['BondTR_pct_ch_D']     #daily rebalanced as benchmark index
xMP['MODCONS_pct_ch_D']=MODCONS_E*xMP['SPXT_pct_ch_D']+(1-MODCONS_E)*xMP['BondTR_pct_ch_D']     #daily rebalanced as benchmark index
xMP['MOD_pct_ch_D']=MOD_E*xMP['SPXT_pct_ch_D']+(1-MOD_E)*xMP['BondTR_pct_ch_D']     #daily rebalanced as benchmark index
xMP['MODGROW_pct_ch_D']=MODGROW_E*xMP['SPXT_pct_ch_D']+(1-MODGROW_E)*xMP['BondTR_pct_ch_D']     #daily rebalanced as benchmark index
xMP['GROW_pct_ch_D']=GROW_E*xMP['SPXT_pct_ch_D']+(1-GROW_E)*xMP['BondTR_pct_ch_D']     #daily rebalanced as benchmark index
xMP['MAXGROW_pct_ch_D']=MAXGROW_E*xMP['SPXT_pct_ch_D']+(1-MAXGROW_E)*xMP['BondTR_pct_ch_D']     #daily rebalanced as benchmark index

xMP['CONS_port']=(1 + xMP['CONS_pct_ch_D']).cumprod()
xMP['MODCONS_port']=(1 + xMP['MODCONS_pct_ch_D']).cumprod()
xMP['MOD_port']=(1 + xMP['MOD_pct_ch_D']).cumprod()
xMP['MODGROW_port']=(1 + xMP['MODGROW_pct_ch_D']).cumprod()
xMP['GROW_port']=(1 + xMP['GROW_pct_ch_D']).cumprod()
xMP['MAXGROW_port']=(1 + xMP['MAXGROW_pct_ch_D']).cumprod()
xMP['Current_port']=(1 + xMP['Current_pct_ch_D']).cumprod()
xMP['New_port']=(1 + xMP['New_pct_ch_D']).cumprod()

xMP['CONS_pct_ch_Y']=xMP['CONS_port'].pct_change(252)
xMP['MODCONS_pct_ch_Y']=xMP['MODCONS_port'].pct_change(252)
xMP['MOD_pct_ch_Y']=xMP['MOD_port'].pct_change(252)
xMP['MODGROW_pct_ch_Y']=xMP['MODGROW_port'].pct_change(252)
xMP['GROW_pct_ch_Y']=xMP['GROW_port'].pct_change(252)
xMP['MAXGROW_pct_ch_Y']=xMP['MAXGROW_port'].pct_change(252)
xMP['Current_pct_ch_Y']=xMP['Current_port'].pct_change(252)
xMP['New_pct_ch_Y']=xMP['New_port'].pct_change(252)

xMP['New_pct_ch_Y']=xMP['NewPort_pct_ch_Y']

############################
xMP_MQ = xDF_M[['DATE']].copy()
xMP_MQ = pd.merge(xMP_MQ, xMP[['DATE','CONS_port','MODCONS_port','MOD_port','MODGROW_port','GROW_port','MAXGROW_port',
                               'Current_port','New_port']],on=['DATE'],how='left')
xMP_MQ['CONS_pct_ch_M']=xMP_MQ['CONS_port'].pct_change()
xMP_MQ['MODCONS_pct_ch_M']=xMP_MQ['MODCONS_port'].pct_change()
xMP_MQ['MOD_pct_ch_M']=xMP_MQ['MOD_port'].pct_change()
xMP_MQ['MODGROW_pct_ch_M']=xMP_MQ['MODGROW_port'].pct_change()
xMP_MQ['GROW_pct_ch_M']=xMP_MQ['GROW_port'].pct_change()
xMP_MQ['MAXGROW_pct_ch_M']=xMP_MQ['MAXGROW_port'].pct_change()
xMP_MQ['Current_pct_ch_M']=xMP_MQ['Current_port'].pct_change()
xMP_MQ['New_pct_ch_M']=xMP_MQ['New_port'].pct_change()

#####xMP_MQ['Current_pct_ch_M']=xMP_MQ['Current_port'].pct_change()

xMP_MQ['CONS_pct_ch_Q']=xMP_MQ['CONS_port'].pct_change(3)
xMP_MQ['MODCONS_pct_ch_Q']=xMP_MQ['MODCONS_port'].pct_change(3)
xMP_MQ['MOD_pct_ch_Q']=xMP_MQ['MOD_port'].pct_change(3)
xMP_MQ['MODGROW_pct_ch_Q']=xMP_MQ['MODGROW_port'].pct_change(3)
xMP_MQ['GROW_pct_ch_Q']=xMP_MQ['GROW_port'].pct_change(3)
xMP_MQ['MAXGROW_pct_ch_Q']=xMP_MQ['MAXGROW_port'].pct_change(3)
xMP_MQ['Current_pct_ch_Q']=xMP_MQ['Current_port'].pct_change(3)
xMP_MQ['New_pct_ch_Q']=xMP_MQ['New_port'].pct_change(3)
############################
xCols_pct_MP = xMP.columns[xMP.columns.str.contains(pat = '_pct_ch_Y')]
xMP2=xMP[xCols_pct_MP].copy()
xAnnRtn_MP_Y=xMP2.mean()
xStdDev_MP_Y=xMP2.std()
xStdDev_MP_Y.to_csv(xDir+'xStdDev_MP_Y.txt')
xAnnRtn_MP_Y.to_csv(xDir+'xAnnRtn_MP_Y.txt')
#################
xCols_pct_MP = xMP.columns[xMP.columns.str.contains(pat = '_pct_ch_D')]
xMP2=xMP[xCols_pct_MP].copy()
xAnnRtn_MP_D=xMP2.mean() * 252 ####  try to annualized compounded annual return
xStdDev_MP_D=xMP2.std() * np.sqrt(252)
xStdDev_MP_D.to_csv(xDir+'xStdDev_MP_D.txt')
xAnnRtn_MP_D.to_csv(xDir+'xAnnRtn_MP_D.txt')

#xStdDev_MP[0] is the std dev of the conservative model portfolio
#xStdDev_MP[5] is the std dev of the MAX Growth model portfolio
# std dev > xStdDev_MP[5] is ACCESSIVE GROWTH portfolio!!!!

######## OLS HERE ANNUAL ###############
xCols_pct_ch_Y= xDF.columns[xDF.columns.str.contains(pat = '_pct_ch_Y')]
xCols_pct_ch_Y=xCols_pct_ch_Y.insert(0,'DATE')

xRiskFactorSet_Y=['SPXT_pct_ch_Y','BondTR_pct_ch_Y','CCY_pct_ch_Y','COMM_pct_ch_Y','USCredit_pct_ch_Y','HYTR_pct_ch_Y',
                  'TIPS_pct_ch_Y','Inflation_pct_ch_Y']   #'CPI_pct_ch_M','RealBondTR_pct_ch_Y'

xRiskFactorSet_Y=['SPXT_pct_ch_Y','USCredit_pct_ch_Y','TIPS_pct_ch_Y','COMM_pct_ch_Y']   #'CPI_pct_ch_M','RealBondTR_pct_ch_Y'
#xRiskFactorSet_Y=['SPXT_pct_ch_Y','USCredit_pct_ch_Y','TIPS_pct_ch_Y','COMM_pct_ch_Y','HYTR_pct_ch_Y']   #'CPI_pct_ch_M','RealBondTR_pct_ch_Y'

################## derive orthogonal risk factors ##################
xDF_orthog = xDF[['DATE']+xRiskFactorSet_Y]
xDF_orthog.dropna(inplace=True)
xDF_orthog.reset_index(drop=True,inplace=True)
## (1) derive orthog_SPXT #####
Y = xDF_orthog['SPXT_pct_ch_Y']
X = xDF_orthog['TIPS_pct_ch_Y']
X = sm.add_constant(X)
model = sm.OLS(Y, X)
result = model.fit()
xDF_orthog['orthog_SPXT_pct_ch_Y'] = result.params[0] + result.resid
print(xDF_orthog[['orthog_SPXT_pct_ch_Y', 'TIPS_pct_ch_Y']].corr())

## (2) derive orthog_USCredit #####
Y = xDF_orthog['USCredit_pct_ch_Y']
X = xDF_orthog[['SPXT_pct_ch_Y','TIPS_pct_ch_Y']]
#X = xDF_orthog['TIPS_pct_ch_Y']
X = sm.add_constant(X)
model = sm.OLS(Y, X)
result = model.fit()
xDF_orthog['orthog_USCredit_pct_ch_Y'] = result.params[0] + result.resid
print(xDF_orthog[['orthog_USCredit_pct_ch_Y','TIPS_pct_ch_Y']].corr())

## (3) derive orthog_COMM #####
Y = xDF_orthog['COMM_pct_ch_Y']
#X = xDF_orthog[['SPXT_pct_ch_Y','TIPS_pct_ch_Y']]
X = xDF_orthog[['SPXT_pct_ch_Y','TIPS_pct_ch_Y','USCredit_pct_ch_Y']]
X = sm.add_constant(X)
model = sm.OLS(Y, X)
result = model.fit()
xDF_orthog['orthog_COMM_pct_ch_Y'] = result.params[0] + result.resid
print(xDF_orthog[['orthog_COMM_pct_ch_Y','TIPS_pct_ch_Y']].corr())

xRiskFactorCorrelations_orthog = (xDF_orthog[['orthog_SPXT_pct_ch_Y','orthog_USCredit_pct_ch_Y','orthog_COMM_pct_ch_Y','TIPS_pct_ch_Y']].corr()).round(4)
xRiskFactorCorrelations_raw = (xDF_orthog[['SPXT_pct_ch_Y','USCredit_pct_ch_Y','COMM_pct_ch_Y','TIPS_pct_ch_Y']].corr()).round(4)

xDF = pd.merge(xDF,xDF_orthog[['DATE','orthog_SPXT_pct_ch_Y','orthog_USCredit_pct_ch_Y','orthog_COMM_pct_ch_Y']],on=['DATE'],how='left')
##################### bring in the rolling annual returns for Model Portfolios as a benchmarks for Risk Exposures ###########
xDF = pd.merge(xDF,xMP[['DATE','CONS_pct_ch_Y','MODCONS_pct_ch_Y','MOD_pct_ch_Y','MODGROW_pct_ch_Y','GROW_pct_ch_Y','MAXGROW_pct_ch_Y']],on=['DATE'],how='left')
##########################################################################################
xOrthogonal = 'orthog'
#xOrthogonal = ''

if xOrthogonal == 'orthog':
    xRiskFactorSet_Y = ['orthog_SPXT_pct_ch_Y','orthog_USCredit_pct_ch_Y','TIPS_pct_ch_Y','orthog_COMM_pct_ch_Y']
    #xRiskFactorSet_Y = ['orthog_SPXT_pct_ch_Y', 'TIPS_pct_ch_Y', 'orthog_COMM_pct_ch_Y']
else:
    xOrthogonal = ''
    xRiskFactorSet_Y = ['SPXT_pct_ch_Y', 'USCredit_pct_ch_Y', 'TIPS_pct_ch_Y',
                        'COMM_pct_ch_Y']  # 'CPI_pct_ch_M','RealBondTR_pct_ch_Y'
    #xRiskFactorSet_Y = ['SPXT_pct_ch_Y', 'TIPS_pct_ch_Y','RealBondTR_pct_ch_Y','COMM_pct_ch_Y']  # 'CPI_pct_ch_M','RealBondTR_pct_ch_Y'

#xRiskFactorSet_Y = ['orthog_SPXT_pct_ch_Y','orthog_USCredit_pct_ch_Y','TIPS_pct_ch_Y','orthog_COMM_pct_ch_Y','HYTR_pct_ch_Y']
############# in REAL terms #####################
xDF['RealSPXT_pct_ch_Y'] = xDF['SPXT_pct_ch_Y'] - xDF['TIPS_pct_ch_Y']
xDF['RealUSCredit_pct_ch_Y'] = xDF['USCredit_pct_ch_Y'] - xDF['TIPS_pct_ch_Y']
xDF['RealCOMM_pct_ch_Y'] = xDF['COMM_pct_ch_Y'] - xDF['TIPS_pct_ch_Y']
##xRiskFactorSet_Y=['RealSPXT_pct_ch_Y','RealUSCredit_pct_ch_Y','TIPS_pct_ch_Y','RealCOMM_pct_ch_Y']
##################################

xDescriptive_Y=xDF[[xY_col+'_pct_ch_Y']+xRiskFactorSet_Y].describe(include='all').to_string()
xCorrelations_Y=xDF[[xY_col+'_pct_ch_Y']+xRiskFactorSet_Y].corr().to_string()

xDescriptive_Y = xDescriptive_Y + '\n\n' + xCorrelations_Y
f = open(xDir + 'xDescriptive_Y_'+xY_col+'.txt','w')
f.write(xDescriptive_Y + '\r\n')
f.close()

xDep_var = ['SPY','AGG','HYG','SHY','MSFT','AMZN','FB','GOOG','VIAC',
            'LQD','30AAPL30MSFT20AMZN20GOOGTR','30SPY30MDY20AGG20LQDTR','TSLA',
            '7030TR','SI2','SI4','SI6','SPLPEQTY','CONS','MODCONS',
            'MOD','MODGROW','GROW','MAXGROW','CashConst','AAPL']
xDep_var = ['SPY','AGG','HYG','SHY','MSFT','AMZN','FB','GOOG','VIAC',
            'LQD','30AAPL30MSFT20AMZN20GOOGTR','30SPY30MDY20AGG20LQDTR','AAPL',
            '7030TR','3070TR','SI2','SI4','SI6','SPLPEQTY','CONS','MODCONS',
            'MOD','MODGROW','GROW','MAXGROW','CashConst','RLV','RIY','RMV',
            'RMC','RDG','RUJ','RTY','RUO','TSLA']  #### 'RLG',
#xDep_var = ['TSLA']  #### 'RLG',

### xDep_var = ['RTY','RUO','AAPL']

#xDep_var = ['RLV','RLG','RIY','RMV','RMC','RDG','RUJ','RTY','RUO','AAPL']

#xDep_Var = [xY_col]

xRiskFactorSet_Y = ['SPXT_pct_ch_Y','BondTR_pct_ch_Y']
#xRiskFactorSet_Y = ['RLG_pct_ch_Y']

xRisk_concentration_Current = pd.DataFrame()
xRisk_concentration_New = pd.DataFrame()
for xY_col in xDep_var:
    ####xDF_OLS_Y=xDF[xCols_pct_ch_Y].copy()
    xDF_OLS_Y = xDF[['DATE'] + xRiskFactorSet_Y + [xY_col+'_pct_ch_Y','NewPort_pct_ch_Y']].copy()  #'CPI_pct_ch_Y',

    xDF_OLS_Y.dropna(inplace=True)
    xDF_OLS_Y.reset_index(drop=True,inplace=True)
    ########### set up weightings for WLS here #####################
    xDF_OLS_Y['w'] = np.exp(-(-xDF_OLS_Y.index+xDF_OLS_Y.index.max()) / (len(xDF_OLS_Y) / 5))    # exponential
    #xDF_OLS_Y['w'] = (xDF_OLS_Y.index) / xDF_OLS_Y.index.max()  # linear - the latest has more weights!
    ###########################
    xStartDate_Y = xDF_OLS_Y['DATE'].min()
    xEndDate_Y = xDF_OLS_Y['DATE'].max()
    #################### model portfolios for Rooling annual rate ############
    xMP_Y = xDF_OLS_Y[['DATE']].copy()
    xMP_Y = pd.merge(xMP_Y, xMP[['DATE','CONS_pct_ch_Y','MODCONS_pct_ch_Y','MOD_pct_ch_Y','MODGROW_pct_ch_Y','GROW_pct_ch_Y',
                        'MAXGROW_pct_ch_Y','Current_pct_ch_Y','New_pct_ch_Y']], on=['DATE'], how='left')
    xMP_Y_AnnRtn = xMP_Y.mean().reset_index()
    xMP_Y_AnnRisk = xMP_Y.std().reset_index()
    xMP_Y_AnnRtn.rename(columns={0: 'AnnRtn'},inplace=True)
    xMP_Y_AnnRisk.rename(columns={0: 'AnnRisk'},inplace=True)

    xMP_Y_AnnRtnRisk = pd.merge(xMP_Y_AnnRtn,xMP_Y_AnnRisk,on=['index'],how='left')
    ################ OLS ################
    xInd_Vars = ['SPXT_pct_ch_Y','BondTR_pct_ch_Y','TIPS_pct_ch_Y','CCY_pct_ch_Y','COMM_pct_ch_Y','USCredit_pct_ch_Y','HYTR_pct_ch_Y']
    xInd_Vars = ['SPXT_pct_ch_Y','BondTR_pct_ch_Y','TIPS_pct_ch_Y','CCY_pct_ch_Y','USCredit_pct_ch_Y']
    xInd_Vars = ['SPXT_pct_ch_Y','BondTR_pct_ch_Y','TIPS_pct_ch_Y','CCY_pct_ch_Y','USCredit_pct_ch_Y','HYTR_pct_ch_Y']
    xInd_Vars = ['SPXT_pct_ch_Y','Inflation_pct_ch_Y','TIPS_pct_ch_Y','CCY_pct_ch_Y','USCredit_pct_ch_Y','HYTR_pct_ch_Y']
    xInd_Vars = ['SPXT_pct_ch_Y','Inflation_pct_ch_Y','TIPS_pct_ch_Y','CCY_pct_ch_Y','USCredit_pct_ch_Y']
    xInd_Vars = ['SPXT_pct_ch_Y']
    xInd_Vars = ['SPXT_pct_ch_Y','BondTR_pct_ch_Y']
    xInd_Vars = ['SPXT_pct_ch_Y','BondTR_pct_ch_Y','TIPS_pct_ch_Y','CCY_pct_ch_Y','COMM_pct_ch_Y','USCredit_pct_ch_Y','HYTR_pct_ch_Y']

    xInd_Vars = xRiskFactorSet_Y

    ###xInd_Vars = ['S5INFT_pct_ch_Y']
    #xInd_Vars = ['SPXT_pct_ch_Y','Inflation_pct_ch_Y','TIPS_pct_ch_Y','CCY_pct_ch_Y','USCredit_pct_ch_Y']
    X = xDF_OLS_Y[xInd_Vars]
    ############### risk factors annual returns and std dev ##########
    X_StdDev_Y = xDF_OLS_Y[xInd_Vars].std().reset_index()
    X_Rtn_Y = xDF_OLS_Y[xInd_Vars].mean().reset_index()
    ##################################################################
    xVersion=['Current','New']
    #xVersion=['Current']
    xRisk_exposures_Current=pd.DataFrame()
    xRisk_exposures_New=pd.DataFrame()
    for x in xVersion:
        if x=='Current':
            Y = xDF_OLS_Y[xY_col + '_pct_ch_Y']
            xY_col2 = xY_col
            xCorrelations_Y = xDF_OLS_Y[[xY_col + '_pct_ch_Y'] + xInd_Vars].corr().to_string()
        elif x=='New':
            Y = xDF_OLS_Y['NewPort_pct_ch_Y']
            xY_col2 = 'New'
            xCorrelations_Y = xDF_OLS_Y[[xY_col2 + 'Port_pct_ch_Y'] + xInd_Vars].corr().to_string()
        #xInd_Vars = ['SPXT_pct_ch_Y','RealBondTR_pct_ch_Y','TIPS_pct_ch_Y','CPI_pct_ch_Y','CCY_pct_ch_Y','COMM_pct_ch_Y','USCredit_pct_ch_Y','HYTR_pct_ch_Y']

        #xCorrelations_Y = xDF_OLS_Y[[xY_col + '_pct_ch_Y']+xInd_Vars].corr().to_string()
        f = open(xDir + 'xCorrelations_Y_' + xY_col + '_' + x + '.txt','w')
        f.write(xCorrelations_Y + '\r\n')
        f.close()

        X = sm.add_constant(X)
        xStart_time = datetime.datetime.now() #time.time_ns()*1000000
        xRegressionType ='WLS'    #'OLS' #'WLS'
        if xRegressionType == 'OLS':
            model = sm.OLS(Y,X)
        elif xRegressionType == 'WLS':
            model = sm.WLS(Y, X, weights=xDF_OLS_Y['w'])
        result = model.fit()
        # for i in range(1,9999):
        #     print(i)
        xEnd_time = datetime.datetime.now() #time.time_ns()*1000000
        globals()['xSecond_Y_'+x] = 'Start: '+(str)(xStart_time) +'; End: '+(str)(xEnd_time) + '; Duration: ' +(str)((xEnd_time - xStart_time))
        xOLS_Summary_Y = result.summary()
        xOLS_text = xOLS_Summary_Y.as_text()

        f = open(xDir + 'xOLS_Y_' + xY_col +  '_' + x + '.txt','w')
        f.write(globals()['xSecond_Y_'+x] + '\n\n' + xOLS_text + '\r\n')
        f.close()

        # ########## calc annualized return YEARLY ##########
        xAnnRtn_Y_Y = Y.mean()
        xAnnRisk_Y_Y = np.sqrt(Y.var())
        # xMP_Y_AnnRtnRisk=xMP_Y_AnnRtnRisk.append({'index':'Current Portfolio','AnnRtn':xAnnRtn_Y_Y,'AnnRisk':xAnnRisk_Y_Y}, ignore_index=True)
        # ############################################

        xVar_X = np.array(X.var())
        xVar_Y = Y.var()
        xCoef_sq = result.params**2
        xVar_resid = result.resid.var()
        xVar_CoefX = xCoef_sq * xVar_X
        xDelta_var = xVar_Y - np.sum(xVar_CoefX) - xVar_resid       #this is the diversificaation effect
        xDelta_varX = xDelta_var * xVar_CoefX / np.sum(xVar_CoefX)
        xVar_X_adj = xVar_CoefX + xDelta_varX
        xVar_X_adj_pct = xVar_X_adj / xVar_Y
        xVar_resid_pct = xVar_resid / xVar_Y
        print (xVar_X_adj_pct, xVar_resid_pct)
        print(np.sum(xVar_X_adj_pct)+xVar_resid_pct)

        xVar_X_adj_pct = pd.DataFrame(xVar_X_adj_pct)
        xVar_X_adj_pct.reset_index(inplace=True)

        xVar_X_adj_pct.rename(columns={0: 'Risk_Concentration(%)'},inplace=True)
        xVar_X_adj_pct.rename(columns={'index': 'Risk_Factor'},inplace=True)
        xVar_X_adj_pct=xVar_X_adj_pct.append({'Risk_Factor':'Idiosyncratic', 'Risk_Concentration(%)': xVar_resid_pct}, ignore_index=True)

        xVar_X_adj_pct=xVar_X_adj_pct.loc[~xVar_X_adj_pct['Risk_Factor'].isin({'const'})]
        xSum = xVar_X_adj_pct['Risk_Concentration(%)'].sum()
        xVar_X_adj_pct=xVar_X_adj_pct.append({'Risk_Factor':'Sum', 'Risk_Concentration(%)': xSum}, ignore_index=True)
        xVar_X_adj_pct=xVar_X_adj_pct.append({'Risk_Factor':model.endog_names+'(Annual StDev)', 'Risk_Concentration(%)': xAnnRisk_Y_Y}, ignore_index=True)
        xVar_X_adj_pct=xVar_X_adj_pct.append({'Risk_Factor':model.endog_names+'(Annual Rtn)', 'Risk_Concentration(%)': xAnnRtn_Y_Y}, ignore_index=True)

        xVar_X_adj_pct['Risk_Concentration(%)'] = xVar_X_adj_pct['Risk_Concentration(%)'].astype(float).map("{:.2%}".format)
        xVar_X_adj_pct=xVar_X_adj_pct.append({'Risk_Factor':model.endog_names+'(Sharpe Ratio)', 'Risk_Concentration(%)': np.round(xAnnRtn_Y_Y/xAnnRisk_Y_Y,2)}, ignore_index=True)

        # for x in (result.tvalues.index):
        #     if x=='const':
        #         continue
        #     else:
        #         #print (x, result.tvalues[x])
        #         if (abs(result.tvalues[x]) <1.5):
        #             xVar_X_adj_pct[xVar_X_adj_pct['Risk_Factor'] == x]['Risk_Exposure(%)'] = 'NA'
        #             #print (x, xVar_X_adj_pct[xVar_X_adj_pct['Risk_Factor']==x]['Risk_Exposure(%)'])

        #####globals()['xRisk_concentration_'+x] = xVar_X_adj_pct

        xRisk_Exposure_Y = xVar_X_adj_pct.to_string()

        f = open(xDir + 'xRisk_Concentration_Y_' + xY_col + '_' + x + '.txt', 'w')
        f.write(xRisk_Exposure_Y + '\r\n')
        f.close()

        ################# store Risk Concentration for the Current Portfolio ###############
        xRiskConcentration_temp = xVar_X_adj_pct[['Risk_Factor', 'Risk_Concentration(%)']].copy()
        xRiskConcentration_temp.rename(columns={'Risk_Concentration(%)': xY_col}, inplace=True)
        xRiskConcentration_temp['Risk_Factor'][len(xRiskConcentration_temp) - 1] = 'Sharpe_Ratio'
        xRiskConcentration_temp['Risk_Factor'][len(xRiskConcentration_temp) - 2] = 'Annual_Rtn'
        xRiskConcentration_temp['Risk_Factor'][len(xRiskConcentration_temp) - 3] = 'Annual_StdDev'
        if len(globals()['xRisk_concentration_'+x]) == 0:
            globals()['xRisk_concentration_'+x] = xRiskConcentration_temp.copy()
        else:
            globals()['xRisk_concentration_'+x] = pd.merge(globals()['xRisk_concentration_'+x], xRiskConcentration_temp, on=['Risk_Factor'], how='left')

        # ######################################
        ############### the following is working on the Std Dev (RISK) ANNUALLY #######
        xStdDev_X = np.array(X.std())   #these are already annualized std dev
        xStdDev_Y = Y.std()     #these are already annualized std dev
        xCoef = result.params.abs()
        xStdDev_resid = result.resid.std()
        xStdDev_CoefX = xCoef * xStdDev_X
        xDelta_StdDev = xStdDev_Y - np.sum(xStdDev_CoefX) - xStdDev_resid  #this is the diversification benefit...
        print('xDelta_StdDev = ', xDelta_StdDev)
        xAdj_StdDev_resid = False
        if (xAdj_StdDev_resid == False):
            xDelta_StdDevX = xDelta_StdDev * xStdDev_CoefX / np.sum(xStdDev_CoefX)
        else:
            xDelta_StdDevX = xDelta_StdDev * xStdDev_CoefX / (np.sum(xStdDev_CoefX) + xStdDev_resid)
            xStdDev_resid = xStdDev_resid + xDelta_StdDev * xStdDev_resid / (np.sum(xStdDev_CoefX) + xStdDev_resid)
        xStdDev_X_adj = xStdDev_CoefX + xDelta_StdDevX

        xStdDev_X_adj = pd.DataFrame(xStdDev_X_adj)
        xStdDev_X_adj.reset_index(inplace=True)

        xStdDev_X_adj.rename(columns={0: 'Risk_Exposure(%)'},inplace=True)
        xStdDev_X_adj.rename(columns={'index': 'Risk_Factor'},inplace=True)
        xStdDev_X_adj=xStdDev_X_adj.append({'Risk_Factor':'Idiosyncratic', 'Risk_Exposure(%)': xStdDev_resid}, ignore_index=True)

        xStdDev_X_adj=xStdDev_X_adj.loc[~xStdDev_X_adj['Risk_Factor'].isin({'const'})]
        xSum = xStdDev_X_adj['Risk_Exposure(%)'].sum()
        xStdDev_X_adj=xStdDev_X_adj.append({'Risk_Factor':'Sum', 'Risk_Exposure(%)': xSum}, ignore_index=True)
        xStdDev_X_adj=xStdDev_X_adj.append({'Risk_Factor':model.endog_names+'(Annual StDev)', 'Risk_Exposure(%)': xAnnRisk_Y_Y}, ignore_index=True)
        xStdDev_X_adj=xStdDev_X_adj.append({'Risk_Factor':model.endog_names+'(Annual Rtn)', 'Risk_Exposure(%)': xAnnRtn_Y_Y}, ignore_index=True)

        #xStdDev_X_adj['Risk_Exposure(%)'] = xStdDev_X_adj['Risk_Exposure(%)'].astype(float).map("{:.2%}".format)

        xStdDev_X_adj=xStdDev_X_adj.append({'Risk_Factor':'Sharpe Ratio (Rtn/Risk)', 'Risk_Exposure(%)': np.round(xAnnRtn_Y_Y / xAnnRisk_Y_Y,2)}, ignore_index=True)
        xStdDev_X_adj=xStdDev_X_adj.append({'Risk_Factor':'Diversification benefit', 'Risk_Exposure(%)': xDelta_StdDev}, ignore_index=True)

        if x== 'Current':
            xStdDev_X_adj.rename(columns={'Risk_Exposure(%)': x + ' Risk (' + xY_col + ')'}, inplace=True)
        else:
            xStdDev_X_adj.rename(columns={'Risk_Exposure(%)': x + ' Risk (proposed)'}, inplace=True)
        globals()['xRisk_exposures_' + x] = xStdDev_X_adj

        xIndex_StdDev=globals()['xRisk_exposures_' + x][
            globals()['xRisk_exposures_' + x]['Risk_Factor'] == model.endog_names + '(Annual StDev)'].index.values[0]
        xIndex_Rtn = globals()['xRisk_exposures_' + x][
            globals()['xRisk_exposures_' + x]['Risk_Factor'] == model.endog_names + '(Annual Rtn)'].index.values[0]
        globals()['xRisk_exposures_' + x].loc[globals()['xRisk_exposures_' + x].index == xIndex_StdDev, 'Risk_Factor'] = 'Annual StdDev'
        globals()['xRisk_exposures_' + x].loc[
            globals()['xRisk_exposures_' + x].index == xIndex_Rtn, 'Risk_Factor'] = 'Annual Rtn'

        globals()['xIdio_exp_' + x] = xStdDev_resid / xSum

        if x=='New':  # second time and last time!
            xStdDev_X_adj = pd.merge(xRisk_exposures_Current, xRisk_exposures_New, on='Risk_Factor', how='left')

        xRisk_Exposure_Y_StdDev = xStdDev_X_adj.to_string()

        ######################################################################
        #xRisk_Exposure_Y.to_csv (xDir + 'xRisk_Exposure_Y.txt')

        f = open(xDir + 'xRisk_Exposure_Y_' + xY_col +  '_' + x + '.txt','w')
        f.write(xRisk_Exposure_Y_StdDev + '\r\n')
        f.close()
        ############### store oefficients for 'Current" portfolio ########
        if x=='Current':
            xCoef_temp = pd.DataFrame(result.params).reset_index()
            xCoef_temp.rename(columns={0: xY_col}, inplace=True)
            xCoef_temp[xY_col] = xCoef_temp[xY_col].round(4)
            xCoef_temp.rename(columns={'index': 'Risk_Factor'}, inplace=True)
            if len(xCoef_table)==0:
                xCoef_table = xCoef_temp.copy()
            else:
                xCoef_table = pd.merge(xCoef_table, xCoef_temp, on=['Risk_Factor'],how='left')
        ############### the following is working on the Std Dev (RISK) ANNUALLY with AR(1) error term #######
        if False:
            ###################### the following is AR(1) error term #########################
            from statsmodels.tsa.arima.model import ARIMA as ARIMA

            X2 = X.drop('const', axis=1)
            sarimax_model = ARIMA(endog=Y, exog=X2, order=(1, 0, 0))  # X already has a constant term, trend='c')  # , seasonal_order=(0,1,1,24))
            sarimax_results = sarimax_model.fit()
            sarimax_results.summary()

            xOLS_AR1_Summary_Y = sarimax_results.summary()
            xOLS_AR1_text = xOLS_AR1_Summary_Y.as_text()

            f = open(xDir + 'xOLS_AR1_Y_' + xY_col + '_' + x + '.txt', 'w')
            f.write(xOLS_AR1_text + '\r\n')
            f.close()

            xStdDev_X = np.array(X.std())   #these are already annualized std dev
            xStdDev_Y = Y.std()     #these are already annualized std dev
            xCoef = sarimax_results.params[:len(X.columns)].abs()
            xStdDev_resid = np.sqrt(sarimax_results.params[len(X.columns):].values[1] / (1-sarimax_results.params[len(X.columns):].values[0]**2)) #result.resid.std()
            xStdDev_CoefX = xCoef * xStdDev_X
            xDelta_StdDev = xStdDev_Y - np.sum(xStdDev_CoefX) - xStdDev_resid
            print('xDelta_StdDev = ', xDelta_StdDev)
            xAdj_StdDev_resid = False
            if (xAdj_StdDev_resid == False):
                xDelta_StdDevX = xDelta_StdDev * xStdDev_CoefX / np.sum(xStdDev_CoefX)
            else:
                xDelta_StdDevX = xDelta_StdDev * xStdDev_CoefX / (np.sum(xStdDev_CoefX) + xStdDev_resid)
                xStdDev_resid = xStdDev_resid + xDelta_StdDev * xStdDev_resid / (np.sum(xStdDev_CoefX) + xStdDev_resid)
            xStdDev_X_adj = xStdDev_CoefX + xDelta_StdDevX

            xStdDev_X_adj = pd.DataFrame(xStdDev_X_adj)
            xStdDev_X_adj.reset_index(inplace=True)

            xStdDev_X_adj.rename(columns={0: 'Risk_Exposure(%)'},inplace=True)
            xStdDev_X_adj.rename(columns={'index': 'Risk_Factor'},inplace=True)
            xStdDev_X_adj=xStdDev_X_adj.append({'Risk_Factor':'Idiosyncratic', 'Risk_Exposure(%)': xStdDev_resid}, ignore_index=True)

            xStdDev_X_adj=xStdDev_X_adj.loc[~xStdDev_X_adj['Risk_Factor'].isin({'const'})]
            xSum = xStdDev_X_adj['Risk_Exposure(%)'].sum()
            xStdDev_X_adj=xStdDev_X_adj.append({'Risk_Factor':'Sum', 'Risk_Exposure(%)': xSum}, ignore_index=True)
            xStdDev_X_adj=xStdDev_X_adj.append({'Risk_Factor':model.endog_names+'(Annual StDev)', 'Risk_Exposure(%)': xAnnRisk_Y_Y}, ignore_index=True)
            xStdDev_X_adj=xStdDev_X_adj.append({'Risk_Factor':model.endog_names+'(Annual Rtn)', 'Risk_Exposure(%)': xAnnRtn_Y_Y}, ignore_index=True)

            #xStdDev_X_adj['Risk_Exposure(%)'] = xStdDev_X_adj['Risk_Exposure(%)'].astype(float).map("{:.2%}".format)

            xStdDev_X_adj=xStdDev_X_adj.append({'Risk_Factor':'Sharpe Ratio (Rtn/Risk)', 'Risk_Exposure(%)': np.round(xAnnRtn_Y_Y / xAnnRisk_Y_Y,2)}, ignore_index=True)

            if x== 'Current':
                xStdDev_X_adj.rename(columns={'Risk_Exposure(%)': x + ' Risk (' + xY_col + ')'}, inplace=True)
            else:
                xStdDev_X_adj.rename(columns={'Risk_Exposure(%)': x + ' Risk (proposed)'}, inplace=True)
            globals()['xRisk_exposures_' + x] = xStdDev_X_adj

            xIndex_StdDev=globals()['xRisk_exposures_' + x][
                globals()['xRisk_exposures_' + x]['Risk_Factor'] == model.endog_names + '(Annual StDev)'].index.values[0]
            xIndex_Rtn = globals()['xRisk_exposures_' + x][
                globals()['xRisk_exposures_' + x]['Risk_Factor'] == model.endog_names + '(Annual Rtn)'].index.values[0]
            globals()['xRisk_exposures_' + x].loc[globals()['xRisk_exposures_' + x].index == xIndex_StdDev, 'Risk_Factor'] = 'Annual StdDev'
            globals()['xRisk_exposures_' + x].loc[
                globals()['xRisk_exposures_' + x].index == xIndex_Rtn, 'Risk_Factor'] = 'Annual Rtn'

            globals()['xIdio_exp_' + x] = xStdDev_resid / xSum

            if x=='New':  # second time and last time!
                xStdDev_X_adj = pd.merge(xRisk_exposures_Current, xRisk_exposures_New, on='Risk_Factor', how='left')


            xRisk_Exposure_Y_StdDev = xStdDev_X_adj.to_string()

            ######################################################################
            #xRisk_Exposure_Y.to_csv (xDir + 'xRisk_Exposure_Y.txt')

            f = open(xDir + 'xRisk_Exposure_Y_AR(1)_' + xY_col +  '_' + x + '.txt','w')
            f.write(xRisk_Exposure_Y_StdDev + '\r\n')
            f.close()

    ######################
    xStdDev_X_Y = pd.DataFrame(X.std()).reset_index()
    xStdDev_X_Y.rename(columns={0:'Risk_Factor_AnnStdDev'}, inplace=True)
    xStdDev_X_Y.rename(columns={'index':'Risk_Factor'}, inplace=True)
    xStdDev_X_adj = pd.merge(xStdDev_X_adj,xStdDev_X_Y, on=['Risk_Factor'],how='left')
    xStdDev_X_adj['Risk_Exp (Current)'] = xStdDev_X_adj['Current Risk ('+xY_col+')']/xStdDev_X_adj['Risk_Factor_AnnStdDev']
    xStdDev_X_adj['Risk_Exp (New)'] = xStdDev_X_adj['New Risk (proposed)']/xStdDev_X_adj['Risk_Factor_AnnStdDev']
    xStdDev_X_adj.loc[xStdDev_X_adj['Risk_Factor']=='Idiosyncratic','Risk_Exp (Current)']=xIdio_exp_Current
    xStdDev_X_adj.loc[xStdDev_X_adj['Risk_Factor']=='Idiosyncratic','Risk_Exp (New)']=xIdio_exp_New
    xSum_Risk_Exp_Current = xStdDev_X_adj['Risk_Exp (Current)'].sum()
    xSum_Risk_Exp_New = xStdDev_X_adj['Risk_Exp (New)'].sum()
    xStdDev_X_adj['Risk_Exp (Current)'] = xStdDev_X_adj['Risk_Exp (Current)']/xSum_Risk_Exp_Current
    xStdDev_X_adj['Risk_Exp (New)'] = xStdDev_X_adj['Risk_Exp (New)']/xSum_Risk_Exp_New
    xSum_Risk_Exp_Current = xStdDev_X_adj['Risk_Exp (Current)'].sum()
    xSum_Risk_Exp_New = xStdDev_X_adj['Risk_Exp (New)'].sum()
    xStdDev_X_adj.loc[xStdDev_X_adj['Risk_Factor']=='Sum','Risk_Exp (Current)']=xSum_Risk_Exp_Current
    xStdDev_X_adj.loc[xStdDev_X_adj['Risk_Factor']=='Sum','Risk_Exp (New)']=xSum_Risk_Exp_New

    xPart_1=xStdDev_X_adj.loc[xStdDev_X_adj.index<len(xStdDev_X_adj)-1]
    xPart_2=xStdDev_X_adj.loc[xStdDev_X_adj.index==len(xStdDev_X_adj)-1]

    xPart_1['Current Risk ('+xY_col+')'] = xPart_1['Current Risk ('+xY_col+')'].astype(float).map("{:.2%}".format)
    xPart_1['New Risk (proposed)'] = xPart_1['New Risk (proposed)'].astype(float).map("{:.2%}".format)
    xPart_1['Risk_Factor_AnnStdDev'] = xPart_1['Risk_Factor_AnnStdDev'].astype(float).map("{:.2%}".format)
    xPart_1['Risk_Exp (Current)'] = xPart_1['Risk_Exp (Current)'].astype(float).map("{:.2%}".format)
    xPart_1['Risk_Exp (New)'] = xPart_1['Risk_Exp (New)'].astype(float).map("{:.2%}".format)

    xStdDev_X_adj=xPart_1.append(xPart_2, ignore_index=True)

    xStdDev_X_adj = xStdDev_X_adj.replace({'nan%': ''})
    xStdDev_X_adj = xStdDev_X_adj.replace({np.nan: ''})

    xRisk_Exposure_Y_StdDev = xStdDev_X_adj.to_string()
    #xStdDev_X_adj['Risk_Exposure(%)'] = xStdDev_X_adj['Risk_Exposure(%)'].astype(float).map("{:.2%}".format)
    ######################
    f = open(xDir + 'xRisk_Exposure_Y_' + xY_col + '.txt','w')
    f.write('From '+xStartDate_Y.strftime('%Y-%m-%d') +' to ' + xEndDate_Y.strftime('%Y-%m-%d') + '\n\n' +xRisk_Exposure_Y_StdDev + '\r\n')
    f.close()
    ################# store Risk Exposures for the Current Portfolio ###############
    xRiskExp_Current_temp = xStdDev_X_adj[['Risk_Factor','Risk_Exp (Current)']].copy()
    xRiskExp_Current_temp.rename(columns={'Risk_Exp (Current)':xY_col}, inplace=True)
    if len(xRiskExp_Current)==0:
        xRiskExp_Current = xRiskExp_Current_temp.copy()
    else:
        xRiskExp_Current = pd.merge(xRiskExp_Current,xRiskExp_Current_temp,on=['Risk_Factor'],how='left')

#res = pd.concat([xRiskExp_Current, xCoef_table], axis=1, keys=["Risk_Exp", "Coefs"])
d={} #dictionary of dataframe
xRiskExp_Current2 = xRiskExp_Current.loc[xRiskExp_Current['Risk_Factor'].isin(list(xRiskFactorSet_Y+['Idiosyncratic']))]
d['Current_Risk_Exposures']=xRiskExp_Current2.set_index('Risk_Factor')
d=pd.concat(d, axis=1)

A={}
xCoef_table2 = xCoef_table.loc[xCoef_table['Risk_Factor'].isin(xRiskFactorSet_Y)]
A['Coefficients']=xCoef_table2.set_index('Risk_Factor')
A=pd.concat(A, axis=1)

B={}
##xRisk_concentration_Current2 = xRisk_concentration_Current.loc[xRisk_concentration_Current['Risk_Factor'].isin(xRiskFactorSet_Y)]
B['Current_Risk_Concentration']=xRisk_concentration_Current.set_index('Risk_Factor')
B=pd.concat(B, axis=1)

C={}
###xRisk_concentration_New2 = xRisk_concentration_New.loc[xRisk_concentration_New['Risk_Factor'].isin(xRiskFactorSet_Y)]
C['New_Risk_Concentration']=xRisk_concentration_New.set_index('Risk_Factor')
C=pd.concat(C, axis=1)

# A2=pd.merge(A,d,on=['Risk_Factor'],how='outer')
# A2.reset_index(inplace=True)
#
# A2_text = A2.to_csv()   #.to_string()
#
# if xOrthogonal == 'orthog':
#     f = open(xDir + 'xCoef_Risk_Exposure_Y_' + xOrthogonal+'.csv','w')
# else:
#     f = open(xDir + 'xCoef_Risk_Exposure_Y.csv', 'w')
# f.write(A2_text + '\r\n')
# f.close()
# ############################
# A2_text = A2.to_string()
#
# if xOrthogonal == 'orthog':
#     f = open(xDir + 'xCoef_Risk_Exposure_Y_' + xOrthogonal+'.txt','w')
# else:
#     f = open(xDir + 'xCoef_Risk_Exposure_Y.txt', 'w')
# f.write(A2_text + '\r\n')
# f.close()

# create excel writer
if xOrthogonal == 'orthog':
    writer = pd.ExcelWriter(xDir + 'xRiskFactorExp_Corre_orthog.xlsx')
    d.reset_index().to_excel(writer, 'Risk_Exposures_orthog')
    A.reset_index().to_excel(writer, 'Coefficients_orthog')
    xRiskFactorCorrelations_orthog.to_excel(writer, 'Corre_RiskFactor_orthog')
    B.reset_index().to_excel(writer, 'Risk_Concentration_orthog')
else:
    writer = pd.ExcelWriter(xDir + 'xRiskFactorExp_Corre_raw.xlsx')
    d.reset_index().to_excel(writer, 'Risk_Exposures_raw')
    A.reset_index().to_excel(writer, 'Coefficients_raw')
    xRiskFactorCorrelations_raw.to_excel(writer, 'Corre_RiskFactor_raw')
    B.reset_index().to_excel(writer, 'Risk_Concentration_raw')
#writer = pd.ExcelWriter(xDir + 'xRiskFactorExp_Corre.xlsx')
# write dataframe to excel sheet named 'marks'
# xRiskFactorCorrelations_orthog.to_excel(writer, 'Corre_RiskFactor_orthog')
# xRiskFactorCorrelations_raw.to_excel(writer, 'Corre_RiskFactor_raw')
# d.reset_index().to_excel(writer, 'Risk_Exposures')
# A.reset_index().to_excel(writer, 'Coefficients')
# save the excel file
writer.save()
writer.close()
###
#
#
##################################################################################
######################################
############### DAILY ###################
xCols_pct_ch_D= xDF.columns[xDF.columns.str.contains(pat = '_pct_ch_D')]
xCols_pct_ch_D=xCols_pct_ch_D.insert(0,'DATE')

xDF_OLS_D=xDF[xCols_pct_ch_D].copy()

xDF_OLS_D.dropna(inplace=True)
xDF_OLS_D.reset_index(drop=True,inplace=True)
############################
xStartDate_D = xDF_OLS_D['DATE'].min()
xEndDate_D = xDF_OLS_D['DATE'].max()
############################
xMean_OLS_D=xDF_OLS_D.mean()*252
xStdDev_OLS_D=xDF_OLS_D.std()*np.sqrt(252)
xStdDev_OLS_D.to_csv(xDir+'xStdDev_OLS_D.txt')
xMean_OLS_D.to_csv(xDir+'xMean_OLS_D.txt')

#################### model portfolios for daily returns ############
xMP_D = xDF_OLS_D[['DATE']].copy()
xMP_D = pd.merge(xMP_D, xMP[['DATE','CONS_pct_ch_D','MODCONS_pct_ch_D','MOD_pct_ch_D','MODGROW_pct_ch_D',
                'GROW_pct_ch_D','MAXGROW_pct_ch_D','Current_pct_ch_D','New_pct_ch_D']], on=['DATE'], how='left')

xMP_D_CumRtn = (1+xMP_D[['CONS_pct_ch_D','MODCONS_pct_ch_D','MOD_pct_ch_D','MODGROW_pct_ch_D','GROW_pct_ch_D',
                         'MAXGROW_pct_ch_D','Current_pct_ch_D','New_pct_ch_D']]).cumprod()
xMP_D_AnnRtn = (xMP_D_CumRtn.iloc[len(xMP_D_CumRtn)-1]/xMP_D_CumRtn.iloc[0])**(1/(len(xMP_D_CumRtn)/252))-1

xMP_D_AnnRtn = xMP_D_AnnRtn.reset_index()
xMP_D_AnnRisk = xMP_D[['CONS_pct_ch_D','MODCONS_pct_ch_D','MOD_pct_ch_D','MODGROW_pct_ch_D','GROW_pct_ch_D',
                       'MAXGROW_pct_ch_D','Current_pct_ch_D','New_pct_ch_D']].std().reset_index()
xMP_D_AnnRtn.rename(columns={0: 'AnnRtn'},inplace=True)
xMP_D_AnnRisk.rename(columns={0: 'AnnRisk'},inplace=True)
xMP_D_AnnRisk['AnnRisk']=xMP_D_AnnRisk['AnnRisk']*np.sqrt(252)

xMP_D_AnnRtnRisk = pd.merge(xMP_D_AnnRtn,xMP_D_AnnRisk,on=['index'],how='left')
####################
Y = xDF_OLS_D[xY_col + '_pct_ch_D']
#xInd_Vars = ['SPXT_pct_ch_D','BondTR_pct_ch_D','CCY_pct_ch_D','COMM_pct_ch_D','USCredit_pct_ch_D','HYTR_pct_ch_D']
xInd_Vars = ['SPXT_pct_ch_D','BondTR_pct_ch_D','TIPS_pct_ch_D','CCY_pct_ch_D','COMM_pct_ch_D','USCredit_pct_ch_D','HYTR_pct_ch_D']
xInd_Vars = ['SPXT_pct_ch_D','BondTR_pct_ch_D']
xInd_Vars = ['RLG_pct_ch_D']

X = xDF_OLS_D[xInd_Vars]

xCorrelations_D = xDF_OLS_D[[xY_col + '_pct_ch_D']+xInd_Vars].corr().to_string()
f = open(xDir + 'xCorrelations_D_' + xY_col + '.txt','w')
f.write(xCorrelations_D + '\r\n')
f.close()

X = sm.add_constant(X)
model = sm.OLS(Y,X)
result = model.fit()
xOLS_Summary_D = result.summary()
xOLS_text = xOLS_Summary_D.as_text()

f = open(xDir + 'xOLS_D_' + xY_col + '.txt','w')
f.write(xOLS_text + '\r\n')
f.close()

# ########## calc annualized return Daily ##########
xCumRtn_Y = (1+Y).cumprod()
xAnnRtn_Y_D = (xCumRtn_Y[len(xCumRtn_Y)-1]/xCumRtn_Y[0])**(1/(len(xCumRtn_Y)/252))-1
xAnnRisk_Y_D = np.sqrt(252*Y.var())
# xMP_D_AnnRtnRisk=xMP_D_AnnRtnRisk.append({'index':'Current Portfolio','AnnRtn':xAnnRtn_Y_D,'AnnRisk':xAnnRisk_Y_D}, ignore_index=True)
############################################
xVar_X = np.array(X.var())
xVar_Y = Y.var()
xCoef_sq = result.params**2
xVar_resid = result.resid.var()
xVar_CoefX = xCoef_sq * xVar_X
xDelta_var = xVar_Y - np.sum(xVar_CoefX) - xVar_resid
xDelta_varX = xDelta_var * xVar_CoefX / np.sum(xVar_CoefX)
xVar_X_adj = xVar_CoefX + xDelta_varX
xVar_X_adj_pct = xVar_X_adj / xVar_Y
xVar_resid_pct = xVar_resid / xVar_Y
print (xVar_X_adj_pct, xVar_resid_pct)
print(np.sum(xVar_X_adj_pct)+xVar_resid_pct)

xVar_X_adj_pct = pd.DataFrame(xVar_X_adj_pct)
xVar_X_adj_pct.reset_index(inplace=True)

xVar_X_adj_pct.rename(columns={0: 'Risk_Concentration(%)'},inplace=True)
xVar_X_adj_pct.rename(columns={'index': 'Risk_Factor'},inplace=True)
xVar_X_adj_pct=xVar_X_adj_pct.append({'Risk_Factor':'Idiosyncratic', 'Risk_Concentration(%)': xVar_resid_pct}, ignore_index=True)

xVar_X_adj_pct=xVar_X_adj_pct.loc[~xVar_X_adj_pct['Risk_Factor'].isin({'const'})]
xSum = xVar_X_adj_pct['Risk_Concentration(%)'].sum()
xVar_X_adj_pct=xVar_X_adj_pct.append({'Risk_Factor':'Sum', 'Risk_Concentration(%)': xSum}, ignore_index=True)
xVar_X_adj_pct=xVar_X_adj_pct.append({'Risk_Factor':model.endog_names+'(Annual StDev)', 'Risk_Concentration(%)': xAnnRisk_Y_D}, ignore_index=True)
xVar_X_adj_pct=xVar_X_adj_pct.append({'Risk_Factor':model.endog_names+'(Annual Rtn)', 'Risk_Concentration(%)': xAnnRtn_Y_D}, ignore_index=True)

xVar_X_adj_pct['Risk_Concentration(%)'] = xVar_X_adj_pct['Risk_Concentration(%)'].astype(float).map("{:.2%}".format)
# for x in (result.tvalues.index):
#     if x=='const':
#         continue
#     else:
#         #print (x, result.tvalues[x])
#         if (abs(result.tvalues[x]) < 1.5):
#             xVar_X_adj_pct[xVar_X_adj_pct['Risk_Factor'] == x]['Risk_Exposure(%)'] = 'NA'
#             #print (x, xVar_X_adj_pct[xVar_X_adj_pct['Risk_Factor']==x]['Risk_Exposure(%)'])

xRisk_Exposure_D = xVar_X_adj_pct.to_string()

f = open(xDir + 'xRisk_Concentration_D_' + xY_col + '.txt','w')
f.write(xRisk_Exposure_D + '\r\n')
f.close()

##########################
xCols_pct_MP = xMP.columns[xMP.columns.str.contains(pat = '_pct_ch_D')]
xCols_pct_MP=xCols_pct_MP.insert(0,'DATE')
xMP_D = xMP[xCols_pct_MP].copy()
xMP_D = xMP_D.loc[(xMP_D['DATE']>=xStartDate_D) & (xMP_D['DATE']<=xEndDate_D)]

xMP_D_StDev = pd.DataFrame(xMP_D.std()*np.sqrt(252))
xMP_D_StDev.reset_index(inplace=True)

xThisName=''
i=0
for x in xMP_D_StDev['index']:
    i=i+1
    if (i<=2):
        continue
    xName = xMP_D_StDev['index'][i-1]
    xAnnStDev = xMP_D_StDev[0]
    if (np.sqrt(252*xVar_Y) > xAnnStDev[i-1]):
        xThisName=xName
    xPreviousName=xName

if (xThisName=='MAXGROW_pct_ch_D'):
    xThisName = 'Accessive Growth Risk'
elif (xThisName == 'GROW_pct_ch_D'):
    xThisName = 'Growth Risk'
elif (xThisName == 'MODGROW_pct_ch_D'):
    xThisName = 'Moderate Growth Risk'
elif (xThisName=='MOD_pct_ch_D'):
    xThisName = 'Moderate Risk'
elif (xThisName=='MODCONS_pct_ch_D'):
    xThisName = 'Moderate Conservative Risk'
elif (xThisName=='CONS_pct_ch_D'):
    xThisName = 'Conservative Risk'

################### MONTHLY #################
##################################################
xDF_M['SPXT_pct_ch_M']=xDF_M['SPXT'].pct_change()
xDF_M['BondTR_pct_ch_M']=xDF_M['BondTR'].pct_change()
xDF_M['AAPL_pct_ch_M']=xDF_M['AAPL'].pct_change()
xDF_M['AGG_pct_ch_M']=xDF_M['AGG'].pct_change()
xDF_M['CCY_pct_ch_M']=xDF_M['CCY'].pct_change()
xDF_M['COMM_pct_ch_M']=xDF_M['COMM'].pct_change()
xDF_M['CREDIT_pct_ch_M']=xDF_M['CREDIT'].pct_change()
xDF_M['FTLS_pct_ch_M']=xDF_M['FTLS'].pct_change()
xDF_M['HFRIEMNI_pct_ch_M']=xDF_M['HFRIEMNI'].pct_change()
xDF_M['PRBAX_pct_ch_M']=xDF_M['PRBAX'].pct_change()
xDF_M['PRWAX_pct_ch_M']=xDF_M['PRWAX'].pct_change()
xDF_M['SPLPEQTY_pct_ch_M']=xDF_M['SPLPEQTY'].pct_change()
xDF_M['SPX_pct_ch_M']=xDF_M['SPX'].pct_change()
xDF_M['SPY_pct_ch_M']=xDF_M['SPY'].pct_change()
xDF_M['TSLA_pct_ch_M']=xDF_M['TSLA'].pct_change()
xDF_M['US3M_pct_ch_M']=xDF_M['US3M'].pct_change()
xDF_M['US10Y_pct_ch_M']=xDF_M['US10Y'].pct_change()
xDF_M['HYG_pct_ch_M']=xDF_M['HYG'].pct_change()
xDF_M['HYTR_pct_ch_M']=xDF_M['HYTR'].pct_change()
xDF_M['RealBondTR_pct_ch_M']=xDF_M['RealBondTR'].pct_change()
xDF_M['CPI_pct_ch_M']=xDF_M['CPI'].pct_change()
xDF_M['CPI_pct_ch_Y']=xDF_M['CPI'].pct_change(12)
xDF_M['TIPS_pct_ch_M']=xDF_M['TIPS'].pct_change()
xDF_M['GMWAX_pct_ch_M']=xDF_M['GMWAX'].pct_change()
xDF_M['CashConst_pct_ch_M']=xDF_M['CashConst'].pct_change()
xDF_M['S5INFT_pct_ch_M']=xDF_M['S5INFT'].pct_change()
xDF_M['7030TR_pct_ch_M']=xDF_M['7030TR'].pct_change()
xDF_M['USCredit_pct_ch_M']=xDF_M['USCredit'].pct_change()
xDF_M['SHY_pct_ch_M']=xDF_M['SHY'].pct_change()
xDF_M['TIP_pct_ch_M']=xDF_M['TIP'].pct_change()
xDF_M['GOOG_pct_ch_M']=xDF_M['GOOG'].pct_change()

xDF_M['Inflation_pct_ch_M'] = xDF_M['BondTR_pct_ch_M'] - xDF_M['TIPS_pct_ch_M']

############### overwrite to create the EXACT 70/30 returns #############
xDF_M['7030TR_pct_ch_M']=0.7*xDF_M['SPXT_pct_ch_M']+0.3*xDF_M['BondTR_pct_ch_M']
xDF_M['3070TR_pct_ch_M']=0.3*xDF_M['SPXT_pct_ch_M']+0.7*xDF_M['BondTR_pct_ch_M']
#############################################

xY_col='3070TR' # for Monthly ony here!

xW1=.75
xW2=0.25
xDF_M['New_pct_ch_M']=xDF_M['NewPort'].pct_change()
xDF_M['New_pct_ch_M']=0.2*xDF_M['SPXT_pct_ch_M']+0.60*xDF_M['BondTR_pct_ch_M']+0.2*xDF_M['HFRIEMNI_pct_ch_M']

xRiskFactorSet_M=['SPXT_pct_ch_M','BondTR_pct_ch_M','CCY_pct_ch_M','COMM_pct_ch_M','USCredit_pct_ch_M','HYTR_pct_ch_M',
                  'CPI_pct_ch_M','TIPS_pct_ch_M','Inflation_pct_ch_M','RealBondTR_pct_ch_M']

xRiskFactorSet_M=['SPXT_pct_ch_M','TIPS_pct_ch_M','USCredit_pct_ch_M','CPI_pct_ch_M','COMM_pct_ch_M']
#xRiskFactorSet_M=['SPXT_pct_ch_M','TIPS_pct_ch_M','USCredit_pct_ch_M','CPI_pct_ch_M','COMM_pct_ch_M','HYTR_pct_ch_M']

xRiskFactorSet_M=['SPXT_pct_ch_M','TIPS_pct_ch_M','USCredit_pct_ch_M','COMM_pct_ch_M']

xDescriptive_M=xDF_M[[xY_col+'_pct_ch_M']+xRiskFactorSet_M].describe(include='all').to_string()
xCorrelations_M=xDF_M[[xY_col+'_pct_ch_M']+xRiskFactorSet_M].corr().to_string()

xDescriptive_M = xDescriptive_M + '\n\n' + xCorrelations_M
f = open(xDir + 'xDescriptive_M_'+xY_col+'.txt','w')
f.write(xDescriptive_M + '\r\n')
f.close()

##############################
################### (ROLLING here) QUARTERLY #################
##################################################
xDF_M['SPXT_pct_ch_Q']=xDF_M['SPXT'].pct_change(3)
xDF_M['BondTR_pct_ch_Q']=xDF_M['BondTR'].pct_change(3)
xDF_M['AAPL_pct_ch_Q']=xDF_M['AAPL'].pct_change(3)
xDF_M['AGG_pct_ch_Q']=xDF_M['AGG'].pct_change(3)
xDF_M['CCY_pct_ch_Q']=xDF_M['CCY'].pct_change(3)
xDF_M['COMM_pct_ch_Q']=xDF_M['COMM'].pct_change(3)
xDF_M['CREDIT_pct_ch_Q']=xDF_M['CREDIT'].pct_change(3)
xDF_M['FTLS_pct_ch_Q']=xDF_M['FTLS'].pct_change(3)
xDF_M['HFRIEMNI_pct_ch_Q']=xDF_M['HFRIEMNI'].pct_change(3)
xDF_M['PRBAX_pct_ch_Q']=xDF_M['PRBAX'].pct_change(3)
xDF_M['PRWAX_pct_ch_Q']=xDF_M['PRWAX'].pct_change(3)
xDF_M['SPLPEQTY_pct_ch_Q']=xDF_M['SPLPEQTY'].pct_change(3)
xDF_M['SPX_pct_ch_Q']=xDF_M['SPX'].pct_change(3)
xDF_M['SPY_pct_ch_Q']=xDF_M['SPY'].pct_change(3)
xDF_M['TSLA_pct_ch_Q']=xDF_M['TSLA'].pct_change(3)
xDF_M['US3M_pct_ch_Q']=xDF_M['US3M'].pct_change(3)
xDF_M['US10Y_pct_ch_Q']=xDF_M['US10Y'].pct_change(3)
xDF_M['HYG_pct_ch_Q']=xDF_M['HYG'].pct_change(3)
xDF_M['HYTR_pct_ch_Q']=xDF_M['HYTR'].pct_change(3)
xDF_M['RealBondTR_pct_ch_Q']=xDF_M['RealBondTR'].pct_change(3)
xDF_M['CPI_pct_ch_Q']=xDF_M['CPI'].pct_change(3)
xDF_M['TIPS_pct_ch_Q']=xDF_M['TIPS'].pct_change(3)
xDF_M['GMWAX_pct_ch_Q']=xDF_M['GMWAX'].pct_change(3)
xDF_M['CashConst_pct_ch_Q']=xDF_M['CashConst'].pct_change(3)
xDF_M['S5INFT_pct_ch_Q']=xDF_M['S5INFT'].pct_change(3)
xDF_M['7030TR_pct_ch_Q']=xDF_M['7030TR'].pct_change(3)
xDF_M['USCredit_pct_ch_Q']=xDF_M['USCredit'].pct_change(3)
xDF_M['SHY_pct_ch_Q']=xDF_M['SHY'].pct_change(3)
xDF_M['TIP_pct_ch_Q']=xDF_M['TIP'].pct_change(3)
xDF_M['GOOG_pct_ch_Q']=xDF_M['GOOG'].pct_change(3)

xDF_M['3070TR_pct_ch_Q']=0.3*xDF_M['SPXT_pct_ch_Q']+0.7*xDF_M['BondTR_pct_ch_Q']
xDF_M['New_pct_ch_Q']=xDF_M['NewPort'].pct_change(3)
######################
###xDF_OLS_M = xDF_M.copy()
xDF_OLS_M = xDF_M[['DATE'] + xRiskFactorSet_M + [xY_col+'_pct_ch_M','CPI_pct_ch_Y','New_pct_ch_M','HFRIEMNI_pct_ch_M']].copy()
###################
xDF_OLS_M.dropna(inplace=True)
xDF_OLS_M.reset_index(drop=True,inplace=True)
##################
xStartDate_M = xDF_OLS_M['DATE'].min()
xEndDate_M = xDF_OLS_M['DATE'].max()
#################### model portfolios for Monthly returns ############
xMP_M = xDF_OLS_M[['DATE']].copy()
xMP_M = pd.merge(xMP_M, xMP_MQ[['DATE','CONS_pct_ch_M','MODCONS_pct_ch_M','MOD_pct_ch_M','MODGROW_pct_ch_M','GROW_pct_ch_M',
                'MAXGROW_pct_ch_M','Current_pct_ch_M','New_pct_ch_M']], on=['DATE'], how='left')
xMP_M_CumRtn = (1+xMP_M[['CONS_pct_ch_M','MODCONS_pct_ch_M','MOD_pct_ch_M','MODGROW_pct_ch_M','GROW_pct_ch_M',
                         'MAXGROW_pct_ch_M','Current_pct_ch_M','New_pct_ch_M']]).cumprod()
xMP_M_AnnRtn = (xMP_M_CumRtn.iloc[len(xMP_M_CumRtn)-1]/xMP_M_CumRtn.iloc[0])**(1/(len(xMP_M_CumRtn)/12))-1

xMP_M_AnnRtn = xMP_M_AnnRtn.reset_index()
xMP_M_AnnRisk = xMP_M[['CONS_pct_ch_M','MODCONS_pct_ch_M','MOD_pct_ch_M','MODGROW_pct_ch_M','GROW_pct_ch_M','MAXGROW_pct_ch_M',
                       'Current_pct_ch_M','New_pct_ch_M']].std().reset_index()
xMP_M_AnnRtn.rename(columns={0: 'AnnRtn'},inplace=True)
xMP_M_AnnRisk.rename(columns={0: 'AnnRisk'},inplace=True)
xMP_M_AnnRisk['AnnRisk']=xMP_M_AnnRisk['AnnRisk']*np.sqrt(12)

xMP_M_AnnRtnRisk = pd.merge(xMP_M_AnnRtn,xMP_M_AnnRisk,on=['index'],how='left')

import time
from datetime import timedelta
#start_time = time.monotonic()
#end_time = time.monotonic()

############## OLS MONHTLY ###################
xVersion=['Current','New']
for x in xVersion:
    if x=='Current':
        ##xY_col = 'HFRIEMNI' #### special test!!!!
        Y = xDF_OLS_M[xY_col + '_pct_ch_M']
        xY_col2 = xY_col
    elif x=='New':
        Y = xDF_OLS_M['New_pct_ch_M']
        xY_col2 = 'New'
    #xInd_Vars = ['SPXT_pct_ch_M','BondTR_pct_ch_M','CCY_pct_ch_M','COMM_pct_ch_M','USCredit_pct_ch_M','HYTR_pct_ch_M']
    #xInd_Vars = ['SPXT_pct_ch_M','RealBondTR_pct_ch_M','TIPS_pct_ch_M','CPI_pct_ch_Y','CCY_pct_ch_M','COMM_pct_ch_M','USCredit_pct_ch_M','HYTR_pct_ch_M']
    xInd_Vars = ['SPXT_pct_ch_M', 'Inflation_pct_ch_M', 'TIPS_pct_ch_M', 'CCY_pct_ch_M', 'USCredit_pct_ch_M']
    xInd_Vars = ['SPXT_pct_ch_M', 'Inflation_pct_ch_M', 'TIPS_pct_ch_M', 'CCY_pct_ch_M', 'USCredit_pct_ch_M']
    xInd_Vars = ['SPXT_pct_ch_M']
    xInd_Vars = ['SPXT_pct_ch_M','BondTR_pct_ch_M']
    xInd_Vars = ['SPXT_pct_ch_M','RealBondTR_pct_ch_M','TIPS_pct_ch_M','CPI_pct_ch_Y','CCY_pct_ch_M','COMM_pct_ch_M','USCredit_pct_ch_M','HYTR_pct_ch_M']
    ##xInd_Vars = ['S5INFT_pct_ch_M']
    #xInd_Vars = ['SPXT_pct_ch_M', 'BondTR_pct_ch_M', 'TIPS_pct_ch_M', 'CCY_pct_ch_M', 'USCredit_pct_ch_M']

    xInd_Vars = xRiskFactorSet_M
    xInd_Vars = ['SPXT_pct_ch_M']

    X = xDF_OLS_M[xInd_Vars]
    #X = xDF_OLS_M[['SPXT_pct_ch_M','BondTR_pct_ch_M','CCY_pct_ch_M','COMM_pct_ch_M','USCredit_pct_ch_M']]

    xCorrelations_M = xDF_OLS_M[[xY_col2 + '_pct_ch_M']+xInd_Vars].corr().to_string()
    f = open(xDir + 'xCorrelations_M_' + xY_col + '_'+ x +'.txt','w')
    f.write(xCorrelations_M + '\r\n')
    f.close()

    X = sm.add_constant(X)
    xStart_time = datetime.datetime.now() #time.time_ns()*1000000
    model = sm.OLS(Y,X)
    result = model.fit()
    # for i in range(1,9999):
    #     print(i)
    xEnd_time = datetime.datetime.now() #time.time_ns()*1000000
    globals()['xSecond_M_' + x] = 'Start: ' + (str)(xStart_time) + '; End: ' + (str)(xEnd_time) + '; Duration: ' + (
        str)((xEnd_time - xStart_time))
    xOLS_Summary_M = result.summary()
    xOLS_text = xOLS_Summary_M.as_text()

    f = open(xDir + 'xOLS_M_' + xY_col + '_' + x + '.txt','w')
    f.write(globals()['xSecond_M_' + x] +'\n\n' + xOLS_text + '\r\n')
    f.close()

    ########## calc annualized return from Monthly returns ##########
    xCumRtn_Y = (1+Y).cumprod()
    xAnnRtn_Y_M = (xCumRtn_Y[len(xCumRtn_Y)-1]/xCumRtn_Y[0])**(1/(len(xCumRtn_Y)/12))-1
    xAnnRisk_Y_M = np.sqrt(12*Y.var())
    #xMP_M_AnnRtnRisk=xMP_M_AnnRtnRisk.append({'index':'Current Portfolio','AnnRtn':xAnnRtn_Y_M,'AnnRisk':xAnnRisk_Y_M}, ignore_index=True)

    ############################################

    xVar_X = np.array(X.var())
    xVar_Y = Y.var()
    xCoef_sq = result.params**2
    xVar_resid = result.resid.var()
    xVar_CoefX = xCoef_sq * xVar_X
    xDelta_var = xVar_Y - np.sum(xVar_CoefX) - xVar_resid
    xDelta_varX = xDelta_var * xVar_CoefX / np.sum(xVar_CoefX)
    xVar_X_adj = xVar_CoefX + xDelta_varX
    xVar_X_adj_pct = xVar_X_adj / xVar_Y
    xVar_resid_pct = xVar_resid / xVar_Y
    print (xVar_X_adj_pct, xVar_resid_pct)
    print(np.sum(xVar_X_adj_pct)+xVar_resid_pct)

    xVar_X_adj_pct = pd.DataFrame(xVar_X_adj_pct)
    xVar_X_adj_pct.reset_index(inplace=True)

    xVar_X_adj_pct.rename(columns={0: 'Risk_Exposure(%)'},inplace=True)
    xVar_X_adj_pct.rename(columns={'index': 'Risk_Factor'},inplace=True)
    xVar_X_adj_pct=xVar_X_adj_pct.append({'Risk_Factor':'Idiosyncratic', 'Risk_Exposure(%)': xVar_resid_pct}, ignore_index=True)

    xVar_X_adj_pct=xVar_X_adj_pct.loc[~xVar_X_adj_pct['Risk_Factor'].isin({'const'})]
    xSum = xVar_X_adj_pct['Risk_Exposure(%)'].sum()
    xVar_X_adj_pct=xVar_X_adj_pct.append({'Risk_Factor':'Sum', 'Risk_Exposure(%)': xSum}, ignore_index=True)
    xVar_X_adj_pct=xVar_X_adj_pct.append({'Risk_Factor':model.endog_names+'(Annual StDev)', 'Risk_Exposure(%)': xAnnRisk_Y_M}, ignore_index=True)
    xVar_X_adj_pct=xVar_X_adj_pct.append({'Risk_Factor':model.endog_names+'(Annual Rtn)', 'Risk_Exposure(%)': xAnnRtn_Y_M}, ignore_index=True)

    xVar_X_adj_pct['Risk_Exposure(%)'] = xVar_X_adj_pct['Risk_Exposure(%)'].astype(float).map("{:.2%}".format)
    # for x in (result.tvalues.index):
    #     if x=='const':
    #         continue
    #     else:
    #         #print (x, result.tvalues[x])
    #         if (abs(result.tvalues[x]) <1.5):
    #             xVar_X_adj_pct[xVar_X_adj_pct['Risk_Factor'] == x]['Risk_Exposure(%)'] = 'NA'
    #             #print (x, xVar_X_adj_pct[xVar_X_adj_pct['Risk_Factor']==x]['Risk_Exposure(%)'])

    xRisk_Exposure_M = xVar_X_adj_pct.to_string()
    #xRisk_Exposure_M.to_csv (xDir + 'xRisk_Exposure_M.txt')

    f = open(xDir + 'xRisk_Concentration_M_' + xY_col + '_'+ x + '.txt','w')
    f.write(xRisk_Exposure_M + '\r\n')
    f.close()
    ################## the following is working on StdDev monthly ###############
    ############### the following is working on the Std Dev (RISK) MONTHLY #######
    xStdDev_X = np.array(X.std()) * np.sqrt(12)
    xStdDev_Y = Y.std() * np.sqrt(12)
    xCoef = result.params.abs()
    xStdDev_resid = result.resid.std() * np.sqrt(12)
    xStdDev_CoefX = xCoef * xStdDev_X
    xDelta_StdDev = xStdDev_Y - np.sum(xStdDev_CoefX) - xStdDev_resid
    ####### debug ########
    print('Monthly '+x+': xDelta_StdDev = ', xDelta_StdDev,'\n')
    print('Monthly '+x+': xStdDev_Y = ', xStdDev_Y,'\n')
    print('Monthly '+x+': xStdDev_X = ', xStdDev_X,'\n')
    print('Monthly '+x+': xStdDev_CoefX = ', xStdDev_CoefX,'\n')
    print('Monthly '+x+': xStdDev_resid = ', xStdDev_resid,'\n')
    ######################
    xAdj_StdDev_resid = False
    if (xAdj_StdDev_resid == False):
        xDelta_StdDevX = xDelta_StdDev * xStdDev_CoefX / np.sum(xStdDev_CoefX)
    else:
        xDelta_StdDevX = xDelta_StdDev * xStdDev_CoefX / (np.sum(xStdDev_CoefX) + xStdDev_resid)
        xStdDev_resid = xStdDev_resid + xDelta_StdDev * xStdDev_resid / (np.sum(xStdDev_CoefX) + xStdDev_resid)
    xStdDev_X_adj = xStdDev_CoefX + xDelta_StdDevX

    xStdDev_X_adj = pd.DataFrame(xStdDev_X_adj)
    xStdDev_X_adj.reset_index(inplace=True)

    xStdDev_X_adj.rename(columns={0: 'Risk_Exposure(%)'},inplace=True)
    xStdDev_X_adj.rename(columns={'index': 'Risk_Factor'},inplace=True)
    xStdDev_X_adj=xStdDev_X_adj.append({'Risk_Factor':'Idiosyncratic', 'Risk_Exposure(%)': xStdDev_resid}, ignore_index=True)

    xStdDev_X_adj=xStdDev_X_adj.loc[~xStdDev_X_adj['Risk_Factor'].isin({'const'})]
    xSum = xStdDev_X_adj['Risk_Exposure(%)'].sum()
    xStdDev_X_adj=xStdDev_X_adj.append({'Risk_Factor':'Sum', 'Risk_Exposure(%)': xSum}, ignore_index=True)
    xStdDev_X_adj=xStdDev_X_adj.append({'Risk_Factor':model.endog_names+'(Annual StDev)', 'Risk_Exposure(%)': xAnnRisk_Y_M}, ignore_index=True)
    xStdDev_X_adj=xStdDev_X_adj.append({'Risk_Factor':model.endog_names+'(Annual Rtn)', 'Risk_Exposure(%)': xAnnRtn_Y_M}, ignore_index=True)

    #xStdDev_X_adj['Risk_Exposure(%)'] = xStdDev_X_adj['Risk_Exposure(%)'].astype(float).map("{:.2%}".format)

    xStdDev_X_adj=xStdDev_X_adj.append({'Risk_Factor':'Sharpe Ratio (Rtn/Risk)', 'Risk_Exposure(%)': np.round(xAnnRtn_Y_M / xAnnRisk_Y_M,2)}, ignore_index=True)

    if x== 'Current':
        xStdDev_X_adj.rename(columns={'Risk_Exposure(%)': x + ' Risk (' + xY_col + ')'}, inplace=True)
    else:
        xStdDev_X_adj.rename(columns={'Risk_Exposure(%)': x + ' Risk (proposed)'}, inplace=True)
    globals()['xRisk_exposures_' + x] = xStdDev_X_adj

    xIndex_StdDev=globals()['xRisk_exposures_' + x][
        globals()['xRisk_exposures_' + x]['Risk_Factor'] == model.endog_names + '(Annual StDev)'].index.values[0]
    xIndex_Rtn = globals()['xRisk_exposures_' + x][
        globals()['xRisk_exposures_' + x]['Risk_Factor'] == model.endog_names + '(Annual Rtn)'].index.values[0]
    globals()['xRisk_exposures_' + x].loc[globals()['xRisk_exposures_' + x].index == xIndex_StdDev, 'Risk_Factor'] = 'Annual StdDev'
    globals()['xRisk_exposures_' + x].loc[
        globals()['xRisk_exposures_' + x].index == xIndex_Rtn, 'Risk_Factor'] = 'Annual Rtn'

    globals()['xIdio_exp_' + x] = xStdDev_resid / xSum

    if x=='New':  # second time and last time!
        xStdDev_X_adj = pd.merge(xRisk_exposures_Current, xRisk_exposures_New, on='Risk_Factor', how='left')

    xRisk_Exposure_M_StdDev = xStdDev_X_adj.to_string()

    ######################################################################
    #xRisk_Exposure_Y.to_csv (xDir + 'xRisk_Exposure_Y.txt')

    f = open(xDir + 'xRisk_Exposure_M_' + xY_col +  '_' + x + '.txt','w')
    f.write(xRisk_Exposure_M_StdDev + '\r\n')
    f.close()
######################
xStdDev_X_M = pd.DataFrame(X.std() * np.sqrt(12)).reset_index()
xStdDev_X_M.rename(columns={0:'Risk_Factor_AnnStdDev'}, inplace=True)
xStdDev_X_M.rename(columns={'index':'Risk_Factor'}, inplace=True)
xStdDev_X_adj = pd.merge(xStdDev_X_adj,xStdDev_X_M, on=['Risk_Factor'],how='left')
xStdDev_X_adj['Risk_Exp (Current)'] = xStdDev_X_adj['Current Risk ('+xY_col+')']/xStdDev_X_adj['Risk_Factor_AnnStdDev']
xStdDev_X_adj['Risk_Exp (New)'] = xStdDev_X_adj['New Risk (proposed)']/xStdDev_X_adj['Risk_Factor_AnnStdDev']
xStdDev_X_adj.loc[xStdDev_X_adj['Risk_Factor']=='Idiosyncratic','Risk_Exp (Current)']=xIdio_exp_Current
xStdDev_X_adj.loc[xStdDev_X_adj['Risk_Factor']=='Idiosyncratic','Risk_Exp (New)']=xIdio_exp_New
xSum_Risk_Exp_Current = xStdDev_X_adj['Risk_Exp (Current)'].sum()
xSum_Risk_Exp_New = xStdDev_X_adj['Risk_Exp (New)'].sum()
xStdDev_X_adj['Risk_Exp (Current)'] = xStdDev_X_adj['Risk_Exp (Current)']/xSum_Risk_Exp_Current
xStdDev_X_adj['Risk_Exp (New)'] = xStdDev_X_adj['Risk_Exp (New)']/xSum_Risk_Exp_New
xSum_Risk_Exp_Current = xStdDev_X_adj['Risk_Exp (Current)'].sum()
xSum_Risk_Exp_New = xStdDev_X_adj['Risk_Exp (New)'].sum()
xStdDev_X_adj.loc[xStdDev_X_adj['Risk_Factor']=='Sum','Risk_Exp (Current)']=xSum_Risk_Exp_Current
xStdDev_X_adj.loc[xStdDev_X_adj['Risk_Factor']=='Sum','Risk_Exp (New)']=xSum_Risk_Exp_New

xPart_1=xStdDev_X_adj.loc[xStdDev_X_adj.index<len(xStdDev_X_adj)-1]
xPart_2=xStdDev_X_adj.loc[xStdDev_X_adj.index==len(xStdDev_X_adj)-1]

xPart_1['Current Risk ('+xY_col+')'] = xPart_1['Current Risk ('+xY_col+')'].astype(float).map("{:.2%}".format)
xPart_1['New Risk (proposed)'] = xPart_1['New Risk (proposed)'].astype(float).map("{:.2%}".format)
xPart_1['Risk_Factor_AnnStdDev'] = xPart_1['Risk_Factor_AnnStdDev'].astype(float).map("{:.2%}".format)
xPart_1['Risk_Exp (Current)'] = xPart_1['Risk_Exp (Current)'].astype(float).map("{:.2%}".format)
xPart_1['Risk_Exp (New)'] = xPart_1['Risk_Exp (New)'].astype(float).map("{:.2%}".format)

xStdDev_X_adj=xPart_1.append(xPart_2, ignore_index=True)

xStdDev_X_adj = xStdDev_X_adj.replace({'nan%': ''})
xStdDev_X_adj = xStdDev_X_adj.replace({np.nan: ''})

xRisk_Exposure_M_StdDev = xStdDev_X_adj.to_string()
#xStdDev_X_adj['Risk_Exposure(%)'] = xStdDev_X_adj['Risk_Exposure(%)'].astype(float).map("{:.2%}".format)
######################
f = open(xDir + 'xRisk_Exposure_M_' + xY_col + '.txt','w')
f.write('From '+xStartDate_M.strftime('%Y-%m-%d') +' to ' + xEndDate_M.strftime('%Y-%m-%d') + '\n\n' + xRisk_Exposure_M_StdDev + '\r\n')
f.close()
#


########################## QUARTERLY #######################
######################
xDF_OLS_Q = xDF_M.copy()
####################
xNoRolling_Q = True  #True
if (xNoRolling_Q):
    xDF_OLS_Q = xDF_OLS_Q.loc[xDF_OLS_Q['diff_Q'].isin({-1,3})]
    xDF_OLS_Q = xDF_OLS_Q.loc[xDF_OLS_Q['diff_Q'].notnull()]
###################
xDF_OLS_Q.dropna(inplace=True)
xDF_OLS_Q.reset_index(drop=True,inplace=True)
######################
xStartDate_Q = xDF_OLS_Q['DATE'].min()
xEndDate_Q = xDF_OLS_Q['DATE'].max()
#################### model portfolios for Quarterly returns ############
xMP_Q = xDF_OLS_Q[['DATE']].copy()
xMP_Q = pd.merge(xMP_Q, xMP_MQ[['DATE','CONS_pct_ch_Q','MODCONS_pct_ch_Q','MOD_pct_ch_Q','MODGROW_pct_ch_Q','GROW_pct_ch_Q',
                'MAXGROW_pct_ch_Q','Current_pct_ch_Q','New_pct_ch_Q']], on=['DATE'], how='left')
xMP_Q_CumRtn = (1+xMP_Q[['CONS_pct_ch_Q','MODCONS_pct_ch_Q','MOD_pct_ch_Q','MODGROW_pct_ch_Q','GROW_pct_ch_Q',
                         'MAXGROW_pct_ch_Q','Current_pct_ch_Q','New_pct_ch_Q']]).cumprod()
xMP_Q_AnnRtn = (xMP_Q_CumRtn.iloc[len(xMP_Q_CumRtn)-1]/xMP_Q_CumRtn.iloc[0])**(1/(len(xMP_Q_CumRtn)/4))-1

xMP_Q_AnnRtn = xMP_Q_AnnRtn.reset_index()
xMP_Q_AnnRisk = xMP_Q[['CONS_pct_ch_Q','MODCONS_pct_ch_Q','MOD_pct_ch_Q','MODGROW_pct_ch_Q','GROW_pct_ch_Q',
                       'MAXGROW_pct_ch_Q','Current_pct_ch_Q','New_pct_ch_Q']].std().reset_index()
xMP_Q_AnnRtn.rename(columns={0: 'AnnRtn'},inplace=True)
xMP_Q_AnnRisk.rename(columns={0: 'AnnRisk'},inplace=True)
xMP_Q_AnnRisk['AnnRisk']=xMP_Q_AnnRisk['AnnRisk']*np.sqrt(4)

xMP_Q_AnnRtnRisk = pd.merge(xMP_Q_AnnRtn,xMP_Q_AnnRisk,on=['index'],how='left')
####################

Y = xDF_OLS_Q[xY_col + '_pct_ch_Q']
xInd_Vars = ['SPXT_pct_ch_Q','RealBondTR_pct_ch_Q','TIPS_pct_ch_Q','CPI_pct_ch_Y','CCY_pct_ch_Q','COMM_pct_ch_Q','USCredit_pct_ch_Q','HYTR_pct_ch_Q']
#xInd_Vars = ['SPXT_pct_ch_Q','TIPS_pct_ch_Q','CPI_pct_ch_Y','CCY_pct_ch_Q','COMM_pct_ch_Q','USCredit_pct_ch_Q','HYTR_pct_ch_Q']
xInd_Vars = ['SPXT_pct_ch_Q','BondTR_pct_ch_Q']
X = xDF_OLS_Q[xInd_Vars]

xCorrelations_Q = xDF_OLS_Q[[xY_col + '_pct_ch_Q']+xInd_Vars].corr().to_string()
f = open(xDir + 'xCorrelations_Q_' + xY_col + '.txt','w')
f.write(xCorrelations_Q + '\r\n')
f.close()

X = sm.add_constant(X)
model = sm.OLS(Y,X)
result = model.fit()
xOLS_Summary_Q = result.summary()
xOLS_text = xOLS_Summary_Q.as_text()

f = open(xDir + 'xOLS_Q_' + xY_col + '.txt','w')
f.write(xOLS_text + '\r\n')
f.close()

########## calc annualized return from Monthly returns ##########
xCumRtn_Y = (1+Y).cumprod()
xAnnRtn_Y_Q = (xCumRtn_Y[len(xCumRtn_Y)-1]/xCumRtn_Y[0])**(1/(len(xCumRtn_Y)/4))-1
xAnnRisk_Y_Q = np.sqrt(4*Y.var())
#xMP_Q_AnnRtnRisk=xMP_Q_AnnRtnRisk.append({'index':'Current Portfolio','AnnRtn':xAnnRtn_Y_Q,'AnnRisk':xAnnRisk_Y_Q}, ignore_index=True)
############################################

xVar_X = np.array(X.var())
xVar_Y = Y.var()
xCoef_sq = result.params**2
xVar_resid = result.resid.var()
xVar_CoefX = xCoef_sq * xVar_X
xDelta_var = xVar_Y - np.sum(xVar_CoefX) - xVar_resid
xDelta_varX = xDelta_var * xVar_CoefX / np.sum(xVar_CoefX)
xVar_X_adj = xVar_CoefX + xDelta_varX
xVar_X_adj_pct = xVar_X_adj / xVar_Y
xVar_resid_pct = xVar_resid / xVar_Y
print (xVar_X_adj_pct, xVar_resid_pct)
print(np.sum(xVar_X_adj_pct)+xVar_resid_pct)

xVar_X_adj_pct = pd.DataFrame(xVar_X_adj_pct)
xVar_X_adj_pct.reset_index(inplace=True)

xVar_X_adj_pct.rename(columns={0: 'Risk_Exposure(%)'},inplace=True)
xVar_X_adj_pct.rename(columns={'index': 'Risk_Factor'},inplace=True)
xVar_X_adj_pct=xVar_X_adj_pct.append({'Risk_Factor':'Idiosyncratic', 'Risk_Exposure(%)': xVar_resid_pct}, ignore_index=True)

xVar_X_adj_pct=xVar_X_adj_pct.loc[~xVar_X_adj_pct['Risk_Factor'].isin({'const'})]
xSum = xVar_X_adj_pct['Risk_Exposure(%)'].sum()
xVar_X_adj_pct=xVar_X_adj_pct.append({'Risk_Factor':'Sum', 'Risk_Exposure(%)': xSum}, ignore_index=True)
xVar_X_adj_pct=xVar_X_adj_pct.append({'Risk_Factor':model.endog_names+'(Annual StDev)', 'Risk_Exposure(%)': xAnnRisk_Y_Q}, ignore_index=True)
xVar_X_adj_pct=xVar_X_adj_pct.append({'Risk_Factor':model.endog_names+'(Annual Rtn)', 'Risk_Exposure(%)': xAnnRtn_Y_Q}, ignore_index=True)

xVar_X_adj_pct['Risk_Exposure(%)'] = xVar_X_adj_pct['Risk_Exposure(%)'].astype(float).map("{:.2%}".format)
# for x in (result.tvalues.index):
#     if x=='const':
#         continue
#     else:
#         #print (x, result.tvalues[x])
#         if (abs(result.tvalues[x]) <1.5):
#             xVar_X_adj_pct[xVar_X_adj_pct['Risk_Factor'] == x]['Risk_Exposure(%)'] = 'NA'
#             #print (x, xVar_X_adj_pct[xVar_X_adj_pct['Risk_Factor']==x]['Risk_Exposure(%)'])

xRisk_Exposure_Q = xVar_X_adj_pct.to_string()
#xRisk_Exposure_M.to_csv (xDir + 'xRisk_Exposure_M.txt')

f = open(xDir + 'xRisk_Exposure_Q_' + xY_col + '.txt','w')
f.write(xRisk_Exposure_Q + '\r\n')
f.close()

#### Scatter plots for Current Portfolio vs 6 Model Portfolios (Using Daily, Monthly, Qquarterly and Annual Rtns #####
import matplotlib.pyplot as plt

xFreq = ''
for k in range(0,4):
    if k==0:
        xRtn_Risk_Name = 'xMP_D_AnnRtnRisk'
        xFreq = '(using daily data)'
        xStartDate = xStartDate_D
        xEndDate = xEndDate_D

    elif k == 1:
        xRtn_Risk_Name = 'xMP_M_AnnRtnRisk'
        xFreq = '(using monthly data)'
        xStartDate = xStartDate_M
        xEndDate = xEndDate_M
    elif k == 2:
        xRtn_Risk_Name = 'xMP_Q_AnnRtnRisk'
        xFreq = '(using quarterly data)'
        xStartDate = xStartDate_Q
        xEndDate = xEndDate_Q
    elif k == 3:
        xRtn_Risk_Name = 'xMP_Y_AnnRtnRisk'
        xFreq = '(using annual data)'
        xStartDate = xStartDate_Y
        xEndDate = xEndDate_Y

    xMP_Rtn_Risk=globals()[xRtn_Risk_Name].copy()
    #xMP_Rtn_Risk=xMP_M_AnnRtnRisk.copy()

    xMP_name = pd.DataFrame()
    xMP_name['name']=''
    xMP_name['Rtn_Risk']=''
    xRtn= xMP_Rtn_Risk['AnnRtn'][0]
    xRisk= xMP_Rtn_Risk['AnnRisk'][0]
    xRtn_Risk = '('+f'{round(xRtn*100,1)}%' + ','+f'{round(xRisk*100,1)}%'+','+f'{round(xRtn/xRisk,2)}'+')'
    xMP_name = xMP_name.append({'name':'Conservative','Rtn_Risk': xRtn_Risk}, ignore_index=True)
    xRtn= xMP_Rtn_Risk['AnnRtn'][1]
    xRisk= xMP_Rtn_Risk['AnnRisk'][1]
    xRtn_Risk = '('+f'{round(xRtn*100,1)}%' + ','+f'{round(xRisk*100,1)}%'+','+f'{round(xRtn/xRisk,2)}'+')'
    xMP_name = xMP_name.append({'name':'Moderate Conservative','Rtn_Risk': xRtn_Risk}, ignore_index=True)
    xRtn= xMP_Rtn_Risk['AnnRtn'][2]
    xRisk= xMP_Rtn_Risk['AnnRisk'][2]
    xRtn_Risk = '('+f'{round(xRtn*100,1)}%' + ','+f'{round(xRisk*100,1)}%'+','+f'{round(xRtn/xRisk,2)}'+')'
    xMP_name = xMP_name.append({'name':'Moderate','Rtn_Risk': xRtn_Risk}, ignore_index=True)
    xRtn= xMP_Rtn_Risk['AnnRtn'][3]
    xRisk= xMP_Rtn_Risk['AnnRisk'][3]
    xRtn_Risk = '('+f'{round(xRtn*100,1)}%' + ','+f'{round(xRisk*100,1)}%'+','+f'{round(xRtn/xRisk,2)}'+')'
    xMP_name = xMP_name.append({'name':'Moderate Growth','Rtn_Risk': xRtn_Risk}, ignore_index=True)
    xRtn= xMP_Rtn_Risk['AnnRtn'][4]
    xRisk= xMP_Rtn_Risk['AnnRisk'][4]
    xRtn_Risk = '('+f'{round(xRtn*100,1)}%' + ','+f'{round(xRisk*100,1)}%'+','+f'{round(xRtn/xRisk,2)}'+')'
    xMP_name = xMP_name.append({'name':'Growth','Rtn_Risk': xRtn_Risk}, ignore_index=True)
    xRtn= xMP_Rtn_Risk['AnnRtn'][5]
    xRisk= xMP_Rtn_Risk['AnnRisk'][5]
    xRtn_Risk = '('+f'{round(xRtn*100,1)}%' + ','+f'{round(xRisk*100,1)}%'+','+f'{round(xRtn/xRisk,2)}'+')'
    xMP_name = xMP_name.append({'name':'Maximum Growth','Rtn_Risk': xRtn_Risk}, ignore_index=True)
    xRtn= xMP_Rtn_Risk['AnnRtn'][6]
    xRisk= xMP_Rtn_Risk['AnnRisk'][6]
    xRtn_Risk = '('+f'{round(xRtn*100,1)}%' + ','+f'{round(xRisk*100,1)}%'+','+f'{round(xRtn/xRisk,2)}'+')'
    xMP_name = xMP_name.append({'name':'Current Portfoio','Rtn_Risk': xRtn_Risk}, ignore_index=True)
    xRtn= xMP_Rtn_Risk['AnnRtn'][7]
    xRisk= xMP_Rtn_Risk['AnnRisk'][7]
    xRtn_Risk = '('+f'{round(xRtn*100,1)}%' + ','+f'{round(xRisk*100,1)}%'+','+f'{round(xRtn/xRisk,2)}'+')'
    xMP_name = xMP_name.append({'name':'New Portfoio','Rtn_Risk': xRtn_Risk}, ignore_index=True)
    #######
    xMP_Rtn_Risk['Lable']=''
    xMP_Rtn_Risk['Rtn_Risk']=''
    i=0
    for x in xMP_name['name']:
        xMP_Rtn_Risk['Lable'][i]=xMP_name['name'][i]
        xMP_Rtn_Risk['Rtn_Risk'][i]=xMP_name['Rtn_Risk'][i]
        i=i+1
    ##############
    x = xMP_Rtn_Risk['AnnRisk'].values
    y = xMP_Rtn_Risk['AnnRtn'].values
    #types = xMP_Rtn_Risk.reset_index()['index'].values
    #types = xMP_Rtn_Risk['index'].values
    types = xMP_Rtn_Risk['Lable'].values

    fig, ax = plt.subplots()
    #ax.plot(risks, returns, color='red', label='Equity/Bond')      # this is a line (efficient frontier)
    xSubText = xFreq + ' from ' + xStartDate.strftime('%m/%d/%Y') + ' to ' + xEndDate.strftime('%m/%d/%Y')
    fig.suptitle('Return and Risk of the Current Portfolio (' + xY_col+') vs Model Portfolios \n' + xSubText, fontsize=13,y=0.98)
    #ax.set_xlabel('Risk (Annualized Std)', fontsize=10)
    #ax.set_ylabel('Annualized Return', fontsize=10)

    #fig, ax = plt.subplots(figsize=(10,10))
    ax.scatter(x, y)

    ax.set_xlabel('Annualized Risk', fontsize=12)
    ax.set_ylabel('Annualized Return', fontsize=12)
    #ax.set_title('(Return and Risk) of the Current Portfolio vs Model Portfolios ' + xSubText, fontsize=18)

    for i, txt in enumerate(types):
        ax.annotate(txt + '\n' + xMP_Rtn_Risk['Rtn_Risk'][i], (x[i], y[i]), xytext=(-18,-18), textcoords='offset points',ha="left", size=8)
        #ax.annotate(txt + '\n', (x[i], y[i]), xytext=(10, 10), textcoords='offset points')
        plt.scatter(x, y, marker='o', color='blue')

    plt.savefig(xDir + xRtn_Risk_Name +'_'+xY_col+'.png')
    plt.show()

################## SI and SPXT and BondTR: Rolling Annual Returns and Calendar Monthly Returns ###########
xSI_Y = xDF[['DATE','SPLPEQTY_pct_ch_Y','SI2_pct_ch_Y','SI4_pct_ch_Y','SI6_pct_ch_Y','SPXT_pct_ch_Y','BondTR_pct_ch_Y']].copy()
xSI_Y.dropna(inplace=True)
xSI_Y.reset_index(drop=True,inplace=True)
xStartDate_Y_SI= xSI_Y['DATE'].min()
xEndDate_Y_SI= xSI_Y['DATE'].max()

xSI_Y_AnnStdDev=pd.DataFrame(xSI_Y.std())
xSI_Y_AnnStdDev.reset_index(inplace=True)
xSI_Y_AnnStdDev.rename(columns={0: 'AnnStdDev(%)'},inplace=True)
xSI_Y_AnnRtn=pd.DataFrame(xSI_Y.mean())
xSI_Y_AnnRtn.reset_index(inplace=True)
xSI_Y_AnnRtn.rename(columns={0: 'AnnRtn(%)'},inplace=True)
xSI_Y_RtnRisk = pd.merge(xSI_Y_AnnRtn,xSI_Y_AnnStdDev,on=['index'],how='left')
xSI_Y_RtnRisk['Sharpe Ratio (Rtn/Risk)'] = xSI_Y_RtnRisk['AnnRtn(%)'] / xSI_Y_RtnRisk['AnnStdDev(%)']

xSI_Y_RtnRisk['AnnRtn(%)'] = xSI_Y_RtnRisk['AnnRtn(%)'].astype(float).map("{:.2%}".format)
xSI_Y_RtnRisk['AnnStdDev(%)'] = xSI_Y_RtnRisk['AnnStdDev(%)'].astype(float).map("{:.2%}".format)
xSI_Y_RtnRisk['Sharpe Ratio (Rtn/Risk)'] = xSI_Y_RtnRisk['Sharpe Ratio (Rtn/Risk)'].astype(float).map("{:.2f}".format)

xText_RtnRisk = xSI_Y_RtnRisk.to_string()
xText_corr = xSI_Y.corr().to_string()

f = open(xDir + 'xSI_Y_AnnRtnRisk_corr.txt','w')
f.write(xStartDate_Y_SI.strftime('%Y/%m/%d') + ' to ' + xEndDate_Y_SI.strftime('%Y/%m/%d') + '\n\n'
        + xText_RtnRisk + '\n\n' + xText_corr)
f.close()
##############################
xSI_M = xDF_M[['DATE','SPLPEQTY_pct_ch_M','HFRIEMNI_pct_ch_M','SI2_pct_ch_M','SI4_pct_ch_M','SI6_pct_ch_M','SPXT_pct_ch_M','BondTR_pct_ch_M']].copy()
xSI_M.dropna(inplace=True)
xSI_M.reset_index(drop=True,inplace=True)
xStartDate_M_SI= xSI_M['DATE'].min()
xEndDate_M_SI= xSI_M['DATE'].max()

xSI_M_AnnStdDev=pd.DataFrame(xSI_M.std())*np.sqrt(12)
xSI_M_AnnStdDev.reset_index(inplace=True)
xSI_M_AnnStdDev.rename(columns={0: 'AnnStdDev(%)'},inplace=True)

#########
# xSI_M_AnnRtn=pd.DataFrame(xSI_M.mean())*12
# xSI_M_AnnRtn.reset_index(inplace=True)
# xSI_M_AnnRtn.rename(columns={0: 'AnnRtn(%)'},inplace=True)
##########
########## calc annualized return from Monthly returns ##########
#xCumRtn_Y = (1 + Y).cumprod()
xCumRtn_Y = (1 + xSI_M[['SPLPEQTY_pct_ch_M','HFRIEMNI_pct_ch_M','SI2_pct_ch_M','SI4_pct_ch_M','SI6_pct_ch_M','SPXT_pct_ch_M','BondTR_pct_ch_M']]).cumprod()
xSI_M_AnnRtn = (xCumRtn_Y.iloc[len(xCumRtn_Y) - 1] / xCumRtn_Y.iloc[0]) ** (1 / (len(xCumRtn_Y) / 12)) - 1
xSI_M_AnnRtn=pd.DataFrame(xSI_M_AnnRtn)
xSI_M_AnnRtn.reset_index(inplace=True)
xSI_M_AnnRtn.rename(columns={0: 'AnnRtn(%)'},inplace=True)
############################################
xSI_M_RtnRisk = pd.merge(xSI_M_AnnRtn,xSI_M_AnnStdDev,on=['index'],how='left')
xSI_M_RtnRisk['Sharpe Ratio (Rtn/Risk)'] = xSI_M_RtnRisk['AnnRtn(%)'] / xSI_M_RtnRisk['AnnStdDev(%)']

xSI_M_RtnRisk['AnnRtn(%)'] = xSI_M_RtnRisk['AnnRtn(%)'].astype(float).map("{:.2%}".format)
xSI_M_RtnRisk['AnnStdDev(%)'] = xSI_M_RtnRisk['AnnStdDev(%)'].astype(float).map("{:.2%}".format)
xSI_M_RtnRisk['Sharpe Ratio (Rtn/Risk)'] = xSI_M_RtnRisk['Sharpe Ratio (Rtn/Risk)'].astype(float).map("{:.2f}".format)

xText_RtnRisk = xSI_M_RtnRisk.to_string()
xText_corr = xSI_M.corr().to_string()

f = open(xDir + 'xSI_M_AnnRtnRisk_corr.txt','w')
f.write(xStartDate_M_SI.strftime('%Y/%m/%d') + ' to ' + xEndDate_M_SI.strftime('%Y/%m/%d') + '\n\n'
        + xText_RtnRisk + '\n\n' + xText_corr)
f.close()
