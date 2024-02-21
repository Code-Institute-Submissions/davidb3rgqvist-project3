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
    """
    The welcome_message() function displays a welcome message for the Apple Vision Pro Buying Survey. It includes an 
    ASCII art representation of the Apple logo and a brief introduction to the survey's purpose. Additionally, it presents 
    a menu with options to insert data, extract analyzed data, view stored data, or exit the program.
    """
    print()
    print("Apple Vision Pro Buying Survey!")
    print("""
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                   .:-+*****+++++++**##*=-..                                        
                              ..+#+=--=----=------------==+##:.                                     
                            .=*=------=----=---------------==*#.                                    
                        .=*%%%%%%%#*+=-----=----------------==%#.                                   
                  ..:-%%%%%%%%%%%%%%%%%%%%%%#+-------------==+%%.                                   
             :+=***#%%%#*+++=======++*#%%%%%%%%%#=----------=%%#:                                   
            =-=---===--------::::::::::::--=+*%%%%%+-------+%%%#:                                   
          .+:----::--...::---::--::::::::::::::-*%%%#----=#@@%%#:                                   
          :+:...........:::::::..........:-----::-#%###%@@@@%###*-                                  
          -+=--::.......:::::::...........:-----::-%@@@@@@@@%##*.=+===++++==-:.                     
          ===-------:::::::::::............------..-@@@@@@@%%*+. .=*##***********-                  
          -+=---------:::::::..............:-----::-#@@@@@%%-    .+**-:......:-*##-.                
          :+=---------:::::::::::::........::------:*%#%%%*.     .-+******#######**#.               
          .+=------------::-:::::::::::::::::::--:::*%=..              .+###############*.          
           -+=--------:::::::::::::::::::::::::::::=%#.               :*#################=          
            -=------:::::::-:::::::::::::::::::::-=#+.              .+###################:          
             .==-----:-+=-:..::::::::::::::::::--=*:               :*###################:           
               .:--:..        ..:::::::::::::---.                .+*###################-            
                                  ..::::----:..                  +%@@@@@@@@@@@@%%%####-             
                                                                 +################%%#=.             
                                                                  .-==+**#########%%=               
                                                                              ..::..                
         .::::   .::::::.  .::::::.  .:::     .:::::::.                                             
        .#@@@@:  .@@@@@@@#.:@@@@@@@*.-@@#     =@@@@@@@=                                             
        .%@@@@-  .@@%. +@@=:@@%. *@@:-@@#     =@@+                                                  
        .@@:@@+  .@@%. :@@+:@@%. =@@=-@@#     =@@+                                                  
        +@%.%@%  .@@%. :@@+:@@%. =@@=-@@#     =@@+                                                  
       .@@#.*@@: .@@@++@@@::@@@+*@@@:-@@#     =@@@@@@+                                              
       :@@+ =@@+ .@@@@@@%- :@@@@@@%: -@@#     =@@*:::.                                              
       =@@+=*@@%..@@%.     :@@%.     -@@#     =@@+                                                  
       #@@@@@@@@..@@%.     :@@%.     -@@#     =@@+                                                  
       @@*   +@@:.@@%.     :@@%.     -@@@%%%%==@@%%%%%-                                             
      :%%-   :%%+.%%#.     :%%#.     -%%%%%%%=-%%%%%%%=                                             
      ....    ... ...    .:..   ....    .:..    ....  ...      .....     .....        .:..          
      :@@*   .@@-:@@%..=@@@@@%. =@@* .+@@@@@@: :@@@@. +@@:     %@@@@@@*..@@@@@@@#. .*@@@@@@:        
       %@@.  +@@.:@@%.=@@#.:@@%.=@@* +@@#.:@@%.:@@@@= +@@:     %@@::*@@*.@@@::#@@* =@@*..@@@.       
       *@@-  %@%.:@@%.+@@+  #%%.=@@* *@@-  %@@.:@@@@# +@@:     %@@. .@@%.@@%. .@@# *@@: .#@@:       
       =@@* :@@* :@@%.:@@@:     =@@* *@@-  %@@.:@@#@@-+@@:     %@@. .@@%.@@%. .@@* *@@: .#@@:       
       :@@%.=@@- :@@%. .%@@%:   =@@* *@@-  %@@.:@@*+@@*@@:     %@@..+@@*.@@@#%@@%. *@@: .#@@:       
        @@@.*@@. :@@%.   -@@@#. =@@* *@@-  %@@.:@@*.@@%@@:     %@@@@@@#..@@@@@@@%. *@@: .#@@:       
        +@@:#@*  :@@%.     +@@#.=@@* *@@-  %@@.:@@* +@@@@:     %@@:..   .@@%. :@@* *@@: .#@@:       
        .@@+@@=  :@@%.*@@: .@@@.=@@* *@@-  %@@.:@@* :@@@@:     %@@.     .@@%. .@@# *@@: .#@@:       
        .%@@@@:  :@@%.=@@#=*@@%.=@@* =@@%=+@@%.:@@*  +@@@:     %@@.     .@@%. .@@# -@@%=+@@@.       
        .#@@@@.  :@@%. -@@@@@*. =@@*  -@@@@@#. :@@*  .@@@:     %@@.     .@@%. .@@%. =%@@@@#.        
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
    """)
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
    """
    This function prompts the user to input gender, age group, income bracket, and likelihood 
    of purchasing on a 0-10 scale. It validates the inputs and appends the data to a Google Sheets 
    document named "ProductSurvey". Finally, it confirms successful insertion and prompts the user 
    to press enter to return to the main menu.
    """
    print("\nInsert Data - Please provide the following information:\n")
    print(Color.UNDERLINE + "Choose Gender:\n" + Color.END)

    gender_choices = {'M': 'Male', 'F': 'Female'}
    gender_input = input( "Enter the gender (M for Male, F for Female: ").strip().upper()
    print()
    while gender_input not in gender_choices:
        print(Color.RED + "Invalid choice. Please choose either 'M' or 'F'.\n" + Color.END)
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
        print(Color.RED + "Invalid choice. Please choose a number between 1 and 6." + Color.END)
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
        print(Color.RED + "Invalid choice. Please choose a number between 1 and 5.\n" + Color.END)
        income_bracket_input = input("Enter the number corresponding to the income bracket: ").strip()
    income_bracket = income_bracket_choices[income_bracket_input]

    print(Color.UNDERLINE + "\nEnter the likelihood of purchasing (0-10 scale):\n" + Color.END)
    likelihood_input = input("Enter a number between 0 and 10: ").strip()
    print()
    while not likelihood_input.isdigit() or int(likelihood_input) < 0 or int(likelihood_input) > 10:
        print(Color.RED + "Invalid input. Please enter a number between 0 and 10." + Color.END)
        likelihood_input = input("\nEnter a number between 0 and 10: ").strip()
        print()
    likelihood = int(likelihood_input)

    sheet = GSPREAD_CLIENT.open('ProductSurvey')
    input_data_worksheet = sheet.worksheet('Input data')
    input_data_worksheet.append_row([gender, age_group, income_bracket, likelihood])
    print(Color.GREEN + "Data has been successfully inserted into the spreadsheet.\n" + Color.END)
    
    press_enter_to_main_menu()


