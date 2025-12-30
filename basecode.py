import random
# All type matchups stored in one place
MATCHUPS = {
  "Normal": {
    "Fighting": "Fighting beats normal! You lose.",
    "Rock": "Rock resists normal! You lose.",
    "Steel": "Steel resists normal! You lose."
  },
  "Fire": {
    "Grass": "Fire burns grass! You win!",
    "Ice": "Fire melts ice! You win!",
    "Bug": "Fire burns bugs! You win!",
    "Steel": "Fire melts steel! You win!",
    "Fairy": "Fire disrupts nature! You win!",
    "Water": "Water puts out fire! You lose.",
    "Ground": "Earth suffocates fire! You lose.",
    "Rock": "Rocks suffocate fire! You lose.",
    "Dragon": "Dragons resist the elements! You lose."
  },
  "Water": {
    "Fire": "Water puts out fire! You win!",
    "Ice": "Water melts ice! You win!",
    "Ground": "Water erodes earth! You win!",
    "Rock": "Water erodes rock! You win!",
    "Steel": "Water rusts steel! You win!",
    "Grass": "Grass absorbs water! You lose.",
    "Electric": "Water conducts electricity! You lose.",
    "Dragon": "Dragons resist the elements! You lose."
  },
  "Grass":
  {
    "Water": "Grass absorbs water! You win!",
    "Electric": "Grass resists electricity! You win!",
    "Ground": "Grass absorbs earth nutrients! You win!",
    "Rock": "Plants break rock! You win!",
    "Fire": "Fire burns grass! You lose.",
    "Ice": "Ice freezes grass! You lose.",
    "Poison": "Poison poisons grass! You lose.",
    "Flying": "Birds eat plants! You lose.",
    "Bug": "Bugs eat plants! You lose.",
    "Dragon": "Dragons resist the elements! You lose.",
    "Steel": "Steel resists grass! You lose."
  },
  "Electric":
  {
    "Water": "Water conducts electricity! You win!",
    "Flying": "Thunder strikes down birds! You win!",
    "Steel": "Metal conducts electricity! You win!",
    "Grass": "Grass resists electricity! You lose.",
    "Ground": "Earth dispels electricity! You lose.",
    "Dragon": "Dragons resist the elements! You lose."
  },
  "Ice":
  {
    "Grass": "Ice freezes grass! You win!",
    "Ground": "Ice freezes the earth! You win!",
    "Flying": "Ice freezes birds! You win!",
    "Dragon": "Ice freezes dragons! You win!",
    "Fire": "Fire melts ice! You lose.",
    "Water": "Water melts ice! You lose.",
    "Fighting": "Fighting shatters ice! You lose.",
    "Rock": "Rock shatters ice! You lose.",
    "Steel": "Steel shatters ice! You lose."
  },
  "Fighting":
  {
    "Normal": "Fighting beats normal! You win!",
    "Ice": "Fighting shatters ice! You win!",
    "Rock": "Fighting shatters rock! You win!",
    "Dark": "Good defeats evil! You win!",
    "Steel": "Fighting shatters steel! You win!",
    "Flying": "Birds avoid fighting! You lose.",
    "Psychic": "Brains over brawn! You lose.",
    "Ghost": "Fighting can't touch ghosts! You lose.",
    "Fairy": "Fairies confound fighting! You lose."
  },
  "Poison":
  {
    "Grass": "Poison poisons grass! You win!",
    "Fighting": "Poison weakens fighting! You win!",
    "Bug": "Pesticides kill bugs! You win!",
    "Fairy": "Poison disrupts nature! You win!",
    "Ground": "Earth can't be poisoned! You lose.",
    "Psychic": "Psychics dispel poison! You lose.",
    "Rock": "Rocks can't be poisoned! You lose.",
    "Ghost": "Ghosts can't be poisoned! You lose.",
    "Steel": "Steel can't be poisoned! You lose."
  },
  "Ground":
  {
    "Fire": "Earth suffocates fire! You win!",
    "Electric": "Earth dispels electricity! You win!",
    "Poison": "Earth can't be poisoned! You win!",
    "Rock": "Earth erodes rock! You win!",
    "Steel": "Earth erodes steel! You win!",
    "Water": "Water erodes earth! You lose.",
    "Grass": "Grass absorbs earth nutrients! You lose.",
    "Ice": "Ice freezes the earth! You lose.",
    "Flying": "Earth can't touch flying objects! You lose.",
    "Bug": "Bugs burrow in the dirt! You lose."
  },
  "Flying":
  {
    "Grass": "Birds eat plants! You win!",
    "Fighting": "Birds avoid fighting! You win!",
    "Ground": "Earth can't touch flying objects! You win!",
    "Bug": "Birds eat bugs! You win!",
    "Electric": "Thunder strikes down birds! You lose.",
    "Ice": "Ice freezes birds! You lose.",
    "Rock": "Rocks strike down birds! You lose.",
    "Steel": "Steel resists wind and birds! You lose."
  },
  "Psychic":
  {
    "Fighting": "Brains over brawn! You win!",
    "Poison": "Psychics dispel poison! You win!",
    "Bug": "Psychics fear bugs! You lose.",
    "Ghost": "Psychics fear ghosts! You lose.",
    "Dark": "Psychics fear the dark! You lose.",
    "Steel": "Psychics can't see through steel! You lose."
  },
  "Bug":
  {
    "Grass": "Bugs eat plants! You win!",
    "Ground": "Bugs burrow in the dirt! You win!",
    "Psychic": "Psychics fear bugs! You win!",
    "Dark": "Bugs see in the dark! You win!",
    "Fire": "Fire burns bugs! You lose.",
    "Poison": "Pesticides kill bugs! You lose.",
    "Flying": "Birds eat bugs! You lose.",
    "Rock": "Rocks squish bugs! You lose.",
    "Ghost": "Ghosts aren't bothered by bugs! You lose.",
    "Steel": "Steel resists bugs! You lose.",
    "Fairy": "Fairies are friends with bugs! You lose."
  },
  "Rock":
  {
    "Normal": "Rock resists normal! You win!",
    "Fire": "Rocks suffocate fire! You win!",
    "Ice": "Rock shatters ice! You win!",
    "Poison": "Rock can't be poisoned! You win!",
    "Flying": "Rocks strike down birds! You win!",
    "Bug": "Rocks squish bugs! You win!",
    "Water": "Water erodes rock! You lose.",
    "Grass": "Plants break rock! You lose.",
    "Fighting": "Fighting shatters rock! You lose.",
    "Ground": "Earth erodes rock! You lose.",
    "Steel": "Steel breaks rock! You lose."
  },
  "Ghost":
  {
    "Fighting": "Fighting can't touch ghosts! You win!",
    "Poison": "Ghosts can't be poisoned! You win!",
    "Psychic": "Psychics fear ghosts! You win!",
    "Bug": "Ghosts aren't bothered by bugs! You win!",
    "Dark": "Darkness corrupts ghosts! You lose."
  },
  "Dragon":
  {
    "Fire": "Dragons resist the elements! You win!",
    "Water": "Dragons resist the elements! You win!",
    "Electric": "Dragons resist the elements! You win!",
    "Grass": "Dragons resist the elements! You win!",
    "Ice": "Ice freezes dragons! You lose.",
    "Steel": "Armored knights slay dragons! You lose.",
    "Fairy": "Fairy tales end with dragons slain! You lose."
  },
  "Dark":
  {
    "Psychic": "Psychics fear the dark! You win!",
    "Ghost": "Darkness corrupts ghosts! You win!",
    "Fighting": "Good defeats evil! You lose.",
    "Bug": "Bugs see in the dark! You lose.",
    "Fairy": "Fairy tales end with evil vanquished! You lose."
  },
  "Steel":
  {
    "Normal": "Steel resists normal! You win!",
    "Grass": "Steel resists grass! You win!",
    "Ice": "Steel shatters ice! You win!",
    "Poison": "Steel can't be poisoned! You win!",
    "Flying": "Steel resists wind and birds! You win!",
    "Psychic": "Psychics can't see through steel! You win!",
    "Bug": "Steel resists bugs! You win!",
    "Rock": "Steel breaks rock! You win!",
    "Dragon": "Armored knights slay dragons! You win!",
    "Fairy": "Iron weakens fairies! You win!",
    "Fire": "Fire melts steel! You lose.",
    "Water": "Water rusts steel! You lose.",
    "Electric": "Metal conducts electricity! You lose.",
    "Fighting": "Fighting shatters steel! You lose.",
    "Ground": "Earth erodes steel! You win!"
  },
  "Fairy":
  {
    "Fighting": "Fairies confound fighting! You win!",
    "Bug": "Fairies are friends with bugs! You win!",
    "Dragon": "Fairy tales end with dragons slain! You win!",
    "Dark": "Fairy tales end with evil vanquished! You win!",
    "Fire": "Fire disrupts nature! You lose.",
    "Poison": "Poison disrupts nature! You win!",
    "Steel": "Iron weakens fairies! You win!"
  }
}

POKEMON_TYPES = list(MATCHUPS.keys())
def get_choices():
  player_choice = input("Enter a Pokémon type: ").capitalize() # Player input code. Allows you to put in any variable.
  computer_choice = random.choice(POKEMON_TYPES) # Computer randomises types.
  return player_choice, computer_choice

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player not in MATCHUPS:
    return "Invalid choice."
    
  if player == computer:
    return "Neutral matchup! It's a tie!"
    
  if computer in MATCHUPS[player]:
    return MATCHUPS[player][computer]
    
  return "Neutral matchup! It's a tie!"
  
player, computer = get_choices()
print(check_win(player, computer))
