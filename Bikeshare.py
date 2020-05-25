import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs





    while True:
        city = input('\nSelect from these cities to analyze; Chicago,New York City or Washington: ').lower()
        if city not in ('chicago,new york city,washington'):
            print('Incorrect input. Please try again')
            continue
        else:
            break



 # TO DO: get user input for month (all, january, february, ... , june)


    while True:
        month = input('\nSelect from these listed months to analyze; January,February,March,April,May,June,July,August,September,October,November,December \n').lower()

        if month not in ('january',
                     'february',
                     'march',
                     'april',
                     'may',
                     'june',
                     'july',
                     'august',
                     'september',
                     'october',
                    'november',
                     'december'):
            print('Incorrect input. Please try again')
            continue
        else:
            break


 # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    while True:
      day = input('\nSelect from the following days of the week Sunday, Monday, tuesday, wednesday, thursday, friday or saturday\n').lower()
      if day not in ('sunday',
                     'monday', 
                     'tuesday', 
                     'wednesday', 
                     'thursday', 
                     'friday',
                     'saturday',                              
                    ):
        print('Incorrect input. Please try again')
        continue
      else:
        break

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

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    most_com_month = df['month'].mode()[0]
    print('Most Common Month:', most_com_month)


    # TO DO: display the most common day of week

    most_com_day = df['day_of_week'].mode()[0]
    print('Most Common day:', most_com_day)



    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    most_com_hour = df['hour'].mode()[0]
    print('Most Common Hour:', most_com_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)


    # TO DO: display most commonly used end station

    most_end_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', most_end_Station)


    # TO DO: display most frequent combination of start station and end station trip

    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', Start_Station, " & ", most_end_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")


    # TO DO: display mean travel time

    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender

    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.\n")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.\n")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.\n")
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
     

def raw_data(df,row_no):
    
    while True:
        trip_detail = input('\nDo you want to see 5 lines of raw data displayed? Enter yes or no:\n ')
        count=df['Start Time'].count()
        if trip_detail.lower() == 'yes':
            if count <= row_no:
                
                break
            else:
                print(df.iloc[row_no:row_no+5])
                row_no += 5
        elif trip_detail.lower() == 'no':
            break
        else:
            print('\nThis input is not correct. Please try again.\n')
            return raw_data(df, line_no)

     
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        raw_data(df,0)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
