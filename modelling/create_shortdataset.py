import pandas as pd
df = pd.read_csv('dataset.csv')

# Assuming 'class_label' is the column with your class labels
class_labels = df['label'].unique()

# Initialize an empty DataFrame to store sampled data
sampled_data = pd.DataFrame()

# Iterate over each class label and sample 10K rows
for label in class_labels:
    class_data = df[df['label'] == label].sample(n=20000, random_state=42)
    sampled_data = pd.concat([sampled_data, class_data])

# Reset index if needed
sampled_data.reset_index(drop=True, inplace=True)

# Now 'sampled_data' contains 10K elements for each class
sampled_data.to_csv('short20Dataset.csv', index=False)