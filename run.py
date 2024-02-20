import gspread
from google.oauth2.service_account import Credentials
import statistics

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('ProductSurvey')


# Welcome image and text
def welcome_message():
    print()
    print("Apple Vision Pro Buying Survey!")
    print("""""")
# Menu
    print()
    print("This survey aims to gather insights into the likelihood of purchasing the Apple Vision Pro product.")
    print()
    print("1. Insert Data")
    print("2. Extract Analyzed Data")
    print("3. View Stored Data")
    print("4. Exit\n")


# Input data
def insert_data():
    print("Insert Data")
    print("Please provide the following information:\n")

    gender_choices = {'M': 'Male', 'F': 'Female'}
    gender_input = input("Gender (M/F): ").strip().upper()
    while gender_input not in gender_choices:
        print("Invalid choice. Please choose either 'M' or 'F'.")
        gender_input = input("Gender (M/F): ").strip().upper()
    gender = gender_choices[gender_input]

    age_group_choices = {
        '1': '18-24', '2': '25-34', '3': '35-44',
        '4': '45-54', '5': '55-64', '6': '65+'
    }
    print("\nChoose Age Group:")
    for key, value in age_group_choices.items():
        print(f"{key}: {value}")
    age_group_input = input("Enter the number corresponding to the age group: ").strip()
    while age_group_input not in age_group_choices:
        print("Invalid choice. Please choose a number between 1 and 6.")
        age_group_input = input("Enter the number corresponding to the age group: ").strip()
    age_group = age_group_choices[age_group_input]

    income_bracket_choices = {
        '1': '$25,000-$49,999', '2': '$50,000-$74,999', '3': '$75,000-$99,999',
        '4': '$100,000-$149,999', '5': '$150,000 or more'
    }
    print("\nChoose Income Bracket:")
    for key, value in income_bracket_choices.items():
        print(f"{key}: {value}")
    income_bracket_input = input("Enter the number corresponding to the income bracket: ").strip()
    while income_bracket_input not in income_bracket_choices:
        print("Invalid choice. Please choose a number between 1 and 5.")
        income_bracket_input = input("Enter the number corresponding to the income bracket: ").strip()
    income_bracket = income_bracket_choices[income_bracket_input]

    print("\nEnter the likelihood of purchasing (0-10 scale):")
    likelihood_input = input("Enter a number between 0 and 10: ").strip()
    while not likelihood_input.isdigit() or int(likelihood_input) < 0 or int(likelihood_input) > 10:
        print("Invalid input. Please enter a number between 0 and 10.")
        likelihood_input = input("Enter a number between 0 and 10: ").strip()
    likelihood = int(likelihood_input)

    sheet = GSPREAD_CLIENT.open('ProductSurvey')
    input_data_worksheet = sheet.worksheet('Input data')
    input_data_worksheet.append_row([gender, age_group, income_bracket, likelihood])
    print("\nData has been successfully inserted into the spreadsheet.\n")


