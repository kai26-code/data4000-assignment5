student_key = input("Student key: ")
seed = sum(ord(ch) for ch in student_key.strip()) 

subtotal = 0.0
total_units = 0

while True:
    item_name = input("Item name: ").strip()

    if item_name.upper() == "DONE":
        break

    if item_name == "":
        print("Item name cannot be empty.")
        continue
    
    while True:
        try:
            unit_price = float(input("Unit price: ").strip())
            if unit_price <= 0:
                print("Unit price must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid price. Please enter a number.")

    while True:
        try:
            quantity = int(input("Quantity: ").strip())
            if quantity < 1:
                print("Quantity must be at least 1.")
                continue
            break
        except ValueError:
            print("Invalid quantity. Please enter an integer.")

    subtotal += unit_price * quantity
    total_units += quantity
    
if total_units >= 10 or subtotal >= 100:
    discount_rate = 0.10
else:
    discount_rate = 0.00

discount_amount = subtotal * discount_rate
total_after_discount = subtotal - discount_amount

if seed % 2 == 1:
    total_after_discount -= 3.00
    perk_applied = "YES"
else:
    perk_applied = "NO"

if total_after_discount < 0:
    total_after_discount = 0.00
    
print(f"Seed: {seed}")
print(f"Units: {total_units}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: {int(discount_rate * 100)}%")
print(f"Perk applied: {perk_applied}")
print(f"Total: ${total_after_discount:.2f}") 