# Extract data menu
def extract_analyzed_data():
    """
    This function provides a menu for extracting analyzed data from the "ProductSurvey" Google Sheets 
    document. Users can choose various criteria such as gender, age group, income bracket, or combinations 
    thereof to retrieve relevant information.
    """
    clear_screen()
    print()
    print("Extract Analyzed Data:\n")
    print(Color.UNDERLINE + "Choose one of the following options:" + Color.END)
    print()
    print("1. Search by Gender")
    print("2. Search by Age Group")
    print("3. Search by Income Bracket")
    print("4. Combine Gender and Age Group")
    print("5. Combine Gender and Income Bracket")
    print("6. Combine Age Group and Income Bracket")
    print("7. Create Persona (combination of gender, age group, and income bracket)")
    print("8. Return to Main Menu\n")

    choice = input("Enter your choice: ")
    print() 

    if choice == '1':
        # Search by Gender
        search_by_gender()
    elif choice == '2':
        # Search by Age Group
        search_by_age_group()
    elif choice == '3':
        # Search by Income Bracket
        search_by_income_bracket()
    elif choice == '4':
        # Combine Gender and Age Group
        combine_gender_and_age_group()
    elif choice == '5':
        # Combine Gender and Income Bracket
        combine_gender_and_income_bracket()
    elif choice == '6':
        # Combine Age Group and Income Bracket
        combine_age_group_and_income_bracket()
    elif choice == '7':
        # Create Persona (combination of gender, age group, and income bracket)
        create_persona()
    elif choice == '8':
        return
    else:
        print(Color.RED + "\nInvalid choice. Please try again." + Color.END)