# Extract data menu
def extract_analyzed_data():
    print("Extract Analyzed Data")
    print("Choose one of the following options:")
    print("1. Search by Gender")
    print("2. Search by Age Group")
    print("3. Search by Income Bracket")
    print("4. Create Persona (combination of gender, age group, and income bracket)")
    print("5. Return to Main Menu")

    choice = input("Enter your choice: ")

    if choice == '1':
        gender_input = input("Enter the gender (M/F): ").strip().upper()
        while gender_input not in ['M', 'F']:
            print("Invalid choice. Please choose either 'M' or 'F'.")
            gender_input = input("Enter the gender (M/F): ").strip().upper()
        gender = 'Male' if gender_input == 'M' else 'Female'
        likelihood_gender = calculate_likelihood_gender({})[gender]  # Fetch likelihood for the specific gender
        if likelihood_gender is not None:
            print(f"Likelihood of purchase for {gender} is {likelihood_gender:.2f}%")
        else:
            print("No data found for the selected gender.")

    elif choice == '2':
        age_group_choices = {
            '1': '18-24', '2': '25-34', '3': '35-44',
            '4': '45-54', '5': '55-64', '6': '65+'
        }
        print("\nChoose Age Group:")
        for key, value in age_group_choices.items():
            print(f"{key}: {value}")
        age_group_input = input("Enter the number corresponding to the age group: ").strip()
        while age_group_input not in age_group_choices:
            print("Invalid choice. Please choose a number between 1 and 6.")
            age_group_input = input("Enter the number corresponding to the age group: ").strip()
        age_group = age_group_choices[age_group_input]
        likelihood_age_group = calculate_likelihood_age_group(age_group)  # Fetch mean likelihood for the age group
        print(f"Likelihood of purchase for age group {age_group} is {likelihood_age_group:.2f}%")

    if choice == '3':
        income_bracket_choices = {
            '1': '$25,000-$49,999', '2': '$50,000-$74,999', '3': '$75,000-$99,999',
            '4': '$100,000-$149,999', '5': '$150,000 or more'
        }
        print("\nChoose Income Bracket:")
        for key, value in income_bracket_choices.items():
            print(f"{key}: {value}")
        income_bracket_input = input("Enter the number corresponding to the income bracket: ").strip()
        while income_bracket_input not in income_bracket_choices:
            print("Invalid choice. Please choose a number between 1 and 5.")
            income_bracket_input = input("Enter the number corresponding to the income bracket: ").strip()
        income_bracket = income_bracket_choices[income_bracket_input]

        income_bracket_statistics = calculate_likelihood_income_bracket(income_bracket)
        print(f"Likelihood statistics for income bracket {income_bracket}:")
        print(f"Likelihood of purchase for income bracket: {income_bracket_statistics:.2f}%")

    elif choice == '4':
        gender_input = input("Enter the gender (M/F): ").strip().upper()
        while gender_input not in ['M', 'F']:
            print("Invalid choice. Please choose either 'M' or 'F'.")
            gender_input = input("Enter the gender (M/F): ").strip().upper()
        gender = 'Male' if gender_input == 'M' else 'Female'  # Convert "M" to "Male" and "F" to "Female"

        age_group_choices = {
            '1': '18-24', '2': '25-34', '3': '35-44',
            '4': '45-54', '5': '55-64', '6': '65+'
        }
        print("\nChoose Age Group:")
        for key, value in age_group_choices.items():
            print(f"{key}: {value}")
        age_group_input = input("Enter the number corresponding to the age group: ").strip()
        while age_group_input not in age_group_choices:
            print("Invalid choice. Please choose a number between 1 and 6.")
            age_group_input = input("Enter the number corresponding to the age group: ").strip()
        age_group = age_group_choices[age_group_input]

        income_bracket_choices = {
            '1': '$25,000-$49,999', '2': '$50,000-$74,999', '3': '$75,000-$99,999',
            '4': '$100,000-$149,999', '5': '$150,000 or more'
        }
        print("\nChoose Income Bracket:")
        for key, value in income_bracket_choices.items():
            print(f"{key}: {value}")
        income_bracket_input = input("Enter the number corresponding to the income bracket: ").strip()
        while income_bracket_input not in income_bracket_choices:
            print("Invalid choice. Please choose a number between 1 and 5.")
            income_bracket_input = input("Enter the number corresponding to the income bracket: ").strip()
        income_bracket = income_bracket_choices[income_bracket_input]

        persona = {'Gender': gender, 'Age Group': age_group, 'Income Bracket': income_bracket}
        likelihood_percentage = calculate_likelihood_persona(persona)
        if likelihood_percentage is not None:
            formatted_persona = ", ".join([f"{key}: {value}" for key, value in persona.items()])
            print(f"Likelihood of purchase for persona {formatted_persona} is {likelihood_percentage:.2f}%")
        else:
            print("No data found for the selected persona.")

    elif choice == '5':
        return
    else:
        print("Invalid choice. Please try again.")


# Calculation gender for statistics 
def calculate_total_gender_records(gender):
    input_data_worksheet = SHEET.worksheet('Input data')
    analyzed_data = input_data_worksheet.get_all_records()
    print("Analyzing data inside the calculation function:")
    print(analyzed_data)  # Print the data being processed

    total_gender_records = sum(1 for record in analyzed_data if record['Gender'] == gender)
    
    return total_gender_records

# Store search result
def store_search_result(persona, likelihood_percentage):
    sheet = GSPREAD_CLIENT.open('ProductSurvey')
    stored_search_worksheet = sheet.worksheet('Stored last search')
    stored_search_worksheet.append_row([persona['Gender'], persona['Age Group'], persona['Income Bracket'], likelihood_percentage])
    print("Search result stored successfully.")


