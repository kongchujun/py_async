
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range=(0, 1))

def filter_outlies(df, threshold, columns):
    df = df[(np.abs(stats.zscore(df[columns], nan_policy='omit')) < threshold).all(axis=1)]
    return df


if __name__=='__main__':
    df = pd.DataFrame({'column': [8,7,8,9,8,1,1,1,1,1,1,1,8,1,1,1,1,6,8,7,9,8]})
    print(df)
    df['a'] = df['column'] - df['column'].shift(1)
    df['b'] = df['column'] - df['column'].shift(-1)
    df['c'] = np.abs(df['a']) + np.abs(df['b'])
    df = df.drop(['a', 'b'], axis=1)
    df = df.replace(np.nan, 0)
    ormalized_data = scaler.fit_transform(df)
    print(ormalized_data)
    