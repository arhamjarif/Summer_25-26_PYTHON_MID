import datetime
def get_valid_float(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val <= 0:
                print('Amount must be greater then 0')
                continue
            return val
        except Exception:
            print('Invalid input. Please Enter a number.')

def get_valid_int(prompt, low, high):
    while True:
        try:
            val = int(input(prompt))
            if low <= val <= high:
                return val
            print(f'Please enter a number between {low} and {high}')
        except Exception:
            print('Invalid input. Please Enter a number.')

def get_valid_date(prompt):
    while True:
        date = input(prompt).strip()
        try:
            datetime.datetime.strptime(date, "%d-%m-%Y")
            return date
        except Exception:
            print('Invalid date. Please use DD-MM-YYYY format.')