# Calculate likelihood in percentage
def calculate_likelihood_gender(search_criteria):
    input_data_worksheet = SHEET.worksheet('Input data')
    analyzed_data = input_data_worksheet.get_all_records()
    print("Analyzing data inside the calculation function:")
    print(analyzed_data)  # Print the data being processed

    total_male_records = 0
    total_female_records = 0
    total_male_likelihood_sum = 0
    total_female_likelihood_sum = 0

    for record in analyzed_data:
        if 'Gender' in record and record['Gender'] in ['Male', 'Female']:
            if record['Gender'] == 'Male':
                total_male_records += 1
                total_male_likelihood_sum += record.get('Likelihood', 0)  
            else:
                total_female_records += 1
                total_female_likelihood_sum += record.get('Likelihood', 0) 

    male_likelihood_percentage = (total_male_likelihood_sum / (total_male_records * 10)) * 100 if total_male_records > 0 else 0
    female_likelihood_percentage = (total_female_likelihood_sum / (total_female_records * 10)) * 100 if total_female_records > 0 else 0

    return {'Male': male_likelihood_percentage, 'Female': female_likelihood_percentage}

# Calculate age group
def calculate_likelihood_age_group(age_group):
    input_data_worksheet = SHEET.worksheet('Input data')
    analyzed_data = input_data_worksheet.get_all_records()

    likelihood_values = [record.get('Likelihood', 0) for record in analyzed_data if record.get('Age Group') == age_group]

    if not likelihood_values:
        return 0

    mean_likelihood = statistics.mean(likelihood_values)
    mean_likelihood_percent = (mean_likelihood / 10) * 100

    return mean_likelihood_percent
    

# Calculate income bracket
def calculate_likelihood_income_bracket(income_bracket):
    input_data_worksheet = SHEET.worksheet('Input data')
    analyzed_data = input_data_worksheet.get_all_records()

    likelihood_values = [record.get('Likelihood', 0) for record in analyzed_data if record.get('Income Bracket') == income_bracket]

    if not likelihood_values:
        return 0

    mean_likelihood = statistics.mean(likelihood_values)
    mean_likelihood_percent = (mean_likelihood / 10) * 100

    return mean_likelihood_percent

# Calculate Persona
def calculate_likelihood_persona(persona):
    input_data_worksheet = SHEET.worksheet('Input data')
    analyzed_data = input_data_worksheet.get_all_records()
    
    matching_records = [record for record in analyzed_data if all(key != 'Likelihood' and record.get(key) == value for key, value in persona.items())]

    if not matching_records:
        print(f"No data found for the persona: {persona}")
        return None  # Return None if no data is found for the persona

    total_records = len(matching_records)
    total_likelihood = sum(record.get('Likelihood', 0) for record in matching_records)

    likelihood_percentage = (total_likelihood / (total_records * 10)) * 100

    return likelihood_percentage


# View stored data menu
def view_stored_data():
    print("View Stored Data")
    print("Choose one of the following options:")
    print("1. View Last Search Persona")
    print("2. View All Stored Search Personas")
    print("3. Return to Main Menu")

    choice = input("Enter your choice: ")

    if choice == '1':
        view_last_search_persona()
    elif choice == '2':
        view_all_stored_search_personas()
    elif choice == '3':
        return
    else:
        print("Invalid choice. Please try again.")

# View last persona
def view_last_search_persona():
    sheet = GSPREAD_CLIENT.open('ProductSurvey')
    stored_search_worksheet = sheet.worksheet('Stored last search')
    last_search_persona = stored_search_worksheet.get_all_records()[-1] 

    print("\nLast Search Persona:")
    for key, value in last_search_persona.items():
        print(f"{key}: {value}")

    if 'Likelihood Percentage' in last_search_persona:
        print("Likelihood Percentage:", last_search_persona['Likelihood Percentage'])
    else:
        print("Likelihood Percentage: Data not available")

# View all personas
def view_all_stored_search_personas():
    sheet = GSPREAD_CLIENT.open('ProductSurvey')
    stored_search_worksheet = sheet.worksheet('Stored last search')
    all_stored_search_personas = stored_search_worksheet.get_all_records()

    print("\nAll Stored Search Personas:")
    for persona in all_stored_search_personas:
        for key, value in persona.items():
            print(f"{key}: {value}")
        print()

#Main function
def main():
    while True:
        welcome_message()
        choice = input("Enter your choice: ")
        print()

        if choice == '1':
            insert_data()
        elif choice == '2':
            extract_analyzed_data()
        elif choice == '3':
            view_stored_data() 
        elif choice == '4':
            print("Exiting the program...\n")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()