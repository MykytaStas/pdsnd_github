import time
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 500)

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
    city=input("Enter name of the city to analyze (chicago, new york city or washington): ").lower()
    month=input("Enter a month (all, january, february, ... , june) to filter by: ").lower()
    day=int(input("Enter weekday number (1-7) or 0 for all days: "))

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

    df= pd.read_csv(CITY_DATA[city])
    df=df.fillna(method = 'backfill', axis = 0)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of week'] = df['Start Time'].dt.dayofweek +1
    df['Hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]

    if day != 0:
        df = df[df['Day of week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    days=['Mo','Di','We','Th','Fr','Sa','Su']
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    common_day = int(df['Day of week'].mode()[0])
    days=['Monday','Tuesday','Wednesday','Thirsday','Friday','Saturday','Sunday']
    common_month = int(df['Month'].mode()[0])
    months=['January','February','March','April','May','June']

    print("The most common month:\n",months[common_month-1],"\n")
    print("The most common day of week:\n",days[common_day-1],"\n")
    print("The most common start hour:\n",df['Hour'].mode()[0],"\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print("The most commonly used start station:\n",df['Start Station'].mode()[0],"\n")
    print("The most commonly used end station:\n",df['End Station'].mode()[0],"\n")
    print("The most frequent combination of start station and end station trip:\n1)",(df['Start Station'] + '; 2) ' + df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print("Total duration:\n",df["Trip Duration"].sum()/3600,"hours\n")
    print("Mean duration:\n",df["Trip Duration"].mean()/3600*60,"minutes\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print("Counts of user types:\n",df["User Type"].value_counts(),"\n")
    print("Counts of gender:\n",df["Gender"].value_counts(),"\n")
    print("Earliest year of birth\n",df["Birth Year"].astype(int).min(),"\n")
    print("Most recent year of birth\n",df["Birth Year"].astype(int).max(),"\n")
    print("Most common year of birth\n",df["Birth Year"].astype(int).mode()[0],"\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Asks user how many rows of row data should be displayed."""
    print("These are the first 5 raw data:\n")
    x=5
    print(df.iloc[:x,:])

    while input("Do you want to see next 5 rows? Enter yes or no.\n ").lower()=="yes":
        x+=5
        print(df.iloc[x-5:x,:])





def main():
    while True:
        try:
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

        except (KeyError,ValueError,UnboundLocalError):
                print("You entered the wrong city or month name. Try again.")
                restart = input('\nWould you like to restart? Enter yes or no.\n')
                if restart.lower() != 'yes':
                    break

if __name__ == "__main__":
	main()
