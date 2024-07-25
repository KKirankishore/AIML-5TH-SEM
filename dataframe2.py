import pandas as pd

# Creating two series
name_grade = pd.Series({'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
                        'Grade': ['A', 'B', 'A', 'C', 'B']})

name_marks = pd.Series({'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
                        'Marks': [85, 78, 92, 65, 88]})

# Creating a dataframe from the two series
student_df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Grade': ['A', 'B', 'A', 'C', 'B'],
    'Marks': [85, 78, 92, 65, 88]
})

# Display the first three records from student dataframe
print("First three records:")
print(student_df.head(3))

# Display the last two records from student dataframe
print("\nLast two records:")
print(student_df.tail(2))
