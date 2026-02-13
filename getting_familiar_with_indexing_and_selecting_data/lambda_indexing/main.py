# Import the `pandas` library
import ___

# Read the csv file
data = ___.___('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/IMDb_Data_final.csv')

# Extract data with even indices
even = data.___[lambda ___: x.___ % 2 ___ 0 ]
# Extract data with odd indices
odd = ___[___: x.index % 2 ___ 0 ]

# Output data
___(even.___, ___)