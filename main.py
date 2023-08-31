from data import coffees, resources


def get_user_input():
    """to get the user input, either coffees, report or off or invalid. """
    check_resources()
    if valid_coffees_str() == '':
        return 'out'
    else:
        user_input_in_function = input(f'What do you want? ({valid_coffees_str()}) off/report ').strip().lower()
        if user_input_in_function not in ['espresso', 'latte', 'cappuccino', 'report', 'off']:
            return 'invalid'
        return user_input_in_function


def valid_coffees_str():
    """creates valid coffees string: espresso/latte/cappuccino"""
    valids = ''
    for c in coffees:
        if coffees[c]['availability']:
            valids += f"{c}/"
    return valids[:len(valids) - 1]


def report():
    """reports the amount of resources."""
    for i in resources:
        if i == 'money':
            print(f'{i}: ${resources[i]}')
        else:
            print(f'{i}: {resources[i]}ml')
    return


def check_resources():
    """checks if the resources are enough, if not, switches the coffee availability to False."""
    for i in coffees:
        if coffees[i]['water'] > resources['water'] or coffees[i]['coffee'] > resources['coffee'] or coffees[i]['milk'] > resources['milk']:
            coffees[i]['availability'] = False


def check_money(coffee, coins_list: list):
    """checks if the money is enough or not, if more, returns the change.
    coins list = [quarters, dimes, nickles, pennies]"""
    money = coins_list[0] * 0.25 + coins_list[1] * 0.10 + coins_list[2] * 0.05 + coins_list[3] * 0.01
    if money >= coffees[coffee]['price']:
        change = money - coffees[coffee]['price']
        return [True, change]
    else:
        return [False]


def update_resources(coffee):
    """updates resources after giving a coffee away."""
    resources['water'] -= coffees[coffee]['water']
    resources['coffee'] -= coffees[coffee]['coffee']
    resources['milk'] -= coffees[coffee]['milk']
    resources['money'] += coffees[coffee]['price']


def get_money():
    """gets the number of each coin and returns a list."""
    print('Please insert coins.')
    quarters_in = int(input('Quarters: '))
    dimes_in = int(input('Dimes: '))
    nickles_in = int(input('Nickles: '))
    pennies_in = int(input('Pennies: '))
    return [quarters_in, dimes_in, nickles_in, pennies_in]


while True:
    user_input = get_user_input()
    if user_input == 'off':
        print('Coffee machine shut off.')
        raise SystemExit
    elif user_input == 'out':
        print('Sorry! the machine has no coffees for now.')
        raise SystemExit
    elif user_input == 'invalid':
        print('invalid input! try again.')
    elif user_input == 'report':
        report()
    else:
        coffee_name = user_input
        if coffees[coffee_name]['availability']:
            print(f"{coffee_name} is ${coffees[coffee_name]['price']}")
            coins_taken = get_money()
            money_check_result = check_money(coffee_name, coins_taken)
            if money_check_result[0]:
                if money_check_result[1] != 0:
                    print(f'Here is your ${money_check_result[1]:.2f} change.')
                print(f'Here is your {coffee_name}.')
                update_resources(coffee_name)
            else:
                print('Sorry, money is not enough. refunded.')
        else:
            user_answer = input('Sorry, there is not enough resources. would you want to order something else? ').strip().lower()
            if user_answer == 'yes':
                pass
            else:
                print('Thank you and Sorry... good-bye.')
                raise SystemExit