# Search by Gender
def search_by_gender():
    """
    Searches for the likelihood of purchase based on gender criteria provided by the user (Male or Female).
    """
    while True:
        gender_input = input("Enter the gender (M for Male, F for Female): ").strip().upper()
        
        if gender_input == 'M':
            search_criteria = 'Male'
            break
        elif gender_input == 'F':
            search_criteria = 'Female'
            break
        else:
            print(Color.RED + "\nInvalid input. Please enter 'M' for Male or 'F' for Female.\n" + Color.END)
    
    likelihood_gender = calculate_likelihood_gender(search_criteria)
    
    if likelihood_gender is not None:
        print()
        print(Color.GREEN + f"Likelihood of purchase for {search_criteria} is {likelihood_gender:.2f}%\n" + Color.END)
    else:
        print(Color.RED + "\nInvalid gender criteria. Please choose 'Male' or 'Female'.\n" + Color.END)
    
    press_enter_to_extract_data_menu()


# Search by Age Group
def search_by_age_group():
    """
    Searches for the likelihood of purchase based on the selected age group.
    """
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
        print(Color.RED + "Invalid choice. Please choose a number between 1 and 6.\n" + Color.END)
        age_group_input = input("Enter the number corresponding to the age group: ").strip()
        print()
    age_group = age_group_choices[age_group_input]
    likelihood_age_group = calculate_likelihood_age_group(age_group)
    print(Color.GREEN + f"Likelihood of purchase for age group {age_group} is {likelihood_age_group:.2f}%\n" + Color.END)
    press_enter_to_extract_data_menu()


# Search by Income Bracket
def search_by_income_bracket():
    """
    Searches for the likelihood of purchase based on the selected income bracket.
    """
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
        print(Color.RED + "Invalid choice. Please choose a number between 1 and 5.\n" + Color.END)
        income_bracket_input = input("Enter the number corresponding to the income bracket: ").strip()
        print()
    income_bracket = income_bracket_choices[income_bracket_input]

    likelihood_income_bracket = calculate_likelihood_income_bracket(income_bracket)
    print(Color.GREEN + f"Likelihood of purchase for customers in the income bracket {income_bracket} is {likelihood_income_bracket:.2f}%.\n" + Color.END)
    press_enter_to_extract_data_menu()


# Combine Gender and Age Group
def combine_gender_and_age_group():
    """
    Searches for the likelihood of purchase based on the combination of gender and age group provided by the user.
    """
    gender = None
    while gender not in ['Male', 'Female']:
        gender_input = input("Enter the gender (M for Male, F for Female): ").strip().upper()
        
        if gender_input == 'M':
            gender = 'Male'
        elif gender_input == 'F':
            gender = 'Female'
        else:
            print(Color.RED + "\nInvalid input. Please enter 'M' for Male or 'F' for Female.\n" + Color.END)
    
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
        print(Color.RED + "Invalid choice. Please choose a number between 1 and 6.\n" + Color.END)
        age_group_input = input("Enter the number corresponding to the age group: ").strip()
        print()
    age_group = age_group_choices[age_group_input]

    likelihood_percentage = calculate_likelihood_gender_and_age_group(gender, age_group)

    if likelihood_percentage is not None:
        print(Color.GREEN + f"Likelihood of purchase for {gender} and {age_group} is {likelihood_percentage:.2f}%\n" + Color.END)
    else:
        print(Color.RED + "\nNo data found for the specified combination.\n" + Color.END)

    press_enter_to_extract_data_menu()


