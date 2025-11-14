import pandas, configparser, json

class Formatter:
    """
    A class to format user data for Auth0 import specific to Energy Co-op.
    """
    def __init__(self, config_file='config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
    
    def run(self):
        welcome_message = """    ___         __  __    ____     ____                           __     ______                           __  __           
        /   | __  __/ /_/ /_  / __ \   /  _/___ ___  ____  ____  _____/ /_   / ____/___  _________ ___  ____ _/ /_/ /____  _____
        / /| |/ / / / __/ __ \/ / / /   / // __ `__ \/ __ \/ __ \/ ___/ __/  / /_  / __ \/ ___/ __ `__ \/ __ `/ __/ __/ _ \/ ___/
        / ___ / /_/ / /_/ / / / /_/ /  _/ // / / / / / /_/ / /_/ / /  / /_   / __/ / /_/ / /  / / / / / / /_/ / /_/ /_/  __/ /    
        /_/  |_\__,_/\__/_/ /_/\____/  /___/_/ /_/ /_/ .___/\____/_/   \__/  /_/    \____/_/  /_/ /_/ /_/\__,_/\__/\__/\___/_/     
                                                    /_/                                                                            """

        print(welcome_message)

        # Read configuration and setup variables
        start_row = self.config.getint('local', 'start_row')
        first_name_column_index = self.config.getint('local', 'first_name_column_index')
        last_name_column_index = self.config.getint('local', 'last_name_column_index')
        email_column_index = self.config.getint('local', 'email_column_index')
        capacity_column_index = self.config.getint('local', 'capacity_column_index')

        # Get file name
        file_name = input("Enter the name of the file to read: ")

        # Read file in
        content = pandas.read_excel(file_name)

        output = []

        for row in content.itertuples():
            if (start_row <= row.Index):
                first_name = row[first_name_column_index]
                last_name = row[last_name_column_index]
                email = row[email_column_index]
                capacity = row[capacity_column_index]
                print(f"Processed row: First Name: {first_name}, Last Name: {last_name}, Email: {email}, Capacity: {capacity}")

                row_object = {
                    "email": email,
                    "email_verfied": False,
                    "given_name": first_name,
                    "family_name": last_name,
                    "app_metadata": {
                        "ownerships": {
                            "gf-wattage": capacity
                        }
                    }
                }

                output.append(row_object)
                print("-----")

        with open('out.json', 'w') as f:
            json.dump(output, f, indent=4)

        print(f"Processed {len(output)} rows. See 'out.json'.")