import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from functools import reduce
from sklearn.model_selection import GridSearchCV

mat=pd.read_csv("MATIC-INR.csv", parse_dates=True).add_suffix("m")
usdt=pd.read_csv("USDT-INR (1).csv",parse_dates=True).add_suffix("u")
bit=pd.read_csv("BTC-INR (2).csv",parse_dates=True).add_suffix("b")
eth=pd.read_csv("ETH-INR (1).csv",parse_dates=True).add_suffix("e")
ada=pd.read_csv("ADA-INR (1).csv",parse_dates=True).add_suffix("a")
neo=pd.read_csv("NEO-INR.csv",parse_dates=True).add_suffix("n")
sol=pd.read_csv("SOL-INR.csv",parse_dates=True).add_suffix("s")
enj=pd.read_csv("ENJ-INR.csv",parse_dates=True).add_suffix("j")
dot=pd.read_csv("DOT-INR.csv",parse_dates=True).add_suffix("d")
axs=pd.read_csv("AXS-INR.csv",parse_dates=True).add_suffix("x")
eos=pd.read_csv("EOS-INR.csv",parse_dates=True).add_suffix("o")

mat["Date"]=pd.to_datetime(mat["Datem"])
usdt["Date"]=pd.to_datetime(usdt["Dateu"])
bit["Date"]=pd.to_datetime(bit["Dateb"])
eth["Date"]=pd.to_datetime(eth["Datee"])
ada["Date"]=pd.to_datetime(ada["Datea"])
neo["Date"]=pd.to_datetime(neo["Daten"])
sol["Date"]=pd.to_datetime(sol["Dates"])
enj["Date"]=pd.to_datetime(enj["Datej"])
dot["Date"]=pd.to_datetime(dot["Dated"])
axs["Date"]=pd.to_datetime(axs["Datex"])
eos["Date"]=pd.to_datetime(eos["Dateo"])


dfs=[mat,usdt,bit,eth,ada,neo,sol,enj,dot,axs,eos]
df_final=reduce(lambda left,right:pd.merge(left,right, on = "Date"),dfs)

df_comp=df_final[["Date","Closed","Closeu","Closeb","Closee","Closea","Closen","Closes","Closej","Closex","Closeo","Closem"]].rename(columns={"Closed":"dot_close","Closeu":"usdt_close","Closeb":"bit_close","Closee":"eth_close","Closea":"ada_close","Closen":"neo_close","Closes":"sol_close","Closej":"enj_close","Closex":"axs_close","Closeo":"eos_close","Closem":"mat_close","Closea":"ada_close"})

df_returns=pd.DataFrame()
df_returns["Date"]=df_comp["Date"]
df_logreturns=pd.DataFrame()
df_logreturns["Date"]=df_comp["Date"]

def calculated_returns(df,x):
    returns = x + str("ret")
    log_r = x + str("log_ret")
    df_returns[returns]= df[x].pct_change()
    df_logreturns[log_r]=np.log(df[x])-np.log(df[x].shift(1))
  
calculated_returns(df_comp,"dot_close")
calculated_returns(df_comp,"usdt_close")
calculated_returns(df_comp,"bit_close")
calculated_returns(df_comp,"eth_close")
calculated_returns(df_comp,"ada_close")
calculated_returns(df_comp,"mat_close")
calculated_returns(df_comp,"eos_close")
calculated_returns(df_comp,"enj_close")
calculated_returns(df_comp,"neo_close")
calculated_returns(df_comp,"axs_close")
calculated_returns(df_comp,"sol_close")

p_ret = [] # Define an empty array for portfolio returns
p_vol = [] # Define an empty array for portfolio volatility
p_weights = [] # Define an empty array for asset weights

num_assets = len(df_logreturns.columns)
num_portfolios = 100000

for portfolio in range(num_portfolios):
    weights = np.random.random(num_assets)
    weights = weights/np.sum(weights)
    p_weights.append(weights)
    returns = np.dot(weights, ind_er) # Returns are the product of individual expected returns of asset and its 
                                      # weights 
    p_ret.append(returns)
    var = covar.mul(weights, axis=0).mul(weights, axis=1).sum().sum()# Portfolio Variance
    sd = np.sqrt(var) # Daily standard deviation
    ann_sd = sd*np.sqrt(454) # Annual standard deviation = volatility
    p_vol.append(ann_sd)


portfolios.plot.scatter(x='Volatility', y='Returns', marker='o', s=10, alpha=0.3, grid=True, figsize=[10,10])



portfolios["High_sharpe"]=(portfolios.Returns/portfolios.Volatility)

prtu=portfolios[(portfolios["Volatility"]<.9)].sort_values("Volatility")
