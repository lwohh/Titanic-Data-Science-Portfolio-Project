# importing necessary packages and libraries
import pandas as pd

# importing my dataset
titanic = pd.read_csv('C:/Users/canyon.white/OneDrive - Convergint/Documents/GitHub/Titanic Data Science Portfolio Project/titanic_data.csv')
titanic.head()


# determining the # of passengers that were aboard the titanic
print(len(titanic))
# answer:
# there were 2208 passengers aboard the titanic


