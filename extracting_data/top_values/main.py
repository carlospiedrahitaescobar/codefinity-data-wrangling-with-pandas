import pandas as pd

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/cars.csv', index_col = 0)

# To retrieve specific values of the column 'Year'
condition = data['Year'] > 2010
data_extracted = data.loc[condition]
data_cheapest = data_extracted.nsmallest(15,"Price",keep = "all")
print(data_cheapest)
# Print data
