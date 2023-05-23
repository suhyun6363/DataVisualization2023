import seaborn as sns
import pandas as pd
titanic = sns.load_dataset("titanic")
print(titanic.info())
print(titanic.head())