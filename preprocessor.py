import pandas as pd

def preprocess(df,region_df):
    df = df[df['Season'] == 'Summer']
    df = df.merge(region_df, on='NOC', how='left')
    df.drop_duplicates(inplace=True)
    # Handling missing values in medals
    df_medal_encoded = pd.get_dummies(df['Medal'])
    df_medal_encoded = df_medal_encoded.astype(int)
    df = pd.concat([df, df_medal_encoded], axis=1)
    return df
