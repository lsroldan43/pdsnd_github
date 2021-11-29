import time
import pandas as pd
import numpy as np
import sys 
# Extract cities names form file's csv names
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
Cities= list(CITY_DATA.keys())
# Defining the filters to work with files.
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    aux= []
    i=0
    city = input("Enter the city (chicago, new york city, washington): ")
    city = str(city).lower()
    while aux!= city:
        aux=Cities[i]
        i += 1
        if i>=len(Cities)+1:
            city = input("Enter the valida city (chicago, new york city, washington): ").lower()
            i =0
            
    # TO DO: get user input for month (all, january, february, ... , june)
    Month=['january', 'february', 'march', 'april', 'may', 'june','All']
    aux= []
    i=0
    month= input("Enter a month ('january', 'february', 'march', 'april', 'may', 'june''all'): ")
    month=month.lower()
    while aux!= month:
        aux=Month[i]
        i += 1
        if i>len(Month)-1:
            month = input("Enter the valida month: ").lower()
            i =0
            
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    Day=['all', 'monday', 'tuesday','wednesday','thurday','friday','saturday','sunday']
    day= input("Enter a day :").lower()
    aux= []
    i=0
    
    while aux!= day:
        aux=Day[i]
        i += 1
        if i>len(Day)-1:
            day = input("Enter the valida day: ").lower()
            i =0

    print('-'*40)
    
    return city, month, day
    #city, month, day=get_filters()

# Function to load data
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
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] =pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    df.reset_index(inplace=True)
    df=df.drop(["index","Unnamed: 0"],axis=1)
    return df
#df=load_data(city, month, day)
# Function to statictics of time
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month= df['month'].mode()[0]

    # TO DO: display the most common day of week
    popular_day= df['day_of_week'].mode()[0]


    # TO DO: display the most common start hour
    popular_start_hour = df['Start Time'].mode()[0]


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Function stats
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    Total_Travel_Time = df['Trip Duration'].sum()

    # TO DO: display mean travel time

    Average_Travel_Time = df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print(user_types)
     # TO DO: Display counts of gender
     
    if city != "washington":
        # write code for Gender statistics
        Gender_statics= df['Gender'].describe()
        # TO DO: Display earliest, most recent, and most common year of birth
        Most_Recent_Birth= int(df['Birth Year'].min())
        Common_Birth= int(df['Birth Year'].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart== 'yes':
            break
        if restart== 'no':
            New_Lines=input('\nWould you like to displaying the first 5 lines of the data ? Enter yes or no.\n')
            j=0
            while New_Lines== 'yes':
                if j+5 <= len(df):
                    print(df.iloc[j:5+j,])
                    print("\nYou have seen", 5+j, " rows of", len(df),"rows" )
                    New_Lines=input('\nWould you like to displaying the next 5 lines of the data ? Enter yes or no.\n')
                    j+=5
                    if  j>=len(df):
                        print("\nThere is not more data to display" )
                        sys.exit()
                    elif New_Lines== 'no':
                        print("\nThe user do not want to see more data" )
                        sys.exit()

               
if __name__ == "__main__":
	main()
