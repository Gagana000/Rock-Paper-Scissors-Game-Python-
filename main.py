import random

# Score variables
computer_wins = 0
user_wins = 0
user_draws = 0
user_loses = 0

options = ['rock', 'paper', 'scissors']

while computer_wins < 3:
    user_guess = input("\nRock, Paper, or Scissors? (r/p/s): ").lower().strip()

    # Convert shorthand input to full words
    if user_guess == 'r':
        user_guess = 'rock'
    elif user_guess == 'p':
        user_guess = 'paper'
    elif user_guess == 's':
        user_guess = 'scissors'

    if user_guess not in options:
        print("❌ Invalid choice. Please enter Rock, Paper, or Scissors.")
        continue

    # Computer's choice
    computer_guess = random.choice(options)

    print(f"\n👉 Your choice: {user_guess.capitalize()}")
    print(f"🤖 Computer chose: {computer_guess.capitalize()}")

    # Determine the result
    if user_guess == computer_guess:
        print("🤝 It's a Draw!")
        user_draws += 1
    elif (user_guess == 'rock' and computer_guess == 'scissors') or \
         (user_guess == 'scissors' and computer_guess == 'paper') or \
         (user_guess == 'paper' and computer_guess == 'rock'):
        print("🎉 You Won!")
        user_wins += 1
    else:
        print("😢 You Lose!")
        computer_wins += 1
        user_loses += 1

    # Check if the computer reached 3 wins
    if computer_wins >= 3:
        print("\n🚨 The computer has won 3 times. Game over!")
        break

    # Ask if the user wants to continue
    keep_going = input("\nDo you want to play again? (y/n): ").lower().strip()
    if keep_going != 'y':
        break

# Display final scores
print("\n🏁 Game Over! Here are your final scores:")
print(f"✅ Wins: {user_wins}")
print(f"❌ Losses: {user_loses}")
print(f"🤝 Draws: {user_draws}")
print("Thanks for playing! 🎮")    