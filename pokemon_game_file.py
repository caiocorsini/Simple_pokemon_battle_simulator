import csv   # To manipulate csv files. They work as "save files" for this program.
from prettytable import PrettyTable   # To print information as easy_to_read tables for the user.
import random as r   # It is going to be used in the battle system
import time as t

# Object class that is going to store information about pokémon such as:
# Name, region where it was introduced, typing and base stats
# dfs stands for Defense instead of the usual "def" because in Python "def" is not a valid variable name since it is used to declare functions/methods
class Pokemon:
  def __init__(self, name, region, type1, type2, hp, atk, dfs, spa, spd, spe):
    self.name = name
    self.region = region
    self.type1 = type1
    self.type2 = type2
    self.hp = hp
    self.atk = atk
    self.dfs = dfs
    self.spa = spa
    self.spd = spd
    self.spe = spe



# Object class to store move information. Built simmilarly to the Pokémon class
# Stores name, typing, base power and accuracy. Accuracy is given in percentage.
class Moves:
  def __init__(self, name, type, power, accuracy, category):
    self.name = name
    self.type = type
    self.power = power
    self.accuracy = accuracy
    self.category = category


# Declares Pokémon and move lists which are going to be used and update throughout the program
# It wasn't really needed, but they are used as paramethers for multiple functions so that they don't work like global ariables.
# Lists of objects based on the object classes declared previously
pokemon_list = []
move_list = []



# Stat value verifier function so that I don't need to write the same loop for every single stat.
# Verifies if base stat is between 0 and 256.
# Called by: new_pokemon()
def valid_stat(insert_stat):
  while insert_stat <= 0 or insert_stat > 255:
    if insert_stat <= 0:
      print("No stat can be equal or below 0!")
    elif insert_stat > 255:
      print("No stat can be higher than 255!")
    insert_stat = int(input("Please, type again: "))
  return insert_stat



# Function for inputing new Pokémon
# Called by: menu(), empty_pokemon()
def new_pokemon(pokemon_list):
  print("--------INSERT NEW POKÉMON--------")
  print("")
  x = True
  while x:
    # Inputing basic information about the new Pokémon
    insert_name = input("Write new Pokémon name: ").lower()
    insert_region = input("Write new Pokémon region: ").lower()
    insert_type1 = input("Write new Pokémon primary typing: ").lower()
    valid = check_if_type_is_valid(insert_type1)   # To check whether type exists or not  
    while valid == False:
      print("Such type doesn't exist. Please, type again.")
      insert_type1 = input("Write new Pokémon primary typing: ").lower()
      valid = check_if_type_is_valid(insert_type1)
      
    print("Write new Pokémon secondary typing (if it is a dual-type)")
    insert_type2 = input("If it is a pure type just click enter without typing anything: ").lower()
    valid = check_if_type_is_valid(insert_type2)   # To check whether type exists or not
    while valid == False:
      if insert_type2 == "":
        valid = True
      else:
        print("Such type doesn't exist. Please, type again.")
        insert_type2 = input("Write new Pokémon primary typing: ").lower()
        valid = check_if_type_is_valid(insert_type2)

    # Inputing the base stats of the Pokémon: HP, Attack, Defense, Special Attack, Special Defense and Speed.
    insert_hp = int(input("Insert HP stat: "))
    valid_stat(insert_hp) # To check if the stat is between 0 and 256 or not
    insert_atk = int(input("Insert attack stat: "))
    valid_stat(insert_atk)
    insert_dfs = int(input("Insert defense stat: "))
    valid_stat(insert_dfs)
    insert_spa = int(input("Insert special attack stat: "))
    valid_stat(insert_spa)
    insert_spd = int(input("Insert special defense stat: "))
    valid_stat(insert_spd)
    insert_speed = int(input("Insert speed stat: "))
    valid_stat(insert_speed)

    # Creates a new object based on the information given about the new Pokémon
    # Such object is added to a list of objects representing the Pokémon
    new_pkmn = Pokemon(insert_name, insert_region, insert_type1, insert_type2, insert_hp, insert_atk, insert_dfs, insert_spa, insert_spd, insert_speed)
    pokemon_list.append(new_pkmn)
    print("")
    print("New Pokémon included!!!")

    # Verifies if user wants to add another Pokémon if they want
    print("")
    continuar = input("Insert new Pokémon? Yes or no: ").lower()
    print("")
    while continuar != "yes" and continuar != "y" and continuar != "no" and continuar != "n":
      print("Invalid input! Only accepts 'yes' or 'no' as inputs. Type again.")
      continuar = input("Insert new Pokémon? Yes or no: ").lower()
      continuar = continuar.lower()
      print("")
    if continuar == "no" or continuar == "n":
      x = False
      print("")
  menu()

    



