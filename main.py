from player import Player
from chapter1 import search_wreckage, repair_ship
from chapter2 import decipher_symbols, solve_puzzle
from chapter3 import sneak_past_creatures, fight_creatures
from chapter4 import search_old_wreckage, decode_message
from chapter5 import final_decision

def start_game():
    print("\n🌌 Welcome to 'Captain Orion: Lost in the Stars'!")
    print("🚀 A sci-fi adventure game where every choice matters!\n")
    
    orion = Player("Captain Orion")
    
    # Chapter 1: Crash Landing
    print("Chapter 1: Crash Landing")
    repair_complete = repair_ship(orion)
    orion.show_inventory()

    # Chapter 2: Alien Ruins
    print("\nChapter 2: The Alien Ruins")
    symbols_deciphered = decipher_symbols()
    puzzle_solved = solve_puzzle() if symbols_deciphered else False

    # Chapter 3: Creatures of the Dark
    print("\nChapter 3: Creatures of the Dark")
    sneaked = sneak_past_creatures(orion)
    if not sneaked:
        survived = fight_creatures(orion)
        if not survived:
            print("💀 Orion fails to escape the creatures. Game Over.")
            return

    # Chapter 4: The Final Piece
    print("\nChapter 4: The Final Piece")
    search_old_wreckage(orion)
    decode_message(orion)
    orion.show_inventory()

    # Chapter 5: The Final Decision
    print("\nChapter 5: The Final Choice")
    final_decision(orion)
    print("🌠 Game Complete! Thanks for playing!")

if __name__ == "__main__":
    start_game()