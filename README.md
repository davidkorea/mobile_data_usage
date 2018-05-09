# mobile_data_usage
 
# 1. Summary

1. read_csv
```php
device_df = pd.read_csv('./mobile_data/user_device.csv')
usage_df = pd.read_csv('./mobile_data/user_usage.csv')
```

2. combine 2 colomns
```php
# transform 2 columns to str type
device_df['platform_version'] =  device_df['platform_version'].astype('str')

# combine and create a new column 'system'
device_df['system'] = device_df['platform'].str.cat( device_df['platform_version'], sep='_' )
```

3. merge 2 csv / dataframe
```php
merge_df = pd.merge(device_df, usage_df, how='inner', on='user_id')
```

4. groupby
```php
mean_usage = merge_df.groupby('system')['monthly_mb'].mean()
# high-low sorting, let new data return to the old data space without creating a new var/space
mean_usage.sort_values(ascending=False, inplace=True)
```

4. plot
```php
mean_usage.plot(kind='bar',rot=45)
plt.show()
```
