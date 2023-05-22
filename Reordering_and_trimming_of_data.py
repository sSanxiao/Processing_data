import pandas as pd
import csv
import numpy as np

# Set the file paths for the input and output files
tsv_path = './result.tsv'
tsv_save_path = r'./Mat.tsv'
xlsx_path = './CorrectDP.xlsx'
csv_save_path = './CorrectDP.csv'

# Define a function to read data from a TSV file
def read_from_tsv(tsv_path) -> list:
    reader_data = []
    with open(tsv_path, ) as csvfile:
        file_list = csv.reader(csvfile, delimiter='\t')
        for line in file_list:
            reader_data.append(line)
    return reader_data

# Define a function to write data to a TSV file
def write_to_tsv(tsv_path, data_frame):
    with open(tsv_path, 'w+', newline='') as f:
        tsv_w = csv.writer(f, delimiter='\t')
        tsv_w.writerows(np.array(data_frame).tolist())

# Read data from the input TSV and XLSX files
tsv = read_from_tsv(tsv_path)
xlsx = pd.read_excel(xlsx_path)

# Convert the data to NumPy arrays
tsv_np = np.array(tsv)
xlsx_np = xlsx.values

# Extract the TCGA data from the TSV and XLSX files
tsv_TCGA = tsv_np[0][1:]
xlsx_TCGA = xlsx_np[:, 0]

# Find the matching TCGA data in the TSV and XLSX files
tsv_TCGA_index_list = []
new_xlsx_TCGA = []
for tsv_TCGA_index, TCGA in enumerate(tsv_TCGA):
    xlsx_TCGA_indexs = np.argwhere(TCGA == xlsx_TCGA)
    if len(xlsx_TCGA_indexs) >= 1:
        xlsx_TCGA_index = xlsx_TCGA_indexs[0]
        new_xlsx_TCGA.append(xlsx_np[xlsx_TCGA_index])
        tsv_TCGA_index_list.append(tsv_TCGA_index)
new_tsv_TCGA = tsv_np[:, tsv_TCGA_index_list]

# Define a function to write data to a CSV file
def writeDataIntoCSV(csvPath, data):
    data = pd.DataFrame(data)
    data.to_csv(csvPath, index=None, header=None)

# Write the new TCGA data to the output CSV and TSV files
writeDataIntoCSV(csv_save_path, np.array(new_xlsx_TCGA)[:, 0, :])
write_to_tsv(tsv_save_path, new_tsv_TCGA)