# Function for user to input new moves
# Works in a very similar way as new_pokemon()
# Called by: menu()
def new_move(move_list):
  print("--------INSERT NEW MOVE--------")
  print("")
  # While loop that will keep running until user decides to quit. See the end of the function.
  x = True
  while x:
    # Inputing basic information about the new move
    insert_name = input("Type name of the move: ").lower()
    # I thought about reusing the same function as the one of the base stats, but the messages to the user should be different, so I wrote it here again.
    insert_power = int(input("Insert base power of the move: "))
    while insert_power > 255 or insert_power <= 0:
      if insert_power > 255:
        print("Base power is too high! Move base power cannot be higher than 255.")
      elif insert_power <= 0:
        print("Base power must be higher than 0! Negative numbers are not valid!")
      insert_power = int(input("Insert base power of the move: "))

    # Remember, base accuracy is given in percentages (%)
    insert_accuracy = int(input("Insert base accuracy of the move. in percentage: "))
    while insert_accuracy > 100 or insert_accuracy <= 0:
      if insert_accuracy > 100:
        print("Accuracy is too high! Move accuracy cannot be higher than 100%.")
      elif insert_accuracy <= 0:
        print("Accuracy must be higher than 0! Negative numbers are not valid!")
      insert_accuracy = int(input("Insert accuracy of the move: "))

    insert_type = input("Insert type of the move: ").lower()
    valid = check_if_type_is_valid(insert_type)   # Checks whether type even exists
    while valid == False:
      print("Such type doesn't exist. Please, type again.")
      insert_type = input("Insert type of the move: ").lower()
      valid = check_if_type_is_valid(insert_type)

    insert_category = input("Is your move physical or special? Type either 'physical' or 'special': ").lower()
    insert_category = insert_category.lower()
    while insert_category != "physical" and insert_category != "special":
      print("Invalid input! Type either 'physical' or 'special.")
      insert_category = input("Is your move physical or special: ").lower()

    # Creates new move object based on the information given by the user
    new_move = Moves(insert_name, insert_type, insert_power, insert_accuracy, insert_category)
    move_list.append(new_move)
    
    print("")
    print("New move included!!!")
    print("")

    # Checks if user wants to add more moves
    continuar = input("Insert new move? Yes or no: ").lower()
    print("")
    while continuar != "yes" and continuar != "y" and continuar != "no" and continuar != "n":
      print("Invalid input! Only accepts 'yes' or 'no' as inputs. Type again.")
      continuar = input("Insert new Pokémon? Yes or no: ").lower()
      print("")
    if continuar == "no" or continuar == "n":
      x = False
      print("")
  menu()



# Function that verifies if the inserted type exists in the game
# Returns boolean value
# Called by: new_pokemon(), new_move()
def check_if_type_is_valid(insert_type):
  # List with every single Pokémon type. Used for the verification process.
  valid_types = ["rock", "water", "electric", "grass", "poison", "psychic", "fire", "ground", "dark", "fairy", "flying", "normal", "ghost", "fighting", "steel", "ice", "dragon", "bug"]
  valid = False
  for i in valid_types:
    if i == insert_type:
      valid = True
  return valid



