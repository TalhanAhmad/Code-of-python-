import random

gold = 0
caught = False

print("🕵️ Welcome to Thief vs Guard!")
print("Steal 50 gold without getting caught!\n")

while not caught and gold < 50:
    print(f"\n💰 Current Gold: {gold}")
    action = input("Choose action (sneak / run / hide): ").lower()

    guard = random.choice(["search", "rest", "patrol"])

    print(f"👮 Guard is: {guard}")

    if action == "sneak":
        if guard == "rest":
            print("😎 Perfect sneak! +15 gold")
            gold += 15
        else:
            print("⚠️ Risky move! +5 gold")
            gold += 5

    elif action == "run":
        if guard == "search":
            print("🚨 You got caught while running!")
            caught = True
        else:
            print("🏃 Fast escape! +10 gold")
            gold += 10

    elif action == "hide":
        if guard == "patrol":
            print("😮 Guard found you hiding!")
            caught = True
        else:
            print("🫥 Safe hide. No gold but safe.")
    
    else:
        print("❌ Invalid action")

# Game result
if caught:
    print("\n💀 GAME OVER! You got caught!")
else:
    print("\n🏆 YOU WIN! You stole enough gold!")