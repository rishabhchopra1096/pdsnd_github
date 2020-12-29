import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_month(m):
    """
    Args: Takes in a variable string
    Returns: The month name provided by the user
    assigned to the variable string
    """
    while m not in  ['january', 'february', 'march', 'april', 'may', 'june']:
        m = input("\nWhich month? January, February, March, April, May or June?\n")
        m = m.lower()
    return m


def get_day(d):
    """
    Args: Takes in a variable string. 
    Returns: Returns the day name provided by the user
    assigned to the variable string.
    """
    while d not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', \
    'saturday', 'sunday']:
        d = input("\nWhich day? Eg: Monday, Tuesday, Wednesday, etc.\n")
        d = d.lower()
    return d
        
        
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # setting initial value to enter loop
    city = None 

    # Get user input for city (chicago, new york city, washington).
    while city not in CITY_DATA:
        city = input("\nWould you like to see data for Chicago, New York City or Washington? \n")
        city = city.lower()
        
    # setting default value for month and day filters. 
    # if the time_filter = 'none', these will remain unchanged.
    month = 'all'
    day = 'all'
    
    # set initial value of time_filter to None
    time_filter = None
    # Ask the user whether they want to filter by month, day , both or not at all.
    while time_filter not in ("month", "day", "both", "none"):
        time_filter = input("\nWould you like to filter the data by month, day, both of not at all? Type 'none' for no filter.\n")
        time_filter = time_filter.lower()
    
    if time_filter == 'month':
        month = get_month(month)
    elif time_filter == 'day':
        day = get_day(day)
    elif time_filter == 'both':
        month = get_month(month)
        day = get_day(day)
    # else, month and day will remain at default value. 

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to 
    # create a new column
    df['month'] = df['Start Time'].dt.month
    # from 1 to 6 (Jan to Jun)
    
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    # from 0 to 6 (Monday to Sunday)
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get 
        # the corresponding int 
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1 
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'all':
        # use the index of the days list to get the corresponding int
        days = ['monday', 'tuesday', 'wednesday', \
                  'thursday', 'friday', 'saturday', \
                 'sunday']
        day = days.index(day)
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]  
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # creating list of months and days to display 
    # time statistics
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days = ['monday', 'tuesday', 'wednesday', \
                  'thursday', 'friday', 'saturday', \
                 'sunday']
    
    # display the most common month
    print("In this data, \n")
    print("The most common month for travelling is:")
    
    # get the most common month using the .value_counts()
    month_mode = df['month'].value_counts().index[0]
    
    # get the count for the most common month 
    month_mode_count = df['month'].value_counts().iloc[0]
    
    # month_mode - 1 implies that months in df['month'] 
    # start from 1, not 0. 
    print(months[month_mode - 1].title(), "with a count of ", month_mode_count, ".\n")
    
    
    # display the most common day of week
    print("The most common day of week for travelling is: ")
    
    # get the most common day_of_week using .value_counts()
    day_of_week_mode = df['day_of_week'].value_counts().index[0]
    
    # get the count for most common day_of_week
    day_of_week_mode_count = df['day_of_week'].value_counts().iloc[0]
    
    # day_of_week start from 0 itself. 
    print(days[day_of_week_mode].title(), "with a count of", day_of_week_mode_count, ".\n")


    # display the most common start hour
    print("The most common hour for travelling is: ")
    # Getting the most common hour using .value_counts() 
    hour_mode = df["Start Time"].dt.hour.value_counts().index[0]
    # Getting the count of the most common hour using .value_counts()
    hour_mode_count = df["Start Time"].dt.hour.value_counts().iloc[0]
    print(str(hour_mode)+":00 hours with a count of", hour_mode_count ,".\n" )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most popular start station is: ")
    print(df["Start Station"].value_counts().index[0], "with a count of",\
    df["Start Station"].value_counts().iloc[0], "\n")

    # display most commonly used end station
    print("The most popular end station is: ")
    print(df["End Station"].value_counts().index[0], "with a count of",\
    df["End Station"].value_counts().iloc[0], "\n")

    # display most frequent combination of start station and end 
    # station trip

    # Make a dictionary with trips : counts as key-value pairs
    trips_count = {}
    for start, end in df[["Start Station", "End Station"]].values:
        if (start, end) in trips_count.keys():
            trips_count[(start, end)] += 1
        else:
            trips_count[(start, end)] = 1

    # Find the most common trip: 
    for trip in trips_count:
        # if the trip count of current trip is the max of all trip count
        if trips_count[trip] == max(trips_count.values()):
            trip_mode = trip
            # break the loop as soon as we get the most common trip.
            break 

    # print the most popular trip
    print("The most popular trip is: ")
    print("{} to {} with a count of {} trips".format(*trip_mode, \
        max(trips_count.values())))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time (ttt)
    ttt = df["Trip Duration"].sum()
    print("Total Travel Time:\n")
    print(ttt, "seconds or")
    print(ttt/3600, "hours or")
    print(ttt/(3600*24), "days.\n")

    # display mean travel time (mtt)
    mtt = df["Trip Duration"].mean()
    print("Mean Travel Time: \n")
    print(mtt, "seconds or")
    print(mtt/60, "minutes.\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Here is the breakdown of users: ")
    print(df["User Type"].value_counts())
    print()

    # Display counts of gender
    if "Gender" in df.columns:
        print("Here is the breakdown of gender: ")
        print(df["Gender"].value_counts())
        print()
    else:
        print("No Gender data to share.")

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        oldest = df["Birth Year"].min()
        youngest = df["Birth Year"].max()
        mean_age = df["Birth Year"].mean()
        print("The oldest passenger was born in: ", oldest, ".")
        print("The youngest passenger was born in: ", youngest, ".")
        print("The average passenger was born in: ", mean_age, ".")
    else:
        print("No Birth Year data to share.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def view_data(df, line_n): 
    """
    Asks the use if they want to see the individual data. 
    If user agrees, show 5 lines of data, and asks the 
    user if they want to be shown 5 more. 
    
    If user rejects, return. 
    """
    # set initial value of see_data to ''
    see_data = ''
    
    # ask the user if they want to see the data
    while see_data not in ('yes', 'no'):
        see_data = input("\nWould you like to view the trip data? Type 'yes' or 'no'.\n")
    see_data = see_data.lower()
    
    # If the user wants to see the data, show them 
    # the data starting from last line number.
    # Then, ask the user if they want to continue 
    # viewing the data. 
    if see_data == 'yes': 
        print(df.iloc[line_n:line_n+5])
        line_n += 5
        return view_data(df, line_n)
    # If the user does not want to see the data, 
    # return the function. 
    if see_data == 'no':
        return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        # show the time stats
        time_stats(df)
        # show the station stats
        station_stats(df)
        # show the trip_duration stats
        trip_duration_stats(df)
        # show the duration stats
        user_stats(df)
        # ask the use if they want to see the data 
        view_data(df,0)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()