# Function that saves all Pokémon data stored in pokemon_list
# Uses csv Module
# Called by: save()
def pokemon_save(pokemon_list):
  file_name = input("Choose a name for your new Pokémon save file: ")
  with open(file_name+".csv", "w", newline="") as f:
    writer = csv.writer(f)
    for x in pokemon_list:
      writer.writerow([x.name, x.region, x.type1, x.type2, x.hp, x.atk, x.dfs, x.spa, x.spd, x.spe])
  print("File saved!!!")
  print("Saved as: '" + file_name + ".csv'")
  print("")
  return



# Function that saves all move data stored in move_list
# Uses csv Module
# Very similar to pokemon_save
# Called by: save()
def move_save(move_list):
  file_name = input("Choose a name for your move new save file: ")
  with open(file_name+".csv", "w", newline="") as f:
    writer = csv.writer(f)
    for x in move_list:
      writer.writerow([x.name, x.type, x.power, x.accuracy, x.category])
  print("File saved!!!")
  print("Saved as: '" + file_name + ".csv'")
  print("")
  return



# General save function
# It doesn't really save anything, it simply calls the functions actually resposible for saving data, those being: pokemon_save() and move_save()
# Called by: menu()
def save(pokemon_list, move_list):
  print("--------SAVE POKÉMON LIST--------")
  print("")
  print("What do you want to save?")
  print("")
  print("[1] Save Pokémon list only")
  print("[2] Save move list only")
  print("[3] Save both Pokémon and move list")
  print("")
  option = input("Type your option: ")

  # Input as a string instead of integer is easier for the user. Less likely to cause bugs.
  while option != "1" and option != "2" and option != "3":
    print("Invalid input! Please, type a number between 1 and 3.")
    option = input("Type your option: ")
    print("")
  
  if option == "1":
    pokemon_save(pokemon_list)
    menu()
  elif option == "2":
    move_save(move_list)
    menu()
  elif option == "3":
    pokemon_save(pokemon_list)
    move_save(move_list)
    menu()



# Loads Pokémon data
# Data is stored in a CSV file by the save functions. This function reads those files and tanslate each line in a pokemon object.
# Called by: load(), searcher(), empty_pokemon()
def pokemon_load(pokemon_list):
  option = input("Type the name of the Pokémon file you want to load. Do not type '.csv': ")
  pokemon_list.clear() #clear all elements from previous list so that they don't merge
  with open(option+".csv", "r") as save_file:
    reader = csv.reader(save_file, delimiter = ",")
    for row in reader:
      name, region, type1, type2, hp, atk, dfs, spa, spd, spe = [item.strip() for item in row]
      loaded_Pokemon = Pokemon(name, region, type1, type2, int(hp), int(atk), int(dfs), int(spa), int(spd), int(spe))
      pokemon_list.append(loaded_Pokemon)
  print(option + ".csv, loaded successfully!!!")
  print("")



# Loads move data
# Data is stored in a CSV file by the save functions. This function reads those files and tanslate each line in a move object.
# Called by: load(), searcher()
def move_load(move_list):
  option = input("Type the name of the move save file you want to load. Do not type '.csv': ")
  move_list.clear() #clear all elements from previous list so that they don't merge
  with open(option+".csv", "r") as save_file:
    reader = csv.reader(save_file, delimiter = ",")
    for row in reader:
      name, type, power, accuracy, category = [item.strip() for item in row]
      loaded_move = Moves(name, type, int(power), int(accuracy), category)
      move_list.append(loaded_move)
  print(option + ".csv, loaded successfully!!!")
  print("")



# General load function
# It doesn't really load anything but it calls other functions that actually load files
def load(pokemon_list, move_list):
  print("--------LOAD POKÉMON LIST--------")
  print("")
  print("What do you want to load?")
  print("")
  print("[1] Load a Pokémon list")
  print("[2] Load a move list")
  print("[3] Load both a Pokémon and a move list")
  print("")
  option = input("Type your option: ")

  while option != "1" and option != "2" and option != "3":
    print("Invalid input! Please, type a number between 1 and 3.")
    option = input("Type your option: ")
    print("")
  
  if option == "1":
    pokemon_load(pokemon_list)
    menu()
  elif option == "2":
    move_load(move_list)
    menu()
  elif option == "3":
    pokemon_load(pokemon_list)
    move_load(move_list)
    menu()



