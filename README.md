# Inventory CSA

A small Python inventory application used to practise **Software Configuration
Status Accounting (CSA)** for SEN 401, Lab 3 (MIVA Open University).

Author: Temidayo Omoyajowo (2025/B/SENG/0513)

## Files

| File | Purpose |
|------|---------|
| `inventory.py` | List of items, each with `item_name`, `quantity` and `price`. |
| `app.py` | Reads the inventory and calculates the total stock value. |
| `utils/helpers.py` | Pure helpers: `item_value`, `total_stock_value`, `highest_stock_item`, `lowest_stock_item`, `low_stock_items`. |
| `tests/` | `unittest` suite for the helpers. |
| `requirements.txt` | Python dependencies. |

## Usage

Requires **Python 3.12+**.

```bash
python3.12 app.py              # print the stock report and export inventory.csv
python3.12 -m unittest -v      # run the tests
```
