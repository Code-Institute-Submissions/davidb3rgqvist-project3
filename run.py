import gspread
from google.oauth2.service_account import Credentials
import statistics
import os

class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

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
    print(Color.CYAN + "This survey aims to gather insights into the likelihood of purchasing the Apple Vision Pro product." + Color.END)
    print()
    print("1. Insert Data")
    print("2. Extract Analyzed Data")
    print("3. View Stored Data")
    print("4. Exit")
    print()


# Input data
def insert_data():
    print("Insert Data - Please provide the following information:\n")
    print(Color.UNDERLINE + "Choose Gender:\n" + Color.END)

    gender_choices = {'M': 'Male', 'F': 'Female'}
    gender_input = input( "Gender (M/F): ").strip().upper()
    print()
    while gender_input not in gender_choices:
        print("Invalid choice. Please choose either 'M' or 'F'.")
        gender_input = input("Gender (M/F): ").strip().upper()
    gender = gender_choices[gender_input]

    age_group_choices = {
        '1': '18-24', '2': '25-34', '3': '35-44',
        '4': '45-54', '5': '55-64', '6': '65+'
    }
    print(Color.UNDERLINE + "\nChoose Age Group:\n" + Color.END)
    for key, value in age_group_choices.items():
        print(f"{key}: {value}")
    age_group_input = input("\nEnter the number corresponding to the age group: ").strip()
    print()
    while age_group_input not in age_group_choices:
        print("\nInvalid choice. Please choose a number between 1 and 6.")
        age_group_input = input("\nEnter the number corresponding to the age group: ").strip()
        print()
    age_group = age_group_choices[age_group_input]

    income_bracket_choices = {
        '1': '$25,000-$49,999', '2': '$50,000-$74,999', '3': '$75,000-$99,999',
        '4': '$100,000-$149,999', '5': '$150,000 or more'
    }
    print(Color.UNDERLINE + "\nChoose Income Bracket:\n" + Color.END)
    for key, value in income_bracket_choices.items():
        print(f"{key}: {value}")
    income_bracket_input = input("\nEnter the number corresponding to the income bracket: ").strip()
    print()
    while income_bracket_input not in income_bracket_choices:
        print("Invalid choice. Please choose a number between 1 and 5.")
        income_bracket_input = input("Enter the number corresponding to the income bracket: ").strip()
    income_bracket = income_bracket_choices[income_bracket_input]

    print(Color.UNDERLINE + "\nEnter the likelihood of purchasing (0-10 scale):\n" + Color.END)
    likelihood_input = input("Enter a number between 0 and 10: ").strip()
    print()
    while not likelihood_input.isdigit() or int(likelihood_input) < 0 or int(likelihood_input) > 10:
        print("\nInvalid input. Please enter a number between 0 and 10.")
        likelihood_input = input("\nEnter a number between 0 and 10: ").strip()
    likelihood = int(likelihood_input)

    sheet = GSPREAD_CLIENT.open('ProductSurvey')
    input_data_worksheet = sheet.worksheet('Input data')
    input_data_worksheet.append_row([gender, age_group, income_bracket, likelihood])
    print(Color.GREEN + "\nData has been successfully inserted into the spreadsheet.\n" + Color.END)
    print()
    press_enter_to_main_menu()

