import time

def final_decision(player):
    print("\n🚀 Captain Orion reaches a working spaceship...")
    time.sleep(1)

    print("🔹 He has three choices:")
    print("1️⃣ Escape the planet.")
    print("2️⃣ Stay and uncover the planet’s secrets.")
    print("3️⃣ Destroy the ruins to prevent anyone else from being trapped.")
    
    if player.has_item("Energy Core"):
        print("ℹ️ With the Energy Core, escaping is more likely to succeed!")
    if player.has_item("Unknown Artifact"):
        print("ℹ️ The Unknown Artifact might hold clues to the planet’s secrets.")
    
    choice = input("🛑 Choose wisely (1/2/3): ")

    if choice == "1":
        print("🚀 Orion takes off, leaving the planet behind!")
        if player.has_item("Energy Core"):
            print("✅ The Energy Core ensures a smooth escape!")
        else:
            print("⚠️ The ship struggles but makes it off the planet.")
    elif choice == "2":
        print("🔍 He stays, determined to discover the planet’s mysteries.")
        if player.has_item("Unknown Artifact"):
            print("✅ The Artifact reveals ancient knowledge!")
        else:
            print("⚠️ Orion searches blindly for answers.")
    elif choice == "3":
        print("💥 He destroys the ruins, ensuring no one else is trapped.")
        if player.has_item("Repair Tools"):
            print("✅ The Repair Tools make demolition efficient!")
        else:
            print("⚠️ It’s a messy job, but the ruins are gone.")
    else:
        print("⏳ Orion hesitates, unsure of what to do next...")
    
    return choice