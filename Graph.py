import pandas as pd
import matplotlib.pyplot as plt

def pie_chart():
    ''' 
    This function creates a pie chart that shows the average cost of undergraduate education by type of institution.

    Parameters:
    None

    Returns:
    None
    '''
    # Load the data
    data = pd.read_csv("nces330_20.csv")

    # Group the data by type of institution and calculate the average cost of undergraduate education
    type_grouped = data.groupby('Type').mean(numeric_only=True)
    # size of the pie chart
    plt.figure(figsize=(7,7))

    # Plot the pie chart
    plt.pie(type_grouped['Value'], labels=type_grouped.index, autopct='%1.1f%%')
    plt.axis('equal')
    plt.title('Average Cost of Undergraduate Education by Type of Institution')
    plt.show()


def bar_chart():
    ''' 
    This function creates a bar chart that shows the average cost of undergraduate education by state.

    Parameters:
    None

    Returns:
    None
    '''
    # Load the data
    data = pd.read_csv("nces330_20.csv")

    # Group the data by state and calculate the average cost of undergraduate education
    state_grouped = data.groupby('State').mean(numeric_only=True)

    # Plot the stacked bar chart
    # size of the bar chart
    plt.figure(figsize=(20,10))
    plt.bar(state_grouped.index, state_grouped['Value'], edgecolor='k')
    plt.xlabel('State')
    plt.ylabel('Average Cost of Undergraduate Education (in dollars)')
    plt.title('Average Cost of Undergraduate Education by State')
    plt.xticks(rotation=90)
    plt.show()

def lines_chart():
    ''' 
    This function creates a line chart that shows the trend of average cost of undergraduate education by state over time.
    
    Parameters:
    
    None
    '''
    # Load the data
    data = pd.read_csv("nces330_20.csv")

    # Group the data by state and year, and calculate the average cost of undergraduate education
    grouped = data.groupby(['State', 'Year']).mean(numeric_only=True)

    # Plot the line chart
    # size of the line chart
    plt.figure(figsize=(20,10))
    for state in grouped.index.levels[0]:
        plt.plot(grouped.loc[state].index, grouped.loc[state]['Value'], label=state)

    plt.xlabel('Year')
    plt.ylabel('Average Cost of Undergraduate Education (in dollars)')
    plt.title('Trend of Average Cost of Undergraduate Education by State over Time')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()

def main():
    lines_chart().__doc__
    bar_chart().__doc__
    pie_chart().__doc__

if __name__ == "__main__":
    main()
