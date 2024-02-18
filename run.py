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

def welcome_message():
    print()
    print("Apple Vision Pro Buying Survey!")
    print("""
............................................................................................................
............................................................................................................
............................................................................................................
............................................................................................................
............................................................................................................
............................................................................................................
............................................................................................................
.............................................:----===----:..................................................
....................................:-=====----------------==++=:...........................................
.................................-+=---:---:--------------------=++:........................................
...............................==----------:------------:---------=*:.......................................
.........................:=++*********++++==---------:--:---------+*+:......................................
..................::::-=++++********************+=---:--:---------**.......................................
..............:=-=++++**++====----------==++*********---::--------**+-......................................
.............------------:::::::::::::::::::::--=+*****=::------+**++-......................................
............=:----::::::..:::::::::::::::::::::::::-+***+--:--=+***++-......................................
...........-=::..........:::::::::..........:::::-:::-+*++-+*****+++++:.....................................
...........-=--:::::::...:::::::::...........::::::-::-+**********+++.==...::::::...........................
...........------:::::::::::::::::............:::::::.:-*********+++-..:=++++++++++++=-:....................
...........------:::::::::::::::::.::.........::::::::::+********-.....-++=--:::::--===+=...................
...........-=----::::::::::::::::::::::.......::::::::::=*******-......-===+++++++++++++==-.................
...........:=----:::::::::::::::::::::::::::::::::::::::=++=*=:..........::-==+++++++++++++=--:.............
............=----:::::::::::::::::::::::::::::::::::::::++=..................=++++++++++++++++++-...........
.............=---:::::::::::::::::::::::::::::::::::::::+=.................:++++++++++++++++++++=...........
..............=---::::::::----:::::::::::::::::::::::--+-.................=+++++++++++++++++++++............
...............:---::::---:.....::::::::::::::::::::--:.................:=++++++++++++++++++++=.............
..................:::..............:::::::::::::::::...................-++++++++++++++++++++++:.............
.......................................:::::::::......................=+*****************++++:..............
......................................................................-++++++++++++++++++*++:...............
........................................................................:--===+++++++++++++-................
......................................................................................::::..................
............................................................................................................
..........*####:...=######*=..+#####**:.:*##......=#######*.................................................
.........:##*##-...=##+--*#*-.+##=-=*#*.:*##......=##=-----.................................................
.........=##-##+...=##=..-##+.+##:..+##::*##......=##-......................................................
.........+#*.*#*...=##=..-##+.+##:..+##::*##......=##-......................................................
.........*#+.+#*:..=##=..=##=.+##:..+#*::*##......=##-......................................................
........:##-.=*#=..=##=..=##=.+##:..+##::*##......=##++++-..................................................
........+##:.-*#*..=##=..=##=.+##:..+#*::*##......=##****+..................................................
........*##****##:.=##=..=##=.+##:..+##::*##......=##-......................................................
.......-##*+++*##=.=##=..=##=.+##:..+##::*##......=##-......................................................
.......=##-...-##+.=##=..=##=.+##:..+##::*##......=##-......................................................
.......=++.....++=.-++-...=++:.=++:..=++-.*++......=++=......................................................
............................::..............::...............................................:::............
.......=##=....*#+.=##-..=*####*-..+##-..-*#####+..:###*..:*#=......+######*:..#######*:...+######-.........
.......-##*...-##=.=##-.=##*::+#*:.+##-.-*#*::+##=.:####=.:*#=......+##=:-*#*-.##*-:=##*:.+##+::*#*:........
.......:###:..+##:.=##-.+##=..=**-.+##-.=##=..-*#*.:####*::*#=......+##=..+##=.##*:..*#*-.*##...=##-........
........*##-..*#*..=##-.-##*:......+##-.=##=..-*#*.:##***=:*#=......+##=..+##=.##*:..*#*-.*##...=##-........
........=##=.:*#=..=##-..=*##+.....+##-.=##=..-*#*.:##+=#*:*#=......+##=..+##=.##*:.=##*..*##...=##-........
........:*#+.-**:..=##-...:+##*=...+##-.=##=..-*#*.:##+:*#=*#=......+##***##*..######*+...*##...=##-........
.........*#*.+#*...=##-.....:*##+..+##-.=##=..-*#*.:##+.=#**#=......+##*+==:...##*-:=##*:.*##...=##-........
.........+##:*#+...=##-.=++:..+##-.+##-.=##=..-*#+.:##+..=###=......+##=.......##*:..*#*-.*##...=##-........
.........=##+*#=...=##-.+##:..+##=.+##-.=##=..-*#+.:##+..=###+......+##=.......##*:..*#*-.*##...=##-........
.........:#####:...=##-.-*#***##*..+##-.:*##***#*:.:##+..:*##=......+##=.......##*:..*#*-.-###**##*.........
..........+++++....=++-...=***+-...=++-...-+***=...:++=...=++=......+++-.......+++:..=++-...=***+-..........
............................................................................................................
............................................................................................................
............................................................................................................
............................................................................................................
    """)
    print()
    print("This survey aims to gather insights into the likelihood of purchasing the Apple Vision Pro product.")
    print()
    print("1. Insert Data")
    print("2. Extract Analyzed Data")
    print("3. View Stored Data")
    print("4. Exit\n")

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


