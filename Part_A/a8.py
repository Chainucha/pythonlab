# Write a Pandas program to join the two given data frames along rows. Sample Data
# frame may contain details of student like rollno, name , Total Marks.

import pandas as pd

# Sample DataFrames
data1 = {
    "RollNo": [101, 102, 103],
    "Name": ["Akira", "Rohith", "Arjun"],
    "TotalMarks": [85, 92, 78],
}
data2 = {
    "RollNo": [104, 105, 106],
    "Name": ["Sachin", "Pawan", "Varun"],
    "TotalMarks": [88, 91, 75],
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
# Concatenate the DataFrames along rows
combined_df = pd.concat([df1, df2], ignore_index=True)
# Display the combined DataFrame
print(combined_df)