# Combine Gender and Income Bracket
def combine_gender_and_income_bracket():
    """
    Searches for the likelihood of purchase based on the combination of gender and income bracket provided by the user.
    """
    gender = None
    while gender not in ['Male', 'Female']:
        gender_input = input("Enter the gender (M for Male, F for Female): ").strip().upper()
        
        if gender_input == 'M':
            gender = 'Male'
        elif gender_input == 'F':
            gender = 'Female'
        else:
            print(Color.RED + "\nInvalid input. Please enter 'M' for Male or 'F' for Female.\n" + Color.END)
    
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
        print(Color.RED + "Invalid choice. Please choose a number between 1 and 5.\n" + Color.END)
        income_bracket_input = input("Enter the number corresponding to the income bracket: ").strip()
        print()
    income_bracket = income_bracket_choices[income_bracket_input]

    likelihood_percentage = calculate_likelihood_gender_and_income_bracket(gender, income_bracket)

    if likelihood_percentage is not None:
        print(Color.GREEN + f"Likelihood of purchase for {gender} and {income_bracket} is {likelihood_percentage:.2f}%\n" + Color.END)
    else:
        print(Color.RED + "\nNo data found for the specified combination.\n" + Color.END)

    press_enter_to_extract_data_menu()


# Combine Age Group and Income Bracket
def combine_age_group_and_income_bracket():
    """
    Searches for the likelihood of purchase based on the combination of age group and income bracket provided by the user.
    """
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
        print(Color.RED + "Invalid choice. Please choose a number between 1 and 6.\n" + Color.END)
        age_group_input = input("Enter the number corresponding to the age group: ").strip()
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
        print(Color.RED + "Invalid choice. Please choose a number between 1 and 5.\n" + Color.END)
        income_bracket_input = input("Enter the number corresponding to the income bracket: ").strip()
        print()
    income_bracket = income_bracket_choices[income_bracket_input]

    likelihood_percentage = calculate_likelihood_age_group_and_income_bracket(age_group, income_bracket)

    if likelihood_percentage is not None:
        print(Color.GREEN + f"Likelihood of purchase for {age_group} and {income_bracket} is {likelihood_percentage:.2f}%\n" + Color.END)
    else:
        print(Color.RED + "\nNo data found for the specified combination.\n" + Color.END)

    press_enter_to_extract_data_menu()


# Calculate likelihood for Age Group and Income Bracket
def calculate_likelihood_age_group_and_income_bracket(age_group, income_bracket):
    """
    Searches for the likelihood of purchase based on the combination of age group and income bracket provided by the user.
    """
    input_data_worksheet = SHEET.worksheet('Input data')
    analyzed_data = input_data_worksheet.get_all_records()

    likelihood_values = [int(str(record.get('Likelihood', 0))) for record in analyzed_data if
                         record.get('Age Group') == age_group and record.get('Income Bracket') == income_bracket and
                         str(record.get('Likelihood', 0)).isdigit()]

    if not likelihood_values:
        return 0

    mean_likelihood = statistics.mean(likelihood_values)
    mean_likelihood_percent = (mean_likelihood / 10) * 100

    return mean_likelihood_percent

# Create Persona (combination of gender, age group, and income bracket)
def create_persona():
    """
    Allows users to create a persona by specifying gender, age group, and income bracket, and then 
    calculates the likelihood of purchase for that persona.
    """
    print(Color.UNDERLINE + "\nChoose Gender:\n" + Color.END)
    gender_input = input("Enter the gender (M for Male, F for Female): ").strip().upper()
    print()
    while gender_input not in ['M', 'F']:
        print(Color.RED + "Invalid choice. Please choose either 'M' or 'F'." + Color.END)
        print()
        gender_input = input("Enter the gender (M for Male, F for Female): ").strip().upper()
    gender = 'Male' if gender_input == 'M' else 'Female' 

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
        print(Color.RED + "Invalid choice. Please choose a number between 1 and 6." + Color.END)
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
        print(Color.RED + "Invalid choice. Please choose a number between 1 and 5." + Color.END)
        income_bracket_input = input("\nEnter the number corresponding to the income bracket: ").strip()
        print()
    income_bracket = income_bracket_choices[income_bracket_input]

    persona = {'Gender': gender, 'Age Group': age_group, 'Income Bracket': income_bracket}
    likelihood_percentage = calculate_likelihood_persona(persona)
    if likelihood_percentage is not None:
        formatted_persona = ", ".join([f"{key}: {value}" for key, value in persona.items()])
        print(Color.GREEN + f"Likelihood of purchase for persona {formatted_persona} is {likelihood_percentage}\n" + Color.END)
        while True:
            store_option = input("Do you want to store the search results? (Y/N): ").strip().lower()
            if store_option == 'y' or store_option == 'yes':
                store_search_result(persona, likelihood_percentage)
                print(Color.GREEN + "\nSearch results stored successfully.\n" + Color.END)
                break
            elif store_option == 'n' or store_option == 'no':
                print(Color.RED + "\nSearch results not stored.\n" + Color.END)
                break
            else:
                print(Color.RED + "\nInvalid choice. Please enter 'Y' or 'N'.\n" + Color.END)
    else:
        print(Color.RED + "\nCould not calculate likelihood for the persona.\n" + Color.END)

    press_enter_to_extract_data_menu()


