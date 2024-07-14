import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
def load_dataset():
    dataset_path = 'datasets/train_FD001.txt'  # Update with your dataset path
    df = pd.read_csv(dataset_path, sep=' ', header=None)
    df.drop(df.columns[[26, 27]], axis=1, inplace=True)  # Drop columns with no variance
    return df

# Perform data analysis and generate reports
def generate_reports():
    df = load_dataset()

    # Example report: Distribution of operational settings
    plt.figure(figsize=(10, 6))
    sns.histplot(df.iloc[:, 0], bins=20, kde=True, color='blue')
    plt.title('Distribution of Operational Setting 1')
    plt.xlabel('Operational Setting 1')
    plt.ylabel('Count')
    plt.savefig('reports/operational_setting_1_distribution.png')
    plt.close()

    # Example report: RUL distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df.iloc[:, -1], bins=20, kde=True, color='green')
    plt.title('Distribution of Remaining Useful Life (RUL)')
    plt.xlabel('RUL')
    plt.ylabel('Count')
    plt.savefig('reports/rul_distribution.png')
    plt.close()

    # Save reports to a specific directory
    reports_dir = 'reports'
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    print("Reports generated successfully!")

if __name__ == "__main__":
    generate_reports()
