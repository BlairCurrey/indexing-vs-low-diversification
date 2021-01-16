import pandas as pd
import datetime as dt

def log(f):
    def wrapper(df, *args, **kwargs):
        start = dt.datetime.now()
        result = f(df, *args, **kwargs)
        stop = dt.datetime.now()
        print(f'{f.__name__}:\n  runtime={stop - start}, end shape={result.shape}')
        return result
    return wrapper

@log
def startPipeline(df):
    return df.copy()

@log
def clean(df):
    df = df.drop(df[df['Dividends'] > 0.0].index)
    return df

@log
def trim(df):
    return df[["Close"]]

@log
def flatten_date(df):
    df = df.reset_index()
    # df = pd.pivot_table(df,index=['Symbol'],columns='Date',values='Close')
    # df.columns.name = ''
    # df.columns = ['Start Close','End Close']
    df = df.set_index(['Symbol', df.groupby('Symbol').cumcount()]).unstack()
    df.columns = [f'Start {c1}' if c2 == 0 else f'End {c1}' for c1, c2 in df.columns]
    return df

@log
def add_percent_change(df):
    df["Percent Change"] = ((df["End Close"] - df["Start Close"]) / df["Start Close"]) * 100
    return df

@log 
def removeOutliers(df):
    return df