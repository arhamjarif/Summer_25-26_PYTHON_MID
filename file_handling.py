import json
def save(user_class:object):
    json_data = user_class.__dict__
    with open('info.json') as file:
        save_file = json.load(file)
    save_file[user_class.username] = json_data
    with open('info.json', 'wt') as file:
        json.dump(save_file,file)
    print('Saved successfully.')

def delete_user():
    with open('info.json') as file:
        file_data = json.load(file)
    users = list(file_data.keys())
    if len(users) == 0:
        print('No users to delete')
        return
    print('Available users:')
    iterator = 1
    for user in users:
        print(f'{iterator}. {user}')
        iterator += 1
    print(f'{iterator}: Back')
    
    while True:
        try:
            choice = int(input('Select user to delete: '))
            if 1 <= choice < iterator:
                del file_data[users[choice-1]]
                with open('info.json') as file:
                    save_file = json.load(file)
                del save_file[users[choice-1]]
                with open('info.json','wt') as file:
                    json.dump(save_file,file)
                print(f'Successfully deleted {users[choice-1]}')
                break
            elif choice == iterator:
                break
            print('Invalid input. Please try again.')
        except Exception:
            print('Invalid input. Please try again.')
