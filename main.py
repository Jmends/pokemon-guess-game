import requests
import random


def get_random_pokemon():
    base_url = 'https://pokeapi.co/api/v2/'  # API url

    random_id = random.randint(1, 494)  # randomly generates number from 1 to 494. will be ID of pokemon. Used to randomly select Pokemon
    pokemon_response = requests.get(f"{base_url}/pokemon/{random_id}")

    if pokemon_response.status_code == 200:  # status code for the response from the API
        random_data = pokemon_response.json()
        pokemon_name = random_data['name']

        height_dm = random_data['height']
        height_m = height_dm / 10  # Converts the standard units of measurement the api uses to be meters ang kilograms

        weight_hg = random_data['weight']
        weight_kg = weight_hg / 10

        if 1 <= random_id <= 151:  # sets the region based on the id of the Pokemon, ID is randomly generated
            region = "Kanto"
        elif 152 <= random_id <= 251:
            region = "Johto"
        elif 252 <= random_id <= 386:
            region = "Hoenn"
        elif 387 <= random_id <= 493:
            region = "Sinnoh"
        else:
            region = "unknown"

        first_letter = random_data['name'].capitalize()

        facts = [  # a list of facts about the randomly selected Pokemon
            f"First Letter of name: {first_letter[0]}",
            f"Region: {region}",
            f"Height: {height_m:.2f} meters",
            f"Type(s): {', '.join(type_['type']['name'] for type_ in random_data['types'])}",
            f"Weight: {weight_kg:.2f} kg",
            f"Abilities: {', '.join(ability['ability']['name'] for ability in random_data['abilities'])}"
        ]

        return facts, pokemon_name

    else:
        print(f"Failed to retrieve data {pokemon_response.status_code}")
        return None, None


def main_game():
    print("Welcome to the pokemon guessing game!")

    start_game = input("Type y to start the game or n to end: ").lower()
    rounds = 10
    current_round = 0
    score = 0

    print("")
    while start_game == 'y' and current_round < rounds:
        current_round += 1
        print(f"Round {current_round} of {rounds}")

        facts, pokemon_name = get_random_pokemon()

        if facts and pokemon_name:
            guesses = 5
            game_running = True

            while game_running and guesses > 0:
                print(f"\n".join(facts))  # joins the list of facts and prints each one on a new line
                print("")
                guess = input("Guess the pokemon: ").lower()

                if guess == pokemon_name:
                    print("Correct")
                    score += 1
                    break
                else:
                    guesses -= 1
                    print(f"wrong you have {guesses} guesses left")
                    print("")

                    if guesses == 0:
                        print(f"The correct answer was: {pokemon_name}\n")

        if current_round < rounds:
            print("New round starting....")
            print("")
        else:
            print("All rounds complete")
            print(f"Your score: {score}/{rounds}")


main_game()
