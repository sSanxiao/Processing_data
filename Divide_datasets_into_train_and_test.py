import pandas as pd

# Read the input TSV file
mat = pd.read_csv('./Mat.tsv', sep='\t', index_col=0)

# Split the data into training and testing sets
mid_col = mat.shape[1] // 2
mat_train = mat.iloc[:, :mid_col]
mat_test = mat.iloc[:, mid_col:]

# Write the training and testing sets to TSV files
mat_train.to_csv('./mat_train.tsv', sep='\t')
mat_test.to_csv('./mat_test.tsv', sep='\t')

# Read the input CSV file
correct_dp = pd.read_csv('./CorrectDP.csv', index_col=0)

# Split the data into training and testing sets
mid_row = correct_dp.shape[0] // 2
correct_dp_train = correct_dp.iloc[:mid_row, :]
correct_dp_test = correct_dp.iloc[mid_row:, :]

# Select the columns that match the training and testing sets
correct_dp_train = correct_dp_train.loc[mat_train.columns]
correct_dp_test = correct_dp_test.loc[mat_test.columns]

# Write the training and testing sets to CSV files
correct_dp_train.to_csv('./CorrectDP_train.csv')
correct_dp_test.to_csv('./CorrectDP_test.csv')
