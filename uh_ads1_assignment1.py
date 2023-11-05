# imports
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
 
    # Labelling the axes and setting title
    plt.xlabel("Year")
    plt.ylabel("Temperature ($^\circ$C)")
    plt.title("Temperature in Singapore")

    # Add a legend at the bottom of the plot
    ax.legend(['Mean','Max','Min'], loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=3)

    # Show the plot
    plt.show()
    # saving the plot to disk
    plt.savefig('TempSingaporeMultipleLinesPlot.png')


def rainfall_AvarageTemperature(data):
    # Group by Month
    groupedByMonth = data.groupby(data['date'].dt.month)
    resultByMonth = groupedByMonth[['mean_temperature', 'daily_rainfall_total']].mean()
    # Round the mean values to 2 decimal places
    resultByMonth = resultByMonth.round(2)
    resultByMonth.reset_index(inplace=True)
    resultByMonth = resultByMonth.rename(columns = {'date':'month'})


    # Define month names
    month_names = [
        'January', 'February', 'March', 'April',
        'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December'
        ]

    # Create a figure and a primary axis
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot the first dataset (daily_rainfall_total) on the primary axis
    ax1.bar(resultByMonth['month'], resultByMonth['daily_rainfall_total'], color='b', label='Daily Rainfall Total')
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Daily Rainfall Total (mm)', color='b')

    # Set the x-axis labels to month names
    ax1.set_xticks(resultByMonth['month'])
    ax1.set_xticklabels(month_names, rotation=45, ha='right')

    # Create a secondary axis sharing the same x-axis (twinx)
    ax2 = ax1.twinx()

    # Plot the second dataset (mean_temperature) on the secondary axis
    ax2.plot(resultByMonth['month'], resultByMonth['mean_temperature'], marker='o', linestyle='-', color='r', label='Mean Temperature')
    ax2.set_ylabel('Mean Temperature ($^\circ$C)', color='r')

    # Adding a legend for both axes
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    # Title for the entire plot
    plt.title('Rainfall with Avarage Temperature')

    # Show the combined plot
    plt.show()

    # saving the plot to disk
    plt.savefig('RainfallwithAvarageTemperature_Plot.png')


def distributionOfRainyDays(data):
    
    # Calculate Rainy and non Rainy days
    non_rainy_days = len(data[data['daily_rainfall_total']==0])
    rainy_days = len(data[data['daily_rainfall_total']>0])

    # Create a pie chart
    labels = ['Rainy Days', 'Non-Rainy Days']
    sizes = [rainy_days, non_rainy_days]
    colors = ['blue', 'lightgrey']
    # Explode the first slice (Rainy Days)
    explode = (0.1, 0)  

    # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')  

    plt.title('Distribution of Rainy Days')

    # Show the pie chart
    plt.show()

    # saving the plot to disk
    plt.savefig('distributionOfRainyDays.png')


def main():
    # reading data , data taken from https://beta.data.gov.sg/collections/1381/view

    dfOrg = pd.read_csv("HistoricalDailyWeatherRecords.csv")

    # Data cleaning removing all na if daily_rainfall_total has na or mean_temperature has na
    df_filtered_index=dfOrg[(dfOrg['daily_rainfall_total']=='na') | (dfOrg['mean_temperature']=='na')].index
    dfOrg.drop(df_filtered_index, inplace=True)

    # convert to date using pd.to_datetime
    dfOrg['date'] = pd.to_datetime(dfOrg['date'])
    dfOrg['mean_temperature'] = pd.to_numeric(dfOrg['mean_temperature'])
    dfOrg['maximum_temperature'] = pd.to_numeric(dfOrg['maximum_temperature'])
    dfOrg['minimum_temperature'] = pd.to_numeric(dfOrg['minimum_temperature'])
    dfOrg['mean_wind_speed'] = pd.to_numeric(dfOrg['mean_wind_speed'])
    dfOrg['max_wind_speed'] = pd.to_numeric(dfOrg['max_wind_speed'])
    dfOrg['daily_rainfall_total'] = pd.to_numeric(dfOrg['daily_rainfall_total'])

    # calling temp_sing_multiple_linesPlot function
    temp_sing_multiple_linesPlot(dfOrg)

    # calling rainfall_AvarageTemperature function
    rainfall_AvarageTemperature(dfOrg)
    
    # calling distributionOfRainyDays function
    distributionOfRainyDays(dfOrg)

if __name__ == "__main__":
    main()
