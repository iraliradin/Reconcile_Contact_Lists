import pandas as pd
import difflib

def find_most_similar_name(name, list2):
    similarity_scores = [difflib.SequenceMatcher(None, name, name2).ratio() for name2 in list2]
    max_similarity = max(similarity_scores)
    most_similar_index = similarity_scores.index(max_similarity)
    return list2[most_similar_index], max_similarity

def compare_lists(list1_file, list2_file):
    # Read the CSV files into pandas DataFrames
    df1 = pd.read_csv(list1_file)
    df2 = pd.read_csv(list2_file)

    # Create the additional columns in list 1
    df1['list_2'] = ''
    df1['resemblance'] = 0.0

    # Iterate over the names in list 1
    for idx, row in df1.iterrows():
        name1 = row['name']
        most_similar_name, resemblance = find_most_similar_name(name1, df2['name'])
        df1.at[idx, 'list_2'] = most_similar_name
        df1.at[idx, 'resemblance'] = resemblance

    # Save the updated DataFrame to a new CSV file
    df1.to_csv('output.csv', index=False)

# Replace 'list1.csv' and 'list2.csv' with your actual input filenames
compare_lists('list1.csv', 'list2.csv')
