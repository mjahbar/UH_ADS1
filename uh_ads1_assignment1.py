#imports
import pandas as pd
import matplotlib.pyplot as plt



def temp_sing_multiple_linesPlot(data):
    # Group by year
    groupedByyear = data.groupby(data['date'].dt.year)
    result = groupedByyear[['mean_temperature', 'maximum_temperature','minimum_temperature']].mean()
    # Round the mean values to 2 decimal places
    result = result.round(2)


    # Plot the mean values for each year
    ax = result.plot(kind='line', figsize=(10, 6))

    #Plot these values as function of time.
    # the look and feel of the plot
    plt.style.use("fivethirtyeight")
 
    # Labelling the axes and setting
    # a title
    plt.xlabel("Year")
    plt.ylabel("Temperature ($^\circ$C)")
    plt.title("Temperature in Singapore")

    # Add a legend at the bottom of the plot
    ax.legend(['Mean','Max','Min'],loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=3)


    # Show the plot
    plt.show()
    #saving 
    plt.savefig('temp_sing_multiple_linesPlot.png')
    




def main():
    # reading data , data taken from https://beta.data.gov.sg/collections/1381/view

    dfOrg = pd.read_csv("HistoricalDailyWeatherRecords.csv")

    # Data cleaning removing all na if daily_rainfall_total has na or mean_temperature has na
    df_filtered_index=dfOrg[(dfOrg['daily_rainfall_total']=='na') | (dfOrg['mean_temperature']=='na')].index
    dfOrg.drop(df_filtered_index , inplace=True)

    # convert to date using pd.to_datetime
    dfOrg['date'] = pd.to_datetime(dfOrg['date'])
    dfOrg['mean_temperature'] = pd.to_numeric(dfOrg['mean_temperature'])
    dfOrg['maximum_temperature'] = pd.to_numeric(dfOrg['maximum_temperature'])
    dfOrg['minimum_temperature'] = pd.to_numeric(dfOrg['minimum_temperature'])
    dfOrg['mean_wind_speed'] = pd.to_numeric(dfOrg['mean_wind_speed'])
    dfOrg['max_wind_speed'] = pd.to_numeric(dfOrg['max_wind_speed'])
    dfOrg['daily_rainfall_total'] = pd.to_numeric(dfOrg['daily_rainfall_total'])
    
    #calling time_chart function
    temp_sing_multiple_linesPlot(dfOrg)

if __name__ == "__main__":
    main()
