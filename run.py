import gspread
from google.oauth2.service_account import Credentials

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
.........................:=++*********++++==---------:--:---------=**.......................................
..................::::-=++++********************+=---:--:---------+*+:......................................
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
.............=---::::::::::::::::::::::::::::::::::::::=+=.................:++++++++++++++++++++=...........
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
.........*#+.+#*:..=##=..=##=.+##:..+#*::*##......=##++++-..................................................
........:##-.=*#=..=#######*:.+#######+.:*##......=##****+..................................................
........+##:.-*#*..=##*+=-:...+##++=-...:*##......=##-......................................................
........*##****##:.=##=.......+##:......:*##......=##-......................................................
.......-##*+++*##=.=##=.......+##:......:*##......=##-......................................................
.......=##-...-##+.=##=.......+##:......:*######*:=#######*.................................................
.......=++.....++=.-++-.......=++:......:+++++++=.-+++++++=.................................................
............................::..............::...............................................:::............
.......=##=....*#+.=##-..=*####*-..+##-..-*#####+..:###*..:*#=......+######*:..#######*:...+######-.........
.......-##*...-##=.=##-.=##*::+#*:.+##-.-*#*::+##=.:####=.:*#=......+##=:-*#*-.##*-:=##*:.+##+::*#*:........
.......:###:..+##:.=##-.+##=..=**-.+##-.=##=..-*#*.:####*::*#=......+##=..+##=.##*:..*#*-.*##...=##-........
........*##-..*#*..=##-.-##*:......+##-.=##=..-*#*.:##***=:*#=......+##=..+##=.##*:..*#*-.*##...=##-........
........=##=.:*#=..=##-..=*##+.....+##-.=##=..-*#*.:##+=#*:*#=......+##=..+##=.##*:.=##*..*##...=##-........
........:*#+.-**:..=##-...:+##*=...+##-.=##=..-*#*.:##+:*#=*#=......+##***##*..######*+...*##...=##-........
.........*#*.+#*...=##-.....:*##+..+##-.=##=..-*#*.:##+.=#**#=......+##*+==:...##*-:=##*:.*##...=##-........
.........+##:*#+...=##-.=++:..+##-.+##-.=##=..-*#*.:##+.:*###=......+##=.......##*:..*#*-.*##...=##-........
.........=##+*#=...=##-.+##:..+##=.+##-.=##=..-*#+.:##+..=###=......+##=.......##*:..*#*-.+##...=##-........
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
    """
    The user enter data: gender, age-group, income bracket, likelihood of purchasing
    """
    print("Please provide the following information:\n")

    # Choose gender
    gender_choices = {'M': 'Male', 'F': 'Female'}
    gender_input = input("Gender (M/F): ").strip().upper()
    while gender_input not in gender_choices:
        print("Invalid choice. Please choose either 'M' or 'F'.")
        gender_input = input("Gender (M/F): ").strip().upper()
    gender = gender_choices[gender_input]
    print()
    print()

    # Choose age group
    age_group_choices = {
        '1': '18-24', '2': '25-34', '3': '35-44',
        '4': '45-54', '5': '55-64', '6': '65+\n'
    }
    print("Choose Age Group:\n")
    for key, value in age_group_choices.items():
        print(f"{key}: {value}")
    age_group_input = input("Enter the number corresponding to the age group: ").strip()
    while age_group_input not in age_group_choices:
        print("Invalid choice. Please choose a number between 1 and 6.")
        age_group_input = input("Enter the number corresponding to the age group: ").strip()
    age_group = age_group_choices[age_group_input]
    print()
    print()

     # Choose income bracket
    income_bracket_choices = {
        '1': '$25,000-$49,999', '2': '$50,000-$74,999', '3': '$75,000-$99,999',
        '4': '$100,000-$149,999', '5': '$150,000 or more\n'
    }
    print("Choose Income Bracket:\n")
    for key, value in income_bracket_choices.items():
        print(f"{key}: {value}")
    income_bracket_input = input("Enter the number corresponding to the income bracket: ").strip()
    while income_bracket_input not in income_bracket_choices:
        print("Invalid choice. Please choose a number between 1 and 5.")
        income_bracket_input = input("Enter the number corresponding to the income bracket: ").strip()
    income_bracket = income_bracket_choices[income_bracket_input]
    print()
    print()

     # Likelihood of purchasing
    likelihood_purchasing_choices = {
        '1': 'None', '2': 'Slim', '3': 'Unlikely',
        '4': 'Possible', '5': 'Very likely\n'
    }
    print("Likelihood to purchasing the Apple Vision Pro:\n")
    for key, value in likelihood_purchasing_choices.items():
        print(f"{key}: {value}")
    likelihood_purchasing_input = input("Enter the number corresponding to the likelihood of purchasing: ").strip()
    while likelihood_purchasing_input not in likelihood_purchasing_choices:
        print("Invalid choice. Please choose a number between 1 and 5.")
        likelihood_purchasing_input = input("Enter the number corresponding to the likelihood of purchasing: ").strip()
    likelihood_purchasing = likelihood_purchasing_choices[likelihood_purchasing_input]

    sheet = GSPREAD_CLIENT.open('ProductSurvey')

    input_data_worksheet = sheet.worksheet('Input data')

    input_data_worksheet.append_row([gender, age_group, income_bracket, likelihood_purchasing])
    print()
    print("Data has been successfully inserted into the spreadsheet.\n")


# Analyzing results
def calculate_percentage(likelihood):
    """
    Calculates the liklelihood of purchasing the Apple Vision Pro
    """
    return (likelihood / 5) * 100

def categorize_likelihood(percentage):
    """
    Categorize the prosentage in low, medium, high
    """
    if percentage <= 30:
        return 'Low'
    elif percentage <= 70:
        return 'Medium'
    else:
        return 'High'

def insert_analyzed_data(age_group, gender, income_bracket, likelihood):
    """
    Inserts the analyzed data to the workshe
    """
    percentage = calculate_percentage(likelihood)
    likelihood_category = categorize_likelihood(percentage)

    # Open the spreadsheet
    sheet = GSPREAD_CLIENT.open('ProductSurvey')

    # Access the worksheet
    analyzed_data_worksheet = sheet.worksheet('Analyzed data')

    # Append the data to the worksheet
    analyzed_data_worksheet.append_row([age_group, gender, income_bracket, likelihood, percentage, likelihood_category])

    print("Analyzed data has been successfully inserted into the spreadsheet.")


# View analyyzed data, option to store search result
def extract_analyzed_data():
    """
    The user extract data based on search: gender, age-group, income bracket.
    recives procentage of likelihood of purchasing the Apple Vision Pro. 
    the result will also get categorized in strong, medium and low chance of purchasing.
    the user has the option to store the search result
    """
    print("Extract Analyzed Data")

#View last search result
def view_stored_data():
    """
    The user can view their latest stored search result
    """
    print("View Stored Data")


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

    insert_analyzed_data(age_group, gender, income_bracket, likelihood)

if __name__ == "__main__":
    main()
