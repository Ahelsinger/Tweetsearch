import pandas as pd
df = pd.read_csv('url_of_csv_file')
mysearchstring = "searchterm"
for index, row in df.iterrows():
    if mysearchstring in row[u'text']:
        print row[u'created_at'], row[u'text']