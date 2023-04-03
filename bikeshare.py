import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # input enter city chicago, new york city, washington
    city = input('Enter the city: ')
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('Please, Enter the city is chicago, new york city and washington: ').lower()
    # input enter months from january to december
    month = input('Enter the month: ')
    while month not in ['all',"january","february","march","april","may","june","july","august","september","october","november","december"]:
        month = input('ENTER MONTH all, january, february, ... , december : ').lower()

    # input enter day 
    day = input('ENTER DAY : ').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    #load data from enter the city
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        months = ["january","february","march","april","may","june","july","august","september","october","november","december"]
        month = months.index(month) + 1
        df = df[df['month'] == month];
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # output display the most common month
    print('Month common is: ',df['month'].value_counts().idxmax())

    # output display the most common day of week
    print('Day of week common is: ',df['day_of_week'].value_counts().idxmax())

    # output display the most common start hour'
    df['hour'] = df['Start Time'].dt.hour
    print("Hour common is: ", df['hour'].value_counts().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # output display most commonly used start station
    print("Start station common is: ", df ['Start Station'].value_counts().idxmax())


    # output display most commonly used end station
    print("End station common is: ", df['End Station'].value_counts().idxmax())

    # output display most frequent combination of start station and end station trip
    start_and_end_stations = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print(start_and_end_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # output display total travel time
    total_travel_time = df['Trip Duration'].sum()/3600

    # output display mean travel time
    total_travel_time = df['Trip Duration'].mean() /3600

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # output Display counts of user types
    counts_user = df['User Type'].value_counts()
    print(counts_user)

    # output Display counts of gender
    counts_gender = df['Gender'].value_counts()
    print(counts_gender)

    # output Display earliest, most recent, and most common year of birth
    early_bd = int(df['Birth Year'].min())
    recent_bd = int(df['Birth Year'].max())
    most_common_bd = int(df['Birth Year'].value_counts().idxmax())
    
    print('Earliest year of birth: ',early_bd,', most recent year of brith: ',recent_bd,', most common year of birth: ',most_common_bd)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()