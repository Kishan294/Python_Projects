import Art
from Data import data
import random

def format_data(account):
    ''' Format the account data into printable format. '''
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess, a_followers, b_Followers):
    ''' Take the user and follower counts and return right'''
    if a_followers > b_Followers :
        return guess == 'A'
    else:
        return guess == 'B'

score = 0
print(Art.logo)
account_b = random.choice(data)

game_should_continue = True
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(Art.vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B' ").upper()

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        score += 1
        print(f"You are right! Current Score: {score}. ")
        account_a = account_b
        
    else:
        print(f"Sorry, That is wrong. Final score: {score}")
        game_should_continue = False


