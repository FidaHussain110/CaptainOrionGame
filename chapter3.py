import random
import time

def sneak_past_creatures(player):
    print("\n👣 Captain Orion must sneak past dangerous creatures in the ruins.")
    time.sleep(1)
    
    print("🔹 How should Orion proceed?")
    print("1. Move slowly and quietly.")
    print("2. Dash quickly past them.")
    choice = input("Enter your choice (1/2): ")
    
    if choice == "1":
        success_chance = 7  # Higher chance for slow movement
    elif choice == "2":
        success_chance = 4  # Lower chance for dashing
    else:
        print("❌ Invalid choice. Orion hesitates.")
        success_chance = 5
    
    roll = random.randint(1, 10)
    print(f"🎲 Stealth Roll: {roll}/{success_chance} needed")
    
    if roll <= success_chance:
        print("✅ Orion avoids detection!")
        return True
    else:
        print("🚨 A creature spots him! He must fight or flee!")
        return False

def fight_creatures(player):
    print("\n⚔️ Orion prepares to fight the approaching creatures...")
    time.sleep(1)

    print("🛠️ Choose a weapon:")
    print("1. Laser (if available)")
    print("2. Blade")
    print("3. Use an inventory item (e.g., Repair Tools)")
    choice = input("Enter your choice (1-3): ")
    
    attack = random.randint(1, 10)
    if choice == "1" and player.has_item("Laser"):
        attack += 2  # Bonus for laser
        print("🔫 Using the Laser!")
    elif choice == "3" and player.has_item("Repair Tools"):
        attack += 1  # Minor bonus for creativity
        print("🛠️ Using the Repair Tools as a makeshift weapon!")
    else:
        print("⚔️ Using a Blade!")

    print(f"🎲 Attack Roll: {attack}/7 needed")
    
    if attack >= 7:
        print("✅ Orion defeats the creatures and escapes!")
        return True
    else:
        print("❌ The creatures overpower him, forcing him to retreat!")
        return False