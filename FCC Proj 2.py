import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    # Copy of dataframe containing only males
    males = df[df['sex'] == 'Male'] # this contains all the males in the database
    average_age_men = males['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    # create python series which contains all the degrees
    degrees = df['education'].value_counts()
    percentage_bachelors = (degrees['Bachelors']/degrees.sum()) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors','Masters','Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors','Masters','Doctorate'])]

    # percentage with salary >50K
    higher_education_rich = (len(higher_education[higher_education['salary'] == '>50K'])/len(higher_education)) * 100
    lower_education_rich = (len(lower_education[lower_education['salary'] == '>50K'])/len(lower_education)) * 100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    # dataframe containing workers who work for the minimum number of hours
    df_min_work_hours = df[df['hours-per-week'] == 1]

    num_min_workers = len(df_min_work_hours[df_min_work_hours['salary'] == '>50K'])

    rich_percentage = (num_min_workers/len(df_min_work_hours)) * 100

    # What country has the highest percentage of people that earn >50K?
    high_salary = df[df['salary'] == '>50K']
    country_list = high_salary['native-country'].value_counts()

    highest_earning_country = country_list.idxmax()
    highest_earning_country_percentage = (country_list.max()/country_list.sum()) * 100

    # Identify the most popular occupation for those who earn >50K in India.
    # Dataframe containing all Indians who earn >50K
    rich_indians = high_salary[high_salary['native-country'] == 'India']


    top_IN_occupation = rich_indians['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()