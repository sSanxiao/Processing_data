import pandas as pd

# Read the json file and convert it to a dictionary
json_data = pd.read_json("./output.json", typ='series')
json_dict = json_data.to_dict()

# Read the tsv file in chunks
df_chunk = pd.read_csv("./.htseq_fpkm.tsv", sep='\t', chunksize=1000)
df_chunk_list = []

# Process each chunk
for i, chunk in enumerate(df_chunk):
    # Split the 'Ensembl_ID' column by '.' and keep only the first part
    chunk['Ensembl_ID'] = chunk['Ensembl_ID'].apply(lambda x: x.split(".")[0])
    
    # Replace the value in 'Ensembl_ID' column with the corresponding value in the json_dict
    for index, row in chunk.iterrows():
        try:
            chunk.loc[index, 'Ensembl_ID'] = json_dict[row['Ensembl_ID']]
        except:
            # If the value is not found in the json_dict, drop the row
            chunk.drop(index=[index], inplace=True)
    
    # Append the processed chunk to the list
    df_chunk_list.append(chunk)

# Concatenate all the chunks into a single DataFrame
result_Df = pd.concat(df_chunk_list)

# Save the result to a tsv file
result_Df.to_csv("./result.tsv", sep='\t', index=False)