# Function used when user tries to look for data that doesn't exist.
# Gives 2 options to fill the empty list: by manually including a new Pokémon or by loadind an existing Pokémon CSV file
def empty_pokemon(pokemon_list):
  print("Your Pokémon list is empty.")
  print("Fill it by inserting new Pokémon or by loading an existing file.")
  print("")
  print("[1] Insert new Pokémon")
  print("[2] Load Pokémon data")
  print("")
  option = input("Type your option: ")

  while option != "1" and option != "2":
    print("Invalid input! Please, type a number between 1 and 2.")
    option = input("Type your option: ")
    print("")
  
  if option == "1":
    print("")
    new_pokemon(pokemon_list)
  elif option == "2":
    pokemon_load(pokemon_list)



# Function used when user tries to look for data that doesn't exist.
# Gives 2 options to fill the empty list: by manually including a new move or by loadind an existing move CSV file
def empty_move(move_list):
  print("Your move list is empty.")
  print("Fill it by inserting new moves or by loading an existing file.")
  print("")
  print("[1] Insert new move")
  print("[2] Load move data")
  print("")
      
  option = input("Type your option: ")

  while option != "1" and option != "2":
    print("Invalid input! Please, type a number between 1 and 2.")
    option = input("Type your option: ")
    print("")
    
  if option == "1":
    print("")
    new_move(move_list)
  elif option == "2":
    move_load(move_list)



# This function searches for a specific Pokémon/move by name by iterating through the pokémon/move lists
# Called by: look_pokemon()
def searcher(pokemon_list, move_list):
  print("")
  print("Search for...")
  print("")
  print("[1] Pokémon")
  print("[2] Move")
  print("")
  option = input("Type your option: ")
  
  while option != "1" and option != "2":
    print("Invalid input! Please, type a number between 1 and 2.")
    option = input("Type your option: ")
    print("")
  
  word = input("Type a full name: ")

  # Iterates through list to see if input and Pokémon name matches
  if option == "1":
    if len(pokemon_list) == 0:
      print("You have no Pokémon data.")
      print("Please, insert at least one Pokémon or load a data file.")
      print("")
      empty_pokemon(pokemon_list)
      menu()
    else:
      found_name = False
      for i in pokemon_list:
        if i.name == word:
          print("")
          print("Pokémon found!")
          found_name = True
          print("")
          print("Name: " + i.name)
          print("Region: " + i.region)
          print("Primary type: " + i.type1)
          print("Secondary type: " + i.type2)
          print("")
          print("HP: " + str(i.hp))
          print("Attack: " + str(i.atk))
          print("Defense: " + str(i.dfs))
          print("Special Attack: " + str(i.spa))
          print("Special Defense: " + str(i.spd))
          print("Speed: " + str(i.spe))
          print("Base stat total: " + str(int(i.hp) + int(i.atk) + int(i.dfs) + int(i.spa) + int(i.spd) + int(i.spe)))
          print("")
          menu()
      if found_name == False:
        print("No Pokémon of such name was found!")
        print("")
        menu()

  if option == "2":
    if len(move_list) == 0:
      print("You have no move data.")
      print("Please, insert at least one move or load a data file.")
      print("")
      empty_move(move_list)
      menu()
    else:
      found_move = False
      for i in move_list:
        if i.name == word:
          print("")
          print("Move found!")
          found_move = True
          print("")
          print("Name: " + i.name)
          print("Type: " + i.type)
          print("Base power: " + str(i.power))
          print("Accuracy: " + str(i.accuracy) + "%")
          print("Category: " + i.category + "%")
          print("")
          menu()
      if found_move == False:
        print("No Move of such name was found!")
        print("")
        menu()



