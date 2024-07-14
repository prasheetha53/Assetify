import pandas as pd

def load_dataset(dataset_path='datasets/train_FD001.txt'):
    df = pd.read_csv(dataset_path, sep=' ', header=None)
    df.drop(columns=[26, 27], inplace=True)  # Drop columns with no variance
    return df
