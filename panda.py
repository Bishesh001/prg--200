# import pandas as pd

# df = pd.DataFrame({
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [25, 30, 35, 40],
#     'Sex': ['Female', 'Male', 'Female', 'Male']
# })

# print(df) 

import pandas as pd
ages = pd.Series([22, 55, 35], name="Age")

print("Ages:")
print(ages)

print("\nAverage Age:", ages.mean())
print("Maximum Age:", ages.max())
print("Minimum Age:", ages.min())