# Calculate likelihood for Gender and Income Bracket
def calculate_likelihood_gender_and_income_bracket(gender, income_bracket):
    """
    Calculates the likelihood of purchase based on the combination of gender and income bracket.
    """
    input_data_worksheet = SHEET.worksheet('Input data')
    analyzed_data = input_data_worksheet.get_all_records()

    likelihood_values = [int(str(record.get('Likelihood', 0))) for record in analyzed_data if
                         record.get('Gender') == gender and record.get('Income Bracket') == income_bracket and
                         str(record.get('Likelihood', 0)).isdigit()]

    if not likelihood_values:
        return 0

    mean_likelihood = statistics.mean(likelihood_values)
    mean_likelihood_percent = (mean_likelihood / 10) * 100

    return mean_likelihood_percent


# Calculate likelihood for Gender and Age Group
def calculate_likelihood_gender_and_age_group(gender, age_group):
    """
    Calculates the likelihood of purchase based on the combination of gender and age group.
    """
    input_data_worksheet = SHEET.worksheet('Input data')
    analyzed_data = input_data_worksheet.get_all_records()

    likelihood_values = [int(str(record.get('Likelihood', 0))) for record in analyzed_data if
                         record.get('Gender') == gender and record.get('Age Group') == age_group and
                         str(record.get('Likelihood', 0)).isdigit()]

    if not likelihood_values:
        return 0

    mean_likelihood = statistics.mean(likelihood_values)
    mean_likelihood_percent = (mean_likelihood / 10) * 100

    return mean_likelihood_percent


# Calculate likelihood for Age Group and Income Bracket
def calculate_likelihood_age_group_and_income_bracket(age_group, income_bracket):
    """
    Calculates the likelihood of purchase based on the combination of age group and income bracket.
    """
    input_data_worksheet = SHEET.worksheet('Input data')
    analyzed_data = input_data_worksheet.get_all_records()

    likelihood_values = [int(str(record.get('Likelihood', 0))) for record in analyzed_data if
                         record.get('Age Group') == age_group and record.get('Income Bracket') == income_bracket and
                         str(record.get('Likelihood', 0)).isdigit()]

    if not likelihood_values:
        return 0

    mean_likelihood = statistics.mean(likelihood_values)
    mean_likelihood_percent = (mean_likelihood / 10) * 100

    return mean_likelihood_percent


# Store search result
def store_search_result(persona, likelihood_percentage):
    """
    Stores the search results of a persona along with its likelihood of purchase.
    """
    sheet = GSPREAD_CLIENT.open('ProductSurvey')
    stored_search_worksheet = sheet.worksheet('Stored last search')
    stored_search_worksheet.append_row([persona['Gender'], persona['Age Group'], persona['Income Bracket'], likelihood_percentage])


# Calculate likelihood in percentage
def calculate_likelihood_gender(search_criteria):
    """
    Calculates the likelihood of purchase based on gender criteria.
    """
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

    if search_criteria == 'Male':
        return male_likelihood_percentage
    elif search_criteria == 'Female':
        return female_likelihood_percentage
    else:
        return None