# Extract data menu
def extract_analyzed_data():
    print()
    print("Extract Analyzed Data:\n")
    print(Color.UNDERLINE + "Choose one of the following options:" + Color.END)
    print()
    print("1. Search by Gender")
    print("2. Search by Age Group")
    print("3. Search by Income Bracket")
    print("4. Create Persona (combination of gender, age group, and income bracket)")
    print("5. Return to Main Menu\n")

    choice = input("Enter your choice: ")
    print() 

    if choice == '1':
        gender_input = input(Color.UNDERLINE + "Enter the gender (M/F): " + Color.END).strip().upper()
        print()
        while gender_input not in ['M', 'F']:
            print("Invalid choice. Please choose either 'M' or 'F'.")
            gender_input = input("Enter the gender (M/F): ").strip().upper()
        gender = 'Male' if gender_input == 'M' else 'Female'
        likelihood_gender = calculate_likelihood_gender({})[gender]  
        if likelihood_gender is not None:
            print(Color.GREEN + f"\nLikelihood of purchase for {gender} is {likelihood_gender:.2f}%\n"+ Color.END)
            press_enter_to_main_menu()
        else:
            print("\nNo data found for the selected gender.\n")
            press_enter_to_main_menu()

    elif choice == '2':
        age_group_choices = {
            '1': '18-24', '2': '25-34', '3': '35-44',
            '4': '45-54', '5': '55-64', '6': '65+'
        }
        print(Color.UNDERLINE + "Choose Age Group:\n" + Color.END)
        for key, value in age_group_choices.items():
            print(f"{key}: {value}")
        print()
        age_group_input = input("Enter the number corresponding to the age group: ").strip()
        while age_group_input not in age_group_choices:
            print("Invalid choice. Please choose a number between 1 and 6.")
            age_group_input = input("Enter the number corresponding to the age group: ").strip()
        age_group = age_group_choices[age_group_input]
        likelihood_age_group = calculate_likelihood_age_group(age_group)
        print(Color.GREEN + f"\nLikelihood of purchase for age group {age_group} is {likelihood_age_group:.2f}%\n" + Color.END)
        press_enter_to_main_menu()

    if choice == '3':
        income_bracket_choices = {
            '1': '$25,000-$49,999', '2': '$50,000-$74,999', '3': '$75,000-$99,999',
            '4': '$100,000-$149,999', '5': '$150,000 or more'
        }
        print(Color.UNDERLINE + "Choose Income Bracket:\n" + Color.END)
        for key, value in income_bracket_choices.items():
            print(f"{key}: {value}")
        income_bracket_input = input("Enter the number corresponding to the income bracket: ").strip()
        print()
        while income_bracket_input not in income_bracket_choices:
            print("Invalid choice. Please choose a number between 1 and 5.")
            income_bracket_input = input("Enter the number corresponding to the income bracket: ").strip()
        income_bracket = income_bracket_choices[income_bracket_input]

        income_bracket_statistics = calculate_likelihood_income_bracket(income_bracket)
        print(Color.GREEN + f"Likelihood of purchase for income bracket: {income_bracket_statistics:.2f}%\n" + Color.END)
        press_enter_to_main_menu()

    elif choice == '4':
        gender_input = input(Color.UNDERLINE + "\nEnter the gender (M/F): " + Color.END).strip().upper()
        print()
        while gender_input not in ['M', 'F']:
            print("Invalid choice. Please choose either 'M' or 'F'.")
            print()
            gender_input = input("\nEnter the gender (M/F): ").strip().upper()
            print()
        gender = 'Male' if gender_input == 'M' else 'Female' 

        age_group_choices = {
            '1': '18-24', '2': '25-34', '3': '35-44',
            '4': '45-54', '5': '55-64', '6': '65+'
        }
        print(Color.UNDERLINE + "Choose Age Group:\n" + Color.END)
        for key, value in age_group_choices.items():
            print(f"{key}: {value}")
        age_group_input = input("\nEnter the number corresponding to the age group: ").strip()
        print()
        while age_group_input not in age_group_choices:
            print("Invalid choice. Please choose a number between 1 and 6.")
            age_group_input = input("\nEnter the number corresponding to the age group: ").strip()
            print()
        age_group = age_group_choices[age_group_input]

        income_bracket_choices = {
            '1': '$25,000-$49,999', '2': '$50,000-$74,999', '3': '$75,000-$99,999',
            '4': '$100,000-$149,999', '5': '$150,000 or more'
        }
        print(Color.UNDERLINE + "Choose Income Bracket:\n" + Color.END)
        for key, value in income_bracket_choices.items():
            print(f"{key}: {value}")
        income_bracket_input = input("Enter the number corresponding to the income bracket: ").strip()
        while income_bracket_input not in income_bracket_choices:
            print("\nInvalid choice. Please choose a number between 1 and 5.\n")
            income_bracket_input = input("Enter the number corresponding to the income bracket: \n").strip()
        income_bracket = income_bracket_choices[income_bracket_input]

        persona = {'Gender': gender, 'Age Group': age_group, 'Income Bracket': income_bracket}
        likelihood_percentage = calculate_likelihood_persona(persona)
        if likelihood_percentage is not None:
            formatted_persona = ", ".join([f"{key}: {value}" for key, value in persona.items()])
            print()
            print(Color.GREEN + f"\nLikelihood of purchase for persona {formatted_persona} is {likelihood_percentage:.2f}%\n" + Color.END)
            print()
            press_enter_to_main_menu()
        else:
            print()
            print("\nNo data found for the selected persona.")
            press_enter_to_main_menu()

    elif choice == '5':
        return
    else:
        print("\nInvalid choice. Please try again.")


