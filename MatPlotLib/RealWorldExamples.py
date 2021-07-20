import matplotlib.pyplot as plt
import pandas as pd
import os


def GasPricesAnalysis():
    df_gasPrices = pd.read_csv('../data/gas_prices.csv')

    #   Plotting USA, South Korea and Canada on Line Graph
    plt.title('Gas Prices Over Time (in USD)')
    plt.plot(df_gasPrices['Year'], df_gasPrices['USA'], 'b.-', label='United States')
    plt.plot(df_gasPrices['Year'], df_gasPrices['Canada'], 'r.-', label='Canada')
    plt.plot(df_gasPrices['Year'], df_gasPrices['South Korea'], label='South Korea')
    plt.plot(df_gasPrices['Year'], df_gasPrices['Australia'], label='Australia')
    plt.plot(df_gasPrices['Year'], df_gasPrices['UK'], label='UK')

    plt.xticks(df_gasPrices.Year[::3])
    plt.xlabel('Year')
    plt.ylabel('US Dollars')
    plt.legend()
    plt.show()

    # Plotting gas prices of every country on a bar graph 1996

    labels = [df_gasPrices.columns[1:]]
    values = df_gasPrices.loc[df_gasPrices['Year'] == '1996']
    plt.bar(labels, values)
    plt.show()


#   GasPricesAnalysis()

def FIFAAnalysis():
    df_FIFAData = pd.read_csv('../data/fifa_data.csv')

    # Histograms - Number of Players with above 90 overall in FIFA 18

    playersWithOver90Overall = df_FIFAData.loc[df_FIFAData['Overall'] > 90]
    plt.hist(playersWithOver90Overall['Overall'])
    plt.title('Histogram representation of players and their overalls')
    plt.xlabel('Overall')
    plt.ylabel('Number of players with the equivalent overall')
    plt.show()

    # Pie Chart - % of players using left foot and right foot in FIFA 18

    leftFoot = df_FIFAData.loc[df_FIFAData['Preferred Foot'] == 'Left'].count()[0]
    rightFoot = df_FIFAData.loc[df_FIFAData['Preferred Foot'] == 'Right'].count()[0]
    foot = ['Left', 'Right']
    colors = ['#03fcad', '#0345fc']
    plt.pie([leftFoot, rightFoot], labels=foot, colors=colors, autopct='%1.2f%%')
    plt.title('Preferred Foot of FIFA 18 Players')
    plt.show()

    # Pie Chart - % of players With Overall in FIFA 18

    playersWithOverAllGreaterThan85 = df_FIFAData.loc[df_FIFAData['Overall'] >= 85].count()[0]
    playersWithOverAllGreaterThan80LessThan90 = \
        df_FIFAData.loc[(df_FIFAData['Overall'] >= 80) & (df_FIFAData['Overall'] < 85)].count()[0]
    playersWithOverAllGreaterThan70LessThan80 = \
        df_FIFAData.loc[(df_FIFAData['Overall'] >= 70) & (df_FIFAData['Overall'] < 80)].count()[0]
    playersWithOverAllGreaterThan60LessThan70 = \
        df_FIFAData.loc[(df_FIFAData['Overall'] >= 60) & (df_FIFAData['Overall'] < 70)].count()[0]
    playersWithOverAllGreaterThan50LessThan60 = \
        df_FIFAData.loc[(df_FIFAData['Overall'] >= 50) & (df_FIFAData['Overall'] < 60)].count()[0]
    playersWithOverAllGreaterThan40LessThan50 = \
        df_FIFAData.loc[(df_FIFAData['Overall'] >= 40) & (df_FIFAData['Overall'] < 50)].count()[0]

    colors = ['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600', '#ffa600']
    labels = ['Overall Greater than 85', 'Overall between 80 and 90', 'Overall between 70 and 80',
              'Overall between 60 and 70',
              'Overall between 50 and 60', 'Overall between 40 and 50']
    plt.pie([playersWithOverAllGreaterThan85, playersWithOverAllGreaterThan80LessThan90,
             playersWithOverAllGreaterThan70LessThan80, playersWithOverAllGreaterThan60LessThan70,
             playersWithOverAllGreaterThan50LessThan60, playersWithOverAllGreaterThan40LessThan50],
            colors=colors, autopct='%1.2f%%', startangle=90, radius=0.9, pctdistance=0.9)

    plt.title("Percentage of players and their overalls")
    plt.legend(labels=labels, loc='best', bbox_to_anchor=(-0.1, 1.),
               fontsize=8)
    plt.show()

    # Youngest Players with highest potentials in FIFA 18

    playersWithHighestPotential = df_FIFAData.loc[(df_FIFAData['Age'] <= 22) & (df_FIFAData['Potential'] > 90)]
    plt.barh(playersWithHighestPotential['Name'], playersWithHighestPotential['Potential'])
    plt.show()

    # Highest rated player for major clubs in Europe

    clubs = ['FC Barcelona', 'Real Madrid', 'Atlético Madrid', 'Manchester United',
             'Manchester City', 'Chelsea', 'Arsenal', 'Tottenham Hotspur', 'Liverpool']

    for club in clubs:
        df_Club = df_FIFAData.loc[df_FIFAData['Club'] == club]
        topRatedPlayerOfTheClub = df_Club.sort_values(['Overall'], ascending=False).head(1)
        topRatedPlayerOfTheClub.to_csv('../data/TopPlayers.csv', mode='a')

    df = pd.read_csv('../data/TopPlayers.csv')
    df = df.loc[~df['Name'].str.contains("Name")]
    df = df.sort_values(['Overall'], ascending=True)
    plt.title('Top players from each team in Premier League and La Liga (FIFA 18)')
    plt.xlabel('Players')
    plt.ylabel('Overall in FIFA 18')
    df['Player And Club'] = df['Name'] + '('+df['Club']+')'
    plt.bar(df['Name'], df['Overall'], align='center')
    plt.show()
    os.remove("../data/TopPlayers.csv")


# FIFAAnalysis()

# def GeographyAnalysis():

