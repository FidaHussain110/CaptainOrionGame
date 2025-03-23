import random
import time

def search_old_wreckage(player):
    print("\n🛰️ Orion discovers an old spaceship wreckage deep in the ruins...")
    time.sleep(1)
    
    print("🔍 Where should Orion search?")
    print("1. Control Panel")
    print("2. Storage Compartment")
    print("3. Engine Bay")
    choice = input("Enter your choice (1-3): ")
    
    if choice not in ["1", "2", "3"]:
        print("❌ Invalid choice. Orion picks randomly.")
        choice = str(random.randint(1, 3))
    
    locations = ["Control Panel", "Storage Compartment", "Engine Bay"]
    location = locations[int(choice) - 1]
    print(f"🔎 Searching the {location}...")
    time.sleep(1)
    
    found = random.choice(["Energy Core", "Damaged Log File", "Unknown Artifact"])
    print(f"🔎 He recovers a {found}!")
    player.add_item(found)
    return found

def decode_message(player):
    print("\n📡 Orion finds a distress beacon with a log...")
    time.sleep(1)
    
    if player.has_item("Damaged Log File"):
        action = input("📜 Decode the log file? (yes/no): ").lower()
        if action == "yes":
            print("📝 Message: 'Final entry... They were not alone. Beware the guardian.'")
            return True
        elif action == "no":
            print("⏳ Orion skips the log and moves on.")
            return False
        else:
            print("❌ Invalid input. Orion ignores the log.")
            return False
    else:
        print("⛔ No log file found to decode.")
        return False