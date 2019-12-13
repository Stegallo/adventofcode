import pandas
import inspect


def load_input():
    filename = inspect.getmodule(inspect.stack()[1][0]).__file__
    df = pandas.read_csv(f"input_{filename.replace('.py','')}.txt", header=None)
    if len(df.columns) > 1:
        df = df.T
    return df[0].values.tolist()
