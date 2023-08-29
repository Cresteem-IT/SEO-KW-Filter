import os
import pandas as pd


def combineCSV(paths, outputfile: str = None):
    if not outputfile:
        outputfile = input("enter output file name:\n")
    # Read and concatenate CSV files
    dfs = [pd.read_csv(file_path) for file_path in paths]
    combined_df = pd.concat(dfs, ignore_index=True)
    
    csvloc=f'outputs/csv/{outputfile}.csv'
    excelloc=f'outputs/excel/{outputfile}.xlsx'
    # Create the output directory if it doesn't exist
    os.makedirs(os.path.dirname(csvloc), exist_ok=True)
    os.makedirs(os.path.dirname(excelloc), exist_ok=True)

    # Save the combined DataFrame to a CSV file
    combined_df.to_csv(csvloc, index=False)
    combined_df.to_excel(excelloc, index=False)
    print("files are combined successfully")
    return (csvloc,excelloc)


def genFilePath(basedir: list, excludedir: list = None):

    if not excludedir:
        excludedir = []
        print('nothing excluded')

    csv_file_paths = []

    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(basedir):
        # Exclude specified folders
        dirs[:] = [d for d in dirs if d not in excludedir]

        for file in files:
            if file.endswith(".csv"):
                csv_file_paths.append(os.path.join(root, file))

    print(f"{len(csv_file_paths)} files are captured")
    return csv_file_paths


def filter(dataset, removelist: list):
    """ romove unwanted columns """
    return dataset.drop(columns=removelist, axis=1)


def filter_search_volume(file):
    min_search_volume = int(input("enter minimum search volume:\n"))
    output = input("output name:\n")
    dataset = pd.read_csv(file)

    # set na if there is -
    dataset['Search Volume'] = pd.to_numeric(
        dataset['Search Volume'], errors='coerce')
    # remove - or na data
    dataset.dropna(subset=['Search Volume'], inplace=True)

    filtered_dataframe = dataset[dataset['Search Volume'].astype(
        int) >= min_search_volume]
    ascended_df = filtered_dataframe.copy()
    ascended_df.sort_values(by='Search Volume', ascending=False, inplace=True)
    ascended_df.drop(columns=['No'], inplace=True)
    ascended_df.to_csv(f'outputs/csv/{output}.csv', index=False)
    ascended_df.to_excel(f'outputs/excel/{output}.xlsx', index=False)


def keywords_to_txt(file, filename: str = None):
    if not filename:
        filename = input("enter file name:\n")
    dataframe = pd.read_csv(file)
    num_keywords = int(input("How much keywords?\n"))
    if num_keywords > len(dataframe):
        num_keywords = len(dataframe)
    keywords = dataframe['Keyword'].tolist()[:num_keywords]
    with open(f'{filename}.txt', 'w') as file:
        file.write(','.join(keywords))

def add_priority(file,priority:int):
    df=pd.read_csv(file)
    df['priority'] = priority
    df.to_csv(file, index=False)
    df.to_excel(f'outputs/excel/{os.path.splitext(os.path.basename(file))[0]}.xlsx', index=False)
    print("added priority and saved")

#basedir = ""
#exdirs = ["competitor"]

# paths=genFilePath(basedir,exdirs)
# combineCSV(paths)

# file ='final.csv'
# filter_search_volume(file)

#finalfile = 'highvol.csv'
#keywords_to_txt(finalfile)
