solution = ["R","L","L","R","R","R","L","L","L","R","R","L","L","R","L","L","R","L","L","L","R","L","R","R","R","L","R","L"]

print("\n======================.")
print("S |     |       |     |")
print("| | .== | | ==. '=. | |")
print("|   |   | |   |   | | |")
print("|===| .===| | '=. |=' |")
print("|   | |   | |   | |   |")
print("|== | | | '=| | | | | |")
print("|   |   |   | | |   | |")
print("| ========= '=' |===' |")
print("|               |     E")
print("'======================\n")
print("\n--- Make your way through the maze ---\n")

arr = []
for i in range(28):
    choice = input(f"Enter your {i+1} move - Left (enter L) or Right (enter R)? ").upper()
    arr.append(choice)

if arr == solution:
    print("\n🎉 Congratulations! You solved the maze and reached the exit!")
else:
    print("\n❌ Wrong path! You got lost in the maze.")
    print("Your moves were: ", "".join(arr))
    print("Correct moves were: ", "".join(solution))
