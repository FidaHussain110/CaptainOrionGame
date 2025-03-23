import time

def decipher_symbols():
    print("\n🏺 Captain Orion approaches ancient alien ruins covered in glowing symbols.")
    time.sleep(1)
    
    answer = input("📜 Attempt to translate the symbols? (yes/no): ").lower()
    
    if answer == "yes":
        print("🔮 The symbols reveal a hidden chamber behind the ruins! Orion can enter.")
        return True
    elif answer == "no":
        print("⛔ Orion skips the translation. The chamber remains sealed.")
        return False
    else:
        print("❌ Invalid input. Orion hesitates and moves on.")
        return False

def solve_puzzle():
    print("\n🧩 Orion finds a stone tablet with a riddle...")
    time.sleep(1)
    
    print("📜 Riddle: 'What has keys but can't open locks?'")
    attempts = 3
    
    while attempts > 0:
        answer = input("🔎 Your answer: ").lower()
        
        if answer == "keyboard":
            print("✅ The temple doors slide open with a deep rumble!")
            return True
        else:
            attempts -= 1
            print(f"❌ Incorrect! {attempts} attempts left.")
    
    print("⛔ The puzzle remains unsolved. Orion must find another way.")
    return False