
import pandas as pd 
from datetime import datetime, date 
  
# Creating a list of date of birth 
dob = {'DOB': ['13/05/1986', '12/12/2018', '23/04/2006']} 
  
# Creating dataframe 
df = pd.DataFrame(data = dob) 
  
# This function converts given date to age 
def age(born): 
    born = datetime.strptime(born, "%d/%m/%Y").date() 
    today = date.today() 
    return today.year - born.year - ((today.month,  
                                      today.day) < (born.month,  
                                                    born.day)) 
  
df['Age'] = df['DOB'].apply(age) 
  
print(df)