# Extract data
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
        gender = input("Enter the gender (M/F): ").strip().upper()
        likelihood_percentage = calculate_likelihood_percentage({'Gender': gender})
        print(f"Likelihood of purchase for {gender} is {likelihood_percentage:.0f}%")

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
        likelihood_percentage = calculate_likelihood_percentage({'Age Group': age_group})
        print(f"Likelihood of purchase for age group {age_group} is {likelihood_percentage:.0f}%")

    elif choice == '3':
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
        likelihood_percentage = calculate_likelihood_percentage({'Income Bracket': income_bracket})
        print(f"Likelihood of purchase for income bracket {income_bracket} is {likelihood_percentage:.0f}%")

    elif choice == '4':
        gender = input("Enter the gender (M/F): ").strip().upper()
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
        likelihood_percentage = calculate_likelihood_percentage(persona)
        print(f"Likelihood of purchase for persona {persona} is {likelihood_percentage:.0f}%")
        
        store_choice = input("Do you want to store this persona search result? (Y/N): ").strip().upper()
        if store_choice == 'Y':
            store_search_result(persona, likelihood_percentage)

    elif choice == '5':
        return
    else:
        print("Invalid choice. Please try again.")


def store_search_result(persona, likelihood_percentage):
    sheet = GSPREAD_CLIENT.open('ProductSurvey')
    stored_search_worksheet = sheet.worksheet('Stored last search')
    stored_search_worksheet.append_row([persona['Gender'], persona['Age Group'], persona['Income Bracket'], likelihood_percentage])
    print("Search result stored successfully.")

 # Calculation of chance of purchase
def calculate_likelihood_statistics(search_criteria):
    input_data_worksheet = SHEET.worksheet('Input data')
    analyzed_data = input_data_worksheet.get_all_records()

    matching_records = []

    # Filter records based on search criteria
    for record in analyzed_data:
        match = all(record.get(key) == value for key, value in search_criteria.items())
        if match:
            matching_records.append(record)

    # Calculate likelihood statistics for matching records
    likelihood_values = [record['Likelihood'] for record in matching_records if 'Likelihood' in record]
    if not likelihood_values:
        return {
            'Mean': 0,
            'Median': 0,
            'Standard Deviation': 0
        }  # Return 0 for all statistics if there are no matching records

    # Calculate mean, median, and standard deviation
    mean_likelihood = statistics.mean(likelihood_values)
    median_likelihood = statistics.median(likelihood_values)
    std_dev_likelihood = statistics.stdev(likelihood_values)

    # Convert mean, median, and standard deviation to percentages
    mean_likelihood_percent = (mean_likelihood / 10) * 100
    median_likelihood_percent = (median_likelihood / 10) * 100
    std_dev_likelihood_percent = (std_dev_likelihood / 10) * 100

    return {
        'Mean': mean_likelihood_percent,
        'Median': median_likelihood_percent,
        'Standard Deviation': std_dev_likelihood_percent
    }

def calculate_likelihood_percentage(search_criteria):
    input_data_worksheet = SHEET.worksheet('Input data')
    analyzed_data = input_data_worksheet.get_all_records()

    total_records = len(analyzed_data)
    matching_records = 0

    # Count matching records based on search criteria
    for record in analyzed_data:
        match = all(record.get(key) == value for key, value in search_criteria.items())
        if match:
            matching_records += 1

    # Calculate likelihood percentage
    if total_records > 0:
        likelihood_percentage = (matching_records / total_records) * 100
    else:
        likelihood_percentage = 0

    return round(likelihood_percentage, -1)  # Round the percentage to the nearest 10

def store_search_result(persona, likelihood_percentage):
    
    sheet = GSPREAD_CLIENT.open('ProductSurvey')
    stored_search_worksheet = sheet.worksheet('Stored last search')
    stored_search_worksheet.append_row([persona['Gender'], persona['Age Group'], persona['Income Bracket'], likelihood_percentage])
    print("Search result stored successfully.")


# View stored data
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

def view_last_search_persona():
    sheet = GSPREAD_CLIENT.open('ProductSurvey')
    stored_search_worksheet = sheet.worksheet('Stored last search')
    last_search_persona = stored_search_worksheet.get_all_records()[-1]  # Get the last stored search

    print("\nLast Search Persona:")
    for key, value in last_search_persona.items():
        print(f"{key}: {value}")

    # Check if 'Likelihood Percentage' exists in the last search persona
    if 'Likelihood Percentage' in last_search_persona:
        print("Likelihood Percentage:", last_search_persona['Likelihood Percentage'])
    else:
        print("Likelihood Percentage: Data not available")

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