# Calculate age group
def calculate_likelihood_age_group(age_group):
    """
    Calculates the likelihood of purchase based on the selected age group.
    """
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
    """
    Calculates the likelihood of purchase based on the selected income bracket.
    """
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
    """
    Calculates the likelihood of purchase for a specified persona based on gender, age group, and income bracket.
    """
    input_data_worksheet = SHEET.worksheet('Input data')
    analyzed_data = input_data_worksheet.get_all_records()
    
    matching_records = [record for record in analyzed_data if all(key != 'Likelihood' and record.get(key) == value for key, value in persona.items())]

    if not matching_records:
        return None  

    total_records = len(matching_records)
    total_likelihood = sum(record.get('Likelihood', 0) for record in matching_records)

    likelihood_percentage = (total_likelihood / (total_records * 10)) * 100
    likelihood_percentage = round(likelihood_percentage, 2)
    likelihood_percentage = f"{likelihood_percentage}%"

    return likelihood_percentage


# View stored data menu
def view_stored_data():
    """
    Provides a menu for viewing stored search data, including options to view the last search persona or all stored search personas.
    """
    clear_screen()
    print("\nView Stored Data:")
    print()
    print(Color.UNDERLINE + "Choose one of the following options:\n" + Color.END)
    print("1. View Last Search Persona")
    print("2. View All Stored Search Personas")
    print("3. Return to Main Menu\n")

    choice = input("Enter your choice: ")
    print()

    if choice == '1':
        view_last_search_persona()
    elif choice == '2':
        view_all_stored_search_personas()
    elif choice == '3':
        return
    else:
        print(Color.RED + "\nInvalid choice. Please try again.\n" + Color.END)


# View last persona
def view_last_search_persona():
    """
    Displays the details of the last searched persona.
    """
    sheet = GSPREAD_CLIENT.open('ProductSurvey')
    stored_search_worksheet = sheet.worksheet('Stored last search')
    all_stored_search_personas = stored_search_worksheet.get_all_records()

    if all_stored_search_personas:
        last_search_persona = all_stored_search_personas[-1] 
        print(Color.UNDERLINE + "\nLast Search Persona:\n" + Color.END)
        for key, value in last_search_persona.items():
            print(Color.GREEN + f"{key}: {value}" + Color.END)
    else:
        print(Color.RED + "\nNo available data\n" + Color.END)

    print()
    press_enter_to_stored_data_menu()


# View all personas
def view_all_stored_search_personas():
    """
    Displays details of all stored search personas.
    """
    sheet = GSPREAD_CLIENT.open('ProductSurvey')
    stored_search_worksheet = sheet.worksheet('Stored last search')
    all_stored_search_personas = stored_search_worksheet.get_all_records()

    print(Color.UNDERLINE + "\nAll Stored Search Personas:\n" + Color.END)
    if all_stored_search_personas:
        for persona in all_stored_search_personas:
            for key, value in persona.items():
                print(Color.GREEN + f"{key}: {value}" + Color.END)
            print()
    else:
        print(Color.RED + "\nNo available data\n" + Color.END)
    press_enter_to_stored_data_menu()


# Return to main menu by pressing enter
def press_enter_to_main_menu():
    """
    Helper functions to prompt the user to press Enter to return to the main menu.
    """
    input("Press Enter to return to the main menu...")
    main()


# Return to extract menu by pressing enter
def press_enter_to_extract_data_menu():
    """
    Helper functions to prompt the user to press Enter to return to the extract data menu.
    """
    input("Press Enter to return to the extract data menu...")
    extract_analyzed_data()


# Return to stored menu by pressing enter
def press_enter_to_stored_data_menu():
    """
    Helper functions to prompt the user to press Enter to return to the stored data menu.
    """
    input("Press Enter to return to the stored data menu...")
    view_stored_data()


# clear screen
def clear_screen():
    """
    Clears the terminal to give the user a fresh start
    """
    os.system('cls' if os.name == 'nt' else 'clear')


#Main function
def main():
    """
    Main functions.
    """
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
            print("Exiting the program...")
            print()
            break
        else:
            print(Color.RED + "Invalid choice. Please try again." + Color.END)

if __name__ == "__main__":
    main()