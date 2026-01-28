import pandas as pd

#Import data archive
#Use data .read_[Type]("Link")
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

df.head()