# Function that shows Pokémon and move information
# Information is shown to the user via tables from pretytables Module
# Called by: menu()
def look_pokemon(pokemon_list):
  print("--------LOOK FOR POKÉMON--------")
  print("")
  # Submenu
  print("What do you want to do:")
  print("[1] Show all Pokémon - basic info")
  print("[2] Show all Pokémon - stats")
  print("[3] Show all moves")
  print("[4] Search data by name")
  print("")
  option = input("Choose your option by typing a number of the menu: ")
  print("")

  while option != "1" and option != "2" and option != "3" and option != "4":
    print("Invalid input! Please, type a number between 1 and 4.")
    option = input("Choose your option by typing a number of the menu: ")
    print("")
  
  if option == "1":
    show_table = PrettyTable()
    show_table.field_names = ["No.", "Name", "Region", "Type 1", "Type 2"]
    # Table builder
    for i in pokemon_list:
      show_table.add_row([pokemon_list.index(i), i.name, i.region, i.type1, i.type2])
    print(show_table) # Table is printed on the console
    if len(pokemon_list) == 0:
      empty_pokemon(pokemon_list)
    print("")
    menu()

  elif option == "2":
    show_table = PrettyTable()
    show_table.field_names = ["No.", "Name", "HP", "Atk", "Def", "SpA", "SpD", "Spe"]
    for i in pokemon_list:
      show_table.add_row([pokemon_list.index(i), i.name, i.hp, i.atk, i.dfs, i.spa, i.spd, i.spe])
    print(show_table)
    if len(pokemon_list) == 0:
      empty_pokemon(pokemon_list)
    print("")
    menu()

  elif option == "3":
    show_table = PrettyTable()
    show_table.field_names = ["No.", "Name", "type", "Power", "Accuracy", "Category"]
    for i in move_list:
      show_table.add_row([move_list.index(i), i.name, i.type, i.power, str(i.accuracy)+"%", i.category])
    print(show_table)
    if len(move_list) == 0:
      empty_move(move_list)
    print("")
    menu()

  elif option == "4":
    searcher(pokemon_list, move_list)
    



