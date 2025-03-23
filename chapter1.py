import random
import time

def search_wreckage(player):
    print("\n🌌 Captain Orion surveys the wreckage of his ship...")
    time.sleep(1)
    
    locations = ["Cockpit", "Engine Room", "Cargo Bay"]
    print("🔍 Where should Orion search?")
    for i, loc in enumerate(locations, 1):
        print(f"{i}. {loc}")
    
    choice = input("Enter your choice (1-3): ")
    if choice not in ["1", "2", "3"]:
        print("❌ Invalid choice. Orion picks randomly.")
        choice = str(random.randint(1, 3))
    
    location = locations[int(choice) - 1]
    print(f"🔎 Searching the {location}...")
    time.sleep(1)
    
    supplies = ["Med Kit", "Flashlight", "Food Rations", "Repair Tools", "Alien Device", "Power Core", "Fuel Cells", "Navigation Module"]
    found = random.choice(supplies)
    print(f"🔎 He finds a {found}!")
    player.add_item(found)
    return found

def repair_ship(player):
    print("\n🛠️ Captain Orion inspects the ship’s damage...")
    time.sleep(1)
    
    required_parts = ["Power Core", "Fuel Cells", "Navigation Module"]
    collected_parts = [item for item in player.inventory if item in required_parts]
    
    print("🔧 The ship needs these parts to be repaired:")
    print(required_parts)
    print("🔍 Current collected parts:", collected_parts or "None")
    
    while len(collected_parts) < len(required_parts):
        action = input("🛠️ Keep searching for parts? (yes/no): ").lower()
        if action == "yes":
            found_item = search_wreckage(player)
            if found_item in required_parts and found_item not in collected_parts:
                collected_parts.append(found_item)
                print(f"✅ {found_item} collected for repair!")
        elif action == "no":
            print("⏳ Orion decides to explore further without fully repairing the ship.")
            return False
        else:
            print("❌ Invalid input. Orion continues searching.")
            found_item = search_wreckage(player)
        
        time.sleep(1)
    
    print("🚀 The ship is partially functional! Orion can explore more or try to leave later.")
    return True