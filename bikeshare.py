import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    """
    For Asking  to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("which city would you like to explore (chicago, new york city, washington):")
    city=city.lower()
    while city not in ['chicago','new york city','washington']:
            city = input("invalid input ,please inter one of those cities (chicago, new york city, washington):")
            city=city.lower()
    filter_details=input("would you like to filter the data by month ,day ,both or not at all: ")
     #  get user input for month (all, january, february, ... , june)
    if filter_details="month":
        month=input("which month do you want filter (all, january, february, ... , june):")
        month=month.lower()
        while month not in ['all','january','february','march','april','june']:
           month = input("invalid input,please inter one of those ['all','january','february','march','april','june']:")
           month=month.lower()
        day=input("which day of week (all, monday, tuesday, ... sunday):")
        day=day.lower()
        while day not in ['all','monday','tuesday','wednesday','thuresday','friday','saturday','sunday']:
          day = input("invalid input,please inter one of day of week (all, monday, tuesday, ... sunday):")
          day=day.lower()
            #  get user input for day of week (all, monday, tuesday, ... sunday)
    elif filter_details="day":
        day=input("which day of week (all, monday, tuesday, ... sunday):")
        day=day.lower()
        while day not in ['all','monday','tuesday','wednesday','thuresday','friday','saturday','sunday']:
          day = input("invalid input,please inter one of day of week (all, monday, tuesday, ... sunday):")
          day=day.lower()
        month=input("which month do you want filter (all, january, february, ... , june):")
        month=month.lower()
        while month not in ['all','january','february','march','april','june']:
           month = input("invalid input,please inter one of those ['all','january','february','march','april','june']:")
           month=month.lower()
    elif filter_details="both":
        month=input("which month do you want filter from january to june:")
        month=month.lower()
        while month not in ['all','january','february','march','april','june']:
           month = input("invalid input,please inter one of those ['all','january','february','march','april','june']:")
           month=month.lower()
        day=input("which day of week (all, monday, tuesday, ... sunday):")
        day=day.lower()
        while day not in ['all','monday','tuesday','wednesday','thuresday','friday','saturday','sunday']:
          day = input("invalid input,please inter one of day of week (all, monday, tuesday, ... sunday):")
          day=day.lower()
     elif filter_details="not at all" or filter_details !="month" or "day" or "both":
        message=input("invalid input please choose which month and day to filter!")
        month=input("which month do you want filter (all, january, february, ... , june):")
        month=month.lower()
        while month not in ['all','january','february','march','april','june']:
           month = input("invalid input,please inter one of those ['all','january','february','march','april','june']:")
           month=month.lower()
        day=input("which day of week (all, monday, tuesday, ... sunday):")
        day=day.lower()
        while day not in ['all','monday','tuesday','wednesday','thuresday','friday','saturday','sunday']:
          day = input("invalid input,please inter one of day of week (all, monday, tuesday, ... sunday):")
          day=day.lower()

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
    df = pd.read_csv(CITY_DATA[city])
    return df


def time_stats(df ):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time']=pd.to_datetime(df['Start Time'])

    # display the most common month
    df['month']=df['Start Time'].dt.month

    if df['month'] != 'all':
        most_Common_month=df['month'].mode()[0]
    elif:
        print("no month is filter!")
        month=input("please inter in which month do you want to filter:")


    #  display the most common day of week
    df['day']=df['Start Time'].dt.weekday_name
    if df['day'] != 'all':
        most_Common_day=df['day'].mode()[0]
    elif:
        print("no day is filter!")
        day=input("please inter in which day do you want to filter:")
    #  display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    most_Common_starthour=df['hour'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return most_Common_month and most_Common_day and most_Common_hour











def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #  display most commonly used start station
    most_popular_start_station=pd.df['Start Station'].mode()[0]

    # display most commonly used end station
    most_popular_end_station=pd.df['End Station'].mode()[0]


    # display most frequent combination of start station and end station trip
    trip=pd.groupby(['most_popular_start_station,most_popular_end_station'])['df.Trip Duration']
    most_popular_trip= trip.mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return most_popular_start_station and most_popular_end_station and most_popular_trip









def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_trip_duration=pd.df['Trip Duration'].sum()

    # display mean travel time
    Average_trip_duration=pd.df['Trip Duration'].mean()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return total_trip_duration and Average_trip_duration











def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
     bikeshare_users = pd.df['User Type'].value_counts()

    #  Display counts of gender
     if city in ['chicago','New_York_City']:
            bikeshare_gender=pd.df['Gender'].value_counts()
 #Display earliest, most recent, and most common year of birth
            most_common_year=pd.df['Birth Year'].mode()[0]
            the_earliest_date=df['Birth Year'].min()
            the_recent_date=df['Birth Year'].max()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return bikeshare_users and the_earliest_date and the_recent_date and bikeshare_gender


def display_data(df):
    raw_data=df
    user_input_request=input("would you like to display more data,yes or no.")
    if user_input_request.lower()="yes":
       raw_data=df.head(5)

    elif:
        user_input_request.lower()
        break
    elif:
        user_input_request.lower() != "yes" or "no"
        break

    while user_input_request.lower()="yes":
        more=input("would you like to display more data,yes or no.")
        if more.lower()="yes":
       raw_data=df.head(5)

    elif:
        more.lower()="no"
        break
    elif:
        more.lower() != "yes" or "no"
        break

    return raw_data








def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
