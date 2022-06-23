# Author: Christina Kampel
# FINAL VERSION -- Currently in Use on R.Pi (June 20, 2022)

import matplotlib.pyplot as plt
import pandas as pd

def get_data(filename: str):
    """
    Gather all data from the CSV file containing DHT11 and DHT20 temperature and humidity data. Sort data into lists.
    
    Arguments:
    - filename: (str) Name of CSV file containing DHT11 and DHT20 data

    Returns:
    - labels: (list of strings) List containing date, time information of the form "Date, Time"
    - dht11_temp: (list of floats) List containing DHT11 temperature data
    - dht11_humi: (list of floats) List containing DHT11 humidity data
    - dht20_temp: (list of floats) List containing DHT20 temperature data
    - dht20_humi: (list of floats) List containing DHT20 humidity data
    """
    
    # Set up all data as lists

    df = pd.read_csv(filename)

    datelabels = df.iloc[:,0]
    timelabels = df.iloc[:,1]


    # Get labels for the x-axis of the graphs; has the form "Date, Time"

    labels = []

    for i in range(len(datelabels)):
        labels.append(f"{datelabels[i]}, {timelabels[i]}")


    # Get lists for temperature data

    dht11_temp = pd.DataFrame(df.iloc[:,2])
    dht20_temp = pd.DataFrame(df.iloc[:,4])

    # Get lists for humidity data

    dht11_humi = pd.DataFrame(df.iloc[:,3])
    dht20_humi = pd.DataFrame(df.iloc[:,5])

    return labels, dht11_temp, dht11_humi, dht20_temp, dht20_humi

def line_graph_temp(filename: str):
    """
    Generates a PNG image of a Matplotlib graph for the DHT11 and DHT20 temperature data. Graph is a scatterplot with lines connecting discrete data points. Region between sets of data is shaded.
    
    Arguments:
    - filename: (str) Name of CSV file containing data

    Returns: None
    """


    # Get all date-time labels and temp, humi data

    labels, dht11_temp, dht11_humi, dht20_temp, dht20_humi = get_data(filename)

    # Convert DataFrames to List format

    dht11_temp_list = list(dht11_temp.iloc[:,0])
    dht11_humi_list = list(dht11_humi.iloc[:,0])
    dht20_temp_list = list(dht20_temp.iloc[:,0])
    dht20_humi_list = list(dht20_humi.iloc[:,0])
    
    # Create figure object

    fig1 = plt.figure()


    # Plot as a continuous line with dots at each data point

    plt.plot(labels, dht11_temp_list, '-o', label='DHT11 Sensor', color='dodgerblue')
    plt.plot(labels, dht20_temp_list, '-o', label='DHT20 Sensor', color='red')


    # Fill between the curves

    plt.fill_between(labels, dht11_temp_list, dht20_temp_list, color='thistle')


    # Set axis labels, title and legend

    plt.xlabel('Date, Time Recorded')
    plt.ylabel('Temperature (Degrees Celsius)')
    plt.title('Comparing Temperature Readings of Two Electronic Sensors')
    plt.legend()


    # Rotate text on x-axis

    plt.xticks(rotation = 90)


    # Save as PNG

    fig1.savefig('static/line_graph_temp.png', bbox_inches='tight')

def line_graph_humi(filename: str):
    """
    Generates a PNG image of a Matplotlib graph for the DHT11 and DHT20 humidity data. Graph is a scatterplot with lines connecting discrete data points. Region between sets of data is shaded.
    
    Arguments:
    - filename: (str) Name of CSV file containing data

    Returns: None
    """


    # Get all date-time labels and temp, humi data

    labels, dht11_temp, dht11_humi, dht20_temp, dht20_humi = get_data(filename)

    # Convert DataFrames to List format

    dht11_temp_list = list(dht11_temp.iloc[:,0])
    dht11_humi_list = list(dht11_humi.iloc[:,0])
    dht20_temp_list = list(dht20_temp.iloc[:,0])
    dht20_humi_list = list(dht20_humi.iloc[:,0])

    # Create figure object

    fig2 = plt.figure()


    # Plot as a continuous line with dots at each data point

    plt.plot(labels, dht11_humi_list, '-o', label='DHT11 Sensor', color='dodgerblue')
    plt.plot(labels, dht20_humi_list, '-o', label='DHT20 Sensor', color='red')


    # Fill between the curves

    plt.fill_between(labels, dht11_humi_list, dht20_humi_list, color='thistle')


    # Set axis labels, title and legend

    plt.xlabel('Date, Time Recorded')
    plt.ylabel('Relative Humidity (%)')
    plt.title('Comparing Relative Humidity Readings of Two Electronic Sensors')
    plt.legend()


    # Rotate text on x-axis

    plt.xticks(rotation = 90)


    # Save as PNG

    fig2.savefig('static/line_graph_humi.png', bbox_inches='tight')

def avg_percent_diff_temp(filename:str):
    """
    Finds the average percent difference between all DHT11 and DHT20 temperature data.
    
    Arguments:
    - filename: (str) Name of CSV file containing data

    Returns:
    - average: (float) Average percent difference between all DHT11 and DHT20 temperature data
    - avg_statement: (str) String containing statement about calculated average, for display purposes
    """

    # Get all date-time labels and temp, humi data

    labels, dht11_temp, dht11_humi, dht20_temp, dht20_humi = get_data(filename)
    

    # Calculate the percent difference between each data point

    rects = []

    for i in range(len(dht11_temp)):
        calc = (abs(float(dht11_temp.iloc[i,0]) - float(dht20_temp.iloc[i,0]))) / ((float(dht11_temp.iloc[i,0]) + float(dht20_temp.iloc[i,0])) / 2) * 100
        rects.append(calc)


    # Find average of all percent differences and round to 3 decimal places

    average = round((sum(rects) / len(rects)), 3)

    # Create an easy-to-print statement summarizing the result

    # avg_statement = f"Average Percent Difference Between DHT11 and DHT20 Sensors (Temperature): {average}%"

    return average

def avg_percent_diff_humi(filename:str):
    """
    Finds the average percent difference between all DHT11 and DHT20 humidity data.
    
    Arguments:
    - filename: (str) Name of CSV file containing data

    Returns:
    - average: (float) Average percent difference between all DHT11 and DHT20 humidity data
    - avg_statement: (str) String containing statement about calculated average, for display purposes
    """

    # Get all date-time labels and temp, humi data

    labels, dht11_temp, dht11_humi, dht20_temp, dht20_humi = get_data(filename)
    

    # Calculate the percent difference between each data point

    rects = []

    for i in range(len(dht11_humi)):
        calc = (abs(float(dht11_humi.iloc[i,0]) - float(dht20_humi.iloc[i,0]))) / ((float(dht11_humi.iloc[i,0]) + float(dht20_humi.iloc[i,0])) / 2) * 100
        rects.append(calc)


    # Find average of all percent differences and round to 3 decimal places

    average = round((sum(rects) / len(rects)), 3)
    
    # Create an easy-to-print statement summarizing the result

    # avg_statement = f"Average Percent Difference Between DHT11 and DHT20 Sensors (Temperature): {average}%"

    return average

filename = "DHT_data.csv"