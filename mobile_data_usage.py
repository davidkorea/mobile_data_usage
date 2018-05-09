import os
import pandas as pd
import matplotlib.pyplot as plt
from pd_utils import utils

user_device = './mobile_data/user_device.csv'
user_usage = './mobile_data/user_usage.csv'

def collect_data():
    device_df = pd.read_csv(user_device)
    usage_df = pd.read_csv(user_usage)
    return device_df,usage_df

def process_data(device_df,usage_df):
    # platform + model
    device_df['platform_version'] = device_df['platform_version'].astype('str')
    device_df['system'] = device_df['platform'].str.cat(device_df['platform_version'],sep='_')
    # print(device_df['system'])

    merge_df = pd.merge(device_df,usage_df,how='inner',on='user_id')
    return merge_df

def analyse_data(merge_df):
    mean_mb_by_system = merge_df.groupby('system')['monthly_mb'].mean()
    mean_mb_by_system.sort_values(ascending=False,inplace=True)
    # print(mean_mb_by_system.head()
    mean_mb_by_system.plot(kind='bar',rot=45)
    plt.ylabel('Monthly Usage (MB)')
    plt.title('Avr data usage by mobile system')
    plt.tight_layout()
    plt.show()

def main():
    device_df, usage_df = collect_data()
    # utils(device_df)
    # utils(usage_df)
    merge_df = process_data(device_df, usage_df)
    analyse_data(merge_df)


main()