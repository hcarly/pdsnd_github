import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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

while True:
        city=str(input('Which city would you like to explore? (chicago, new york city or washington): '))

         print('Ooops...I don\'t understand that!. Please input a valid month')
         continue
       except:
         if city.lower() not in ('chicago', 'new york city','washington'):
            print('I am sorry, this is not a valid city, please try again')
         else:
            break

    while True:
        try:
           month=input('Which month would you like to choose? (all,january,february,... june:)')
        except:
            print('Ooops...I don\'t understand that!. Please input a valid month')
            continue
            if month.title() not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
                print('I am sorry, this is not a valid month, please try again')
            else:
                print('Perfect, let\'s continue')
        break
    while True:
       try:
           day= input('Which date would you like explore?(all, monday, tuesday, ... sunday):')
       except:
            print('Ooops...I don\'t understand that!. Please input a valid day')
            continue
            if day.title() not in ('All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
                print('I am sorry, this is not a valid day, please try again')
            else:
               print('Perfect, let\'s continue')
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
df = pd.read_csv(CITY_DATA[city])

# convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])

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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Frequent month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Frequent day of the week:', popular_day)

    # TO DO: display the most common start hour

    df['hour'] =df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Frequent Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Frequent End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['most_freq_trip']=df['Start Station']+ df['End Station']
    print('The most commmon combination of starting and ending station trip is\n {}'.format((df['most_freq_trip'].mode()[0])))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time was:{}'.format(total_travel_time))


    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('Average travel time was:{}'.format(average_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)


    # TO DO: Display counts of gender

    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('Genders: {}'.format(gender))
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        common_bd= int(df['Birth Year'].mode())
        print('The most common year of birth: {}'.format(common_bd))

        earliest_bd= int(df ['Birth Year'].min ())
        print ('The earliest year of birth: {}'. format(earliest_bd))

        most_recent_bd= int(df ['Birth Year'].max())
        print ('The most recent year of birth: {}'. format(most_recent_bd))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    i=0
    raw_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
    while True:
         if raw_data not in ['yes', 'no']:
            print('Sorry, try again')
            raw_data= input('\nWould you like to see more raw data? Enter yes or no.\n')
            continue
         elif raw_data=='no':
              break
         else:
              print(df.iloc[i:i+5])
              raw_data= input('\nWould you like to see more raw data? Enter yes or no.\n')
              i+=5

print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
