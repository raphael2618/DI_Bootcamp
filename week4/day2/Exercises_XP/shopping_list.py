basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# Remove “Banana” from the list.
del basket[0]
print(basket)
# Remove “Blueberries” from the list.
del basket[-1]
print(basket)
# Add “Kiwi” to the end of the list.
basket.append("kiwi")
# Add “Apples” to the beginning of the list.
basket.insert(0, "apples")
# Count how many apples are in the basket.
for i in basket:
    totalApples = 0
    if i == "Apples":
        totalApples += 1
        print(totalApples)
    # Empty the basket.
basket.clear()
# Print(basket)
print(basket)
