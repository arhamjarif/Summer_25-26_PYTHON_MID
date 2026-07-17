import os.path,json, function, Instance_methods

def save(user_class:object):
    json_data = user_class.__dict__
    with open('info.json') as file:
        save_file = json.load(file)
    save_file[user_class.username] = json_data
    with open('info.json', 'wt') as file:
        json.dump(save_file,file)
    print('Saved successfully.')

def delete_user(file_data):
    users = list(file_data.keys())
    if len(users) == 0:
        print('No users to delete')
        return
    print('Available users:')
    iterator = 1
    for user in users:
        print(f'{iterator}. {user}')
        iterator += 1
    while True:
        try:
            choice = int(input('Select user to delete: '))
            if 1 <= choice <= iterator:
                del file_data[users[choice-1]]
                with open('info.json') as file:
                    save_file = json.load(file)
                del save_file[users[choice-1]]
                with open('info.json','wt') as file:
                    json.dump(save_file,file)
                print(f'Successfully deleted {users[choice-1]}')
                break
            print('Invalid input. Please try again.')
        except Exception:
            print('Invalid input. Please try again.')
if not os.path.exists('info.json'):
    with open('info.json','w') as file:
        empty = {}
        json.dump(empty,file)

try:
    with open('info.json') as file:
        file_data = json.load(file)
        print('========== WELCOME ==========')
        users = list(file_data.keys())
        print('Available users:')
        iterator = 1
        for user in users:
            print(f'{iterator}. {user}')
            iterator += 1
        print(f'{iterator}. New user')
        while True:
            try:
                selected_user = int(input('Select user: '))
                if 0 < selected_user <= (len(users)+1):
                    break
                print('Invalid input. Please try again.')
            except Exception:
                print('Invalid input. Please try again.')
        if selected_user <= len(users):
            info = file_data[users[selected_user-1]]
            user_class  = Instance_methods.User(info["username"])
            user_class.balance = info["balance"]
            user_class.budget  = info["budget"]
            user_class.income  = info["income"]
            user_class.expense = info["expense"]
        else:
            
            username = input('Enter username: ')
            user_class = Instance_methods.User(username)
            
        while True:
            print('\n\n========== BUDGET TRACKER ==========')
            print(f'User: {user_class.username}')
            print(f'Balance: {user_class.balance} BDT')
            print(f'Budget Limit: {user_class.budget} BDT\n\n')
            remaining = user_class.budget - user_class.total_expense()
            if remaining <0:
                print(f"  * WARNING: Already over budget by {abs(remaining):.2f} BDT!")
            else:
                print(f"  * {remaining:.2f} BDT remaining.")
            print('1. Add Entry\n2. Delete Entry\n3. View History\n4. Set Budget\n5. Search by Category\n6. Statistics\n7. Save \n8. Delete user\n9. Quit\n')
            choice = input('Select option: ')
            match choice:
                case '1':
                    user_class.add_entry()
                case '2':
                    user_class.delete_entry()
                case '3':
                    function.view_history(user_class)
                case '4':
                    function.set_budget(user_class)
                case '5':
                    function.search_by_category(user_class)
                case '6':
                    user_class.show_statistics()
                case '7':
                    save(user_class)
                case '8':
                    delete_user(file_data)
                case '9':
                    break


    
except OSError as e:
    print(f'An error occured {e}')
