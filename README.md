# data4000-assignment5

## Author
Kai Ostaszewski

---

# Exercise 1 – Discount Calculator

## Description
This program calculates a customer’s discount rate and final price based on:
- Purchase amount
- Membership status (seed member perk) 

It applies conditional logic [input(), float(), int(), if / elif / else, loops]

## What to do: 
- Enter your student key.
- Enter item names, unit prices, and quantities until finished.
- Type DONE to finish and see the totals, discount, seed perk, and final price.

## Business Rules
- Discount:
  - 10% discount if purchase ≥ 100 or units ≥ 10
  - 0% discount otherwise
- Seed Member Perk:
  - After discount, if seed is odd then subtract $3.00
  - if seed even, no perk given

## Example Output
``` bash
Student key: k102
Item name: Notebook
Unit price: 5
Quantity: 2
Item name: DONE
Seed: 254
Units: 2
Subtotal: $10.00
Discount: 0%
Perk applied: NO
Total: $10.00
```

# Exercise 2 – Inventory Spotcheck with API

## Description
This program processes inventory counts and determines which SKUs require reordering.  
It also performs a small external spot check using the iTunes Search API.

Concepts used: `input()`, `int()`, `if / elif / else`, `while` loops, `try / except`, `requests`, JSON processing.

## What to do: 
- Enter your student key.
- Enter SKUs and on-hand quantities until finished.
- Type DONE to finish and see:
    - Seed, threshold, SKUs entered, reorder flagged
    - API spotcheck results, songs returned, and API status

## Business Rules
- Seed Calculation:
  - `seed = sum(ord(ch) for ch in student_key.strip())`
- Threshold Logic (based on seed % 3):
  - 0 → threshold = 15
  - 1 → threshold = 12
  - 2 → threshold = 9
- Reorder Decision:
  - If `on_hand < threshold` → REORDER
  - Else → OK
- API Spotcheck:
  - Seed even → search term = "weezer"
  - Seed odd → search term = "drake"
  - Count results where `kind == "song"`
  - Handle errors:
    - Network failure → `API status: FAILED`
    - Invalid JSON → `API status: INVALID_RESPONSE`
    - Success → `API status: OK`

---

## Installation
First, activate your virtual environment:

``` bash
source .venv/bin/activate
```
Second, insert the code to insert "requests"
``` bash 
python3 -m pip install requests
OR
pip install requests
```

## Example Output
``` bash
Student key: k102
SKU: A100
On hand: 2
SKU: B200
On hand: 3
SKU: DONE

Seed: 254
Threshold: 9
SKUs entered: 2
Reorder flagged: 2
Spotcheck term: weezer
Songs returned: 5
API status: OK
```
