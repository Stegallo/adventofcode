import pandas
import inspect


def basic_load():
    filename = inspect.getmodule(inspect.stack()[2][0]).__file__
    df = pandas.read_csv(f"input_{filename.replace('.py','')}.txt", header=None)
    if len(df.columns) > 1:
        df = df.T
    return df


def load_input():
    df = basic_load()
    return df[0].values.tolist()


def load_multi_input():
    df = basic_load()
    return df[0].values.tolist(), df[1].values.tolist()
