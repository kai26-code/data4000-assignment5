import requests

student_key = input("Student key: ")
seed = sum(ord(ch) for ch in student_key.strip())

total_skus = 0
reorder_count = 0

if seed % 3 == 0:
    threshold = 15
elif seed % 3 == 1:
    threshold = 12
else:
    threshold = 9


while True:
    sku = input("SKU: ").strip()

    if sku.upper() == "DONE":
        break

    if sku == "":
        print("SKU cannot be blank.")
        continue

    # Quantity validation
    while True:
        try:
            on_hand = int(input("On hand: ").strip())
            if on_hand < 0:
                print("Inventory cannot be negative.")
                continue
            break 
        except ValueError:
            print("Invalid number. Please enter an integer.")

    total_skus += 1

    if on_hand < threshold:
        reorder_count += 1

if seed % 2 == 0:
    term = "weezer"
else:
    term = "drake"

songs_count = "N/A"
api_status = "FAILED"


try:
    # Build URL using seed-based term
    url = f"https://itunes.apple.com/search?entity=song&limit=5&term={term}"

    response = requests.get(url, timeout=5)

    # Raise error if bad HTTP status
    response.raise_for_status()

    o = response.json()

    # Validate JSON structure
    if "results" not in o:
        api_status = "INVALID_RESPONSE"
    else:
        count = 0
        for result in o["results"]:
            if result.get("kind") == "song":
                count += 1

        songs_count = count
        api_status = "OK"

except requests.exceptions.RequestException:
    api_status = "FAILED"

except ValueError:
    api_status = "INVALID_RESPONSE"

print(f"Seed: {seed}")
print(f"Threshold: {threshold}")
print(f"SKUs entered: {total_skus}")
print(f"Reorder flagged: {reorder_count}")
print(f"Spotcheck term: {term}")
print(f"Songs returned: {songs_count}")
print(f"API status: {api_status}")