def pkmn1_setup(pokemon_list, move_list, pkmn1_move_list):

  pkmn1 = Pokemon("", "", "", "", 0, 0, 0, 0, 0, 0)
  
  choice = input("Choose your Pokémon. Type its name here: ").lower()
  for i in pokemon_list:
    if i.name == choice:
      hp_stat = (2 * int(i.hp) + 31 + (255//4)) + 110
      atk_stat = (2 * int(i.atk) + 31 + (255//4)) + 5
      dfs_stat = (2 * int(i.dfs) + 31 + (255//4)) + 5
      spa_stat = (2 * int(i.spa) + 31 + (255//4)) + 5
      spd_stat = (2 * int(i.spd) + 31 + (255//4)) + 5
      spe_stat = (2 * int(i.spe) + 31 + (255//4)) + 5
      pkmn1 = Pokemon(i.name, i.region, i.type1, i.type2, hp_stat, atk_stat, dfs_stat, spa_stat, spd_stat, spe_stat)

  for i in range(4):
    move_choice = input("Type the name of a move for your Pokémon to learn: ").lower()
    for j in move_list:
      if j.name == move_choice:
        pkmn1_move_list.append(j)
  return pkmn1



def pkmn2_setup(pokemon_list, move_list, pkmn2_move_list):
  print("Setting up pkmn2")

  pkmn2 = Pokemon("", "", "", "", 0, 0, 0, 0, 0, 0)
  
  rdm_generator = r.randint(0, len(pokemon_list)-1)
  for i in pokemon_list:
    if pokemon_list.index(i) == rdm_generator:
      hp_stat = (2 * int(i.hp) + 31 + (255//4)) + 110
      atk_stat = (2 * int(i.atk) + 31 + (255//4)) + 5
      dfs_stat = (2 * int(i.dfs) + 31 + (255//4)) + 5
      spa_stat = (2 * int(i.spa) + 31 + (255//4)) + 5
      spd_stat = (2 * int(i.spd) + 31 + (255//4)) + 5
      spe_stat = (2 * int(i.spe) + 31 + (255//4)) + 5
      pkmn2 = Pokemon(i.name, i.region, i.type1, i.type2, hp_stat, atk_stat, dfs_stat, spa_stat, spd_stat, spe_stat)


  for w in range(4):
    rdm_generator = r.randint(0, len(move_list)-1)
    for j in move_list:
      if move_list.index(j) == rdm_generator:
        pkmn2_move_list.append(j)
  return pkmn2



#-------- ACTION ---------
def hp_bar(max_hp, current_hp):
  current_percentage = round((100 * current_hp) / max_hp)
  quotient = current_percentage / 5
  print("[", end="")
  if quotient > 0 and quotient < 1:
    print("#", end="")
  elif quotient >= 1:
    for i in range(round(quotient)):
      print("#", end="")
  print("]", end="")



# Critical Hit calculator
def critical_hit():
  rdm_number = r.randint(1, 24)
  if rdm_number == 1:
    t.sleep(1)
    print("CRITICAL HIT!!!")
    return 1.5
  else:
    return 1



def STAB(used_move, user):
  if used_move.type == user.type1 or used_move.type == user.type2:
    return 1.5
  else:
    return 1



def deal_damage(used_move, user, target):
  # Must return amount of damage dealt on the target as an integer
  # Target's current hp will be subtracted with that
  # First, it is going to calculate if the move will miss or not based on its accuracy.
  calculated_accuracy = 100 - used_move.accuracy
  rdm_number = r.randint(1, 100)
  if rdm_number <= calculated_accuracy:
    t.sleep(1)
    print("But it missed...")
    damage = 0
    t.sleep(1)

  else:
    multiplier = type_chart(used_move, user, target)
    if multiplier == 0:
      damage = 0
      t.sleep(1)
      
    else:
      if used_move.category == "physical":
        damage = round((((42 * used_move.power * (user.atk / target.dfs)) / 50) + 2) * ((r.randint(85, 100)) / 100) * multiplier * critical_hit() * STAB(used_move, user))
        t.sleep(1)

      elif used_move.category == "special":
        damage = round((((42 * used_move.power * (user.spa / target.spd)) / 50) + 2) * ((r.randint(85, 100)) / 100) * multiplier * critical_hit() * STAB(used_move, user))
        t.sleep(1)
      
    print(user.name + " dealt " + str(damage) + " damage to " + target.name + "!")
  t.sleep(1)
  return int(damage)



def is_everyone_alive(pkmn1, pkmn2, pkmn1_current_hp, pkmn2_current_hp):
  if pkmn1_current_hp <= 0:
    print("")
    print(pkmn1.name + " is down!")
    t.sleep(1)
    print(pkmn2.name + " won the battle!")
    return False
    
  elif pkmn2_current_hp <= 0:
    print("")
    print(pkmn2.name + " is down!")
    t.sleep(1)
    print(pkmn1.name + " won the battle!")
    return False

  elif pkmn1_current_hp > 0 and pkmn2_current_hp > 0:
    return True
    
  




# This function should return the type effectiveness multiplier
def type_chart(used_move, pkmn1, pkmn2):
  
  # Columns have to follow this pattern ["name_of_defense_type", multipliers]
  # type_column = ["type", 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  # Indexes should match the same type for both attack and defense
  
  normal_column = ["normal", 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
  fire_column = ["fire", 1, 0.5, 2, 1, 0.5, 0.5, 1, 1, 2, 1, 1, 0.5, 2, 1, 1, 1, 0.5, 0.5]
  water_column = ["water", 1, 0.5, 0.5, 2, 2, 0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1]
  electric_column = ["electric", 1, 1, 1, 0.5, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 1, 0.5, 1]
  grass_column = ["grass", 1, 2, 0.5, 0.5, 0.5, 2, 1, 2, 0.5, 2, 1, 2, 1, 1, 1, 1, 1, 1]
  ice_column = ["ice", 1, 2, 1, 1, 1, 0.5, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1]
  fighting_column = ["fighting", 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0.5, 0.5, 1, 1, 0.5, 1, 2]
  poison_column = ["poison", 1, 1, 1, 1, 0.5, 1, 0.5, 0.5, 2, 1, 2, 0.5, 1, 1, 1, 1, 1, 0.5]
  ground_column = ["ground", 1, 1, 2, 2, 0, 2, 1, 0.5, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 1]
  flying_column = ["flying", 1, 1, 1, 0.5, 2, 2, 0.5, 1, 0, 1, 1, 0.5, 2, 1, 1, 1, 1, 1]
  psychic_column = ["psychic", 1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 0.5, 2, 1, 2, 1, 2, 1, 1]
  bug_column = ["bug", 1, 2, 1, 0.5, 1, 1, 0.5, 1, 0.5, 2, 1, 1, 2, 1, 1, 1, 1, 1]
  rock_column = ["rock", 0.5, 0.5, 2, 2, 1, 1, 2, 0.5, 2, 0.5, 1, 1, 1, 1, 1, 1, 2, 1]
  ghost_column = ["ghost", 0, 1, 1, 1, 1, 1, 0, 0.5, 1, 1, 1, 0.5, 1, 2, 1, 2, 1, 1]
  dragon_column = ["dragon", 1, 0.5, 0.5, 0.5, 0.5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2]
  dark_column = ["dark", 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 2, 1, 0.5, 1, 0.5, 1, 2]
  steel_column = ["steel", 0.5, 2, 1, 0.5, 1, 0.5, 2, 0, 2, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 1, 0.5, 0.5]
  fairy_column = ["fairy", 1, 1, 1, 1, 1, 1, 0.5, 2, 1, 1, 1, 0.5, 1, 1, 0, 0.5, 2, 1]

  defender_type = [normal_column, fire_column, water_column, electric_column, grass_column, ice_column, fighting_column, poison_column, ground_column, flying_column, psychic_column, bug_column, rock_column, ghost_column, dragon_column, dark_column, steel_column, fairy_column]

  attacker_type = ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]

  cont = -1
  type_multiplier = 1

  for i in range(len(attacker_type)):
    if attacker_type[i] == used_move.type:
      cont = i

  cont += 1

  for i in defender_type:
    if i[0] == pkmn2.type1:
      for j in range(len(i)):
        if j == cont:
          type_multiplier *= i[j]

  for i in defender_type:
    if i[0] == pkmn2.type2:
      for j in range(len(i)):
        if j == cont:
          type_multiplier *= i[j]

  t.sleep(1)
  
  if type_multiplier > 1:
    print("It is super effective!!!")
  elif type_multiplier < 1 and type_multiplier != 0:
    print("It is not very effective...")
  elif type_multiplier == 0:
    print(pkmn2.name + " is immune to " + used_move.type + " type moves!")
  return type_multiplier



def battle(pokemon_list, move_list):
  print("BATTLE STARTS")
  print("")

  pkmn1_move_list = []
  pkmn2_move_list = []
  pkmn1 = pkmn1_setup(pokemon_list, move_list, pkmn1_move_list)
  pkmn2 = pkmn2_setup(pokemon_list, move_list, pkmn2_move_list)

  pkmn1_current_hp = pkmn1.hp
  pkmn2_current_hp = pkmn2.hp
  everyone_alive = True

  if pkmn1.spe <= pkmn2.spe:
    print(pkmn1.name + " is faster than " + pkmn2.name)
    option_foe = r.randint(0, 3)
    for i in range(len(pkmn2_move_list)):
      if i == option_foe:
        print("")
        print(pkmn2.name + " used " + pkmn2_move_list[i].name + "!")
        chosen_move = pkmn2_move_list[i]
        
    damage_dealt = deal_damage(chosen_move, pkmn2, pkmn1)
    pkmn1_current_hp -= damage_dealt

    everyone_alive = is_everyone_alive(pkmn1, pkmn2, pkmn1_current_hp, pkmn2_current_hp)
  
  
  while everyone_alive == True:
    print("You")
    print(pkmn1.name)
    print(str(pkmn1_current_hp) + "/" + str(pkmn1.hp))
    hp_bar(pkmn1.hp, pkmn1_current_hp)
  
    # For some reason, I needed two "print("")" to separate the printed lines on the console
    print("")
    print("")
  
    print("Foe")
    print(pkmn2.name)
    print(str(pkmn2_current_hp) + "/" + str(pkmn2.hp))
    hp_bar(pkmn2.hp, pkmn2_current_hp)
  
    print("")
    print("")

    if everyone_alive == True:
      n = 0
      for i in pkmn1_move_list:
        n += 1
        print("[" + str(n) + "] " + i.name)
  
      print("")
      option = int(input("Which move you want to use? Type a number here: "))
      while option <= 0 or option >= 5:
        print("Please, type a number between 1 and 4.")
        option = int(input("Which move you want to use? Type a number here: "))
      option -= 1
    
      # Your Pokémon is attacking
      for i in range(len(pkmn1_move_list)):
        if i == option:
          print("")
          print(pkmn1.name + " used " + pkmn1_move_list[i].name + "!")
          chosen_move = pkmn1_move_list[i]
      
      damage_dealt = deal_damage(chosen_move, pkmn1, pkmn2)
      
      pkmn2_current_hp -= damage_dealt
  
      everyone_alive = is_everyone_alive(pkmn1, pkmn2, pkmn1_current_hp, pkmn2_current_hp)
  
  
    if everyone_alive == True:
      # Opponent's Pokémon is attacking
      option_foe = r.randint(0, 3)
    
      for i in range(len(pkmn2_move_list)):
        if i == option_foe:
          print("")
          print(pkmn2.name + " used " + pkmn2_move_list[i].name + "!")
          chosen_move = pkmn2_move_list[i]
          
      damage_dealt = deal_damage(chosen_move, pkmn2, pkmn1)
      pkmn1_current_hp -= damage_dealt
  
      everyone_alive = is_everyone_alive(pkmn1, pkmn2, pkmn1_current_hp, pkmn2_current_hp)

    print("")
  menu()









# The main menu of the program. It is used to select which functionality the user wants to use.
# It is shown to the user during the entire program and is only shut down when the user chooses the "Exit" option
def menu():
  print("--------MAIN MENU--------")
  print("")
  print("[1] Insert new Pokémon")
  print("[2] Insert new move")
  print("[3] Look for data")
  print("[4] Save data")
  print("[5] Load data")
  print("[6] BATTLE!!!")
  print("[7] Exit")
  print("")
  option = input("Choose your option by typing the number: ")
  print("")

  # Input verification
  while option != "1" and option != "2" and option != "3" and option != "4" and option != "5" and option != "6" and option != "7":
    print("Invalid input! Please, type a number between 1 and 7.")
    option = input("Type your option: ")
    print("")

  if option == "1":
    new_pokemon(pokemon_list)
  elif option == "2":
    new_move(move_list)
  elif option == "3":
    look_pokemon(pokemon_list)
  elif option == "4":
    save(pokemon_list, move_list)
  elif option == "5":
    load(pokemon_list, move_list)
  elif option == "6":
    battle(pokemon_list, move_list)
  elif option == "7":
    print("Bye bye! Thanks for playing!")
    return

# The welcome screen of the program
# Firstly asks if the user wants to star a new file or work with a previous one
# This screen is only shown once during the program runtime
print("--------POKÉMON MAKER--------")
print("")
print("Do you want to start a new file or load a previous one?")
print("")
print("[1] New file")
print("[2] Load file")
print("")
option = input("Choose an option by typing a number: ")

while option != "1" and option != "2":
    print("Invalid input! Please, type a number between 1 and 2.")
    option = input("Type your option: ")
    print("")
  
if option == "1":
  print("")
  menu()
elif option == "2":
  print("")
  load(pokemon_list, move_list)