# Calculation gender for statistics 
def calculate_total_gender_records(gender):
    input_data_worksheet = SHEET.worksheet('Input data')
    analyzed_data = input_data_worksheet.get_all_records()
    print("Analyzing data inside the calculation function:")

    total_gender_records = sum(1 for record in analyzed_data if record['Gender'] == gender)
    
    return total_gender_records

# Store search result
def store_search_result(persona, likelihood_percentage):
    sheet = GSPREAD_CLIENT.open('ProductSurvey')
    stored_search_worksheet = sheet.worksheet('Stored last search')
    stored_search_worksheet.append_row([persona['Gender'], persona['Age Group'], persona['Income Bracket'], likelihood_percentage])
    print("Search result stored successfully.")
    press_enter_to_main_menu()

# Calculate likelihood in percentage
def calculate_likelihood_gender(search_criteria):
    input_data_worksheet = SHEET.worksheet('Input data')
    analyzed_data = input_data_worksheet.get_all_records() 

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

    likelihood_values = [int(str(record.get('Likelihood', 0))) for record in analyzed_data if record.get('Age Group') == age_group and str(record.get('Likelihood', 0)).isdigit()]

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
        return None  

    total_records = len(matching_records)
    total_likelihood = sum(record.get('Likelihood', 0) for record in matching_records)

    likelihood_percentage = (total_likelihood / (total_records * 10)) * 100

    return likelihood_percentage


# View stored data menu
def view_stored_data():
    print("View Stored Data:")
    print()
    print(Color.UNDERLINE + "Choose one of the following options:" + Color.END)
    print("1. View Last Search Persona")
    print("2. View All Stored Search Personas")
    print("3. Return to Main Menu\n")

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

    print(Color.UNDERLINE + "\nLast Search Persona:" + Color.UNDERLINE)
    for key, value in last_search_persona.items():
        print(f"{key}: {value}")

    if 'Likelihood Percentage' in last_search_persona:
        print("Likelihood Percentage:", last_search_persona['Likelihood Percentage'])
    else:
        print("Likelihood Percentage: Data not available")

    print()
    press_enter_to_main_menu()

# View all personas
def view_all_stored_search_personas():
    sheet = GSPREAD_CLIENT.open('ProductSurvey')
    stored_search_worksheet = sheet.worksheet('Stored last search')
    all_stored_search_personas = stored_search_worksheet.get_all_records()

    print(Color.UNDERLINE + "\nAll Stored Search Personas:" + Color.END)
    for persona in all_stored_search_personas:
        for key, value in persona.items():
            print(f"{key}: {value}")
        print()
    
    press_enter_to_main_menu()

def press_enter_to_main_menu():
    input("Press Enter to return to the main menu...")
    main()

def clear_screen():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

#Main function
def main():
    while True:
        clear_screen()
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