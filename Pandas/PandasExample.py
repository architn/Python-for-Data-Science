import pandas as pd
df = pd.read_csv('../data/pokemon_data.csv')


def PandasExample():

    print(df)

    # To view top 3 rows
    print("Top 3 rows: {}".format(df.head(3)))

    # To view bottom 3 rows
    print("Bottom 3 rows: {}".format(df.tail(3)))


# PandasExample()


def PandasReadingData():

    # Read Headers
    print("Print all headers {}".format(df.columns))

    # Read Columns
    print("Columns {}".format(df[['Name', 'Type 1']]))

    # Read Each Row
    print(df.iloc[1])
    print(df.iloc[1:4])

    # Read Specific Row
    print(df.iloc[2, 1])

    # Get Specific Record
    print(df.loc[df['Type 1'] == 'Fire'])


# PandasReadingData()

# Sorting

def SortingDataInPandas():

    # Sorting in Ascending Order as per name
    # print(df.sort_values(['Name'], ascending=True))

    # Combination Sort
    print(df.sort_values(['Name', 'Type 1'], ascending=[False, True]))


# SortingDataInPandas()

def ManipulatingDataInPandas():

    # Way 1: Slow but less room for mistake
    df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
    print(df.head(5))

    # Dropping a column
    df.drop(columns=['Total'])
    print(df.head(5))

    # Way 2: Faster but mistakes could be made
    df['Total'] = df.iloc[:, 4:10].sum(axis=1)
    print(df.head(5))

    # Reordering columns
    print(df[['Name', 'HP', 'Defense']])


# ManipulatingDataInPandas()

# Filtering Data

def FilteringDataInPandas():
    # Python uses operators for conditions not 'and' 'or'
    new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
    new_df = new_df.reset_index()
    print(new_df)

    # To filter some data out
    new_df1 = df.loc[~df['Name'].str.contains("Mega")]
    print(new_df1)
    # Create new csv
    new_df.to_csv('filtered.csv')


# FilteringDataInPandas()
