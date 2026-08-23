# Project 4: Inventory Manager with Action Logging
**Week 2 Capstone — Topics: Scope, OOP Basics, Exceptions, File Handling, *args/**kwargs**

## Goal
Build an inventory system where each item is an object, changes are logged
flexibly using `*args`/`**kwargs`, and the inventory persists to a CSV file.

## What You'll Practice
- OOP basics (an `Item` class)
- `*args` and `**kwargs` for a flexible logging function
- File handling (CSV read/write)
- Exceptions (handling missing files, bad input)
- Scope (a module-level counter vs. a global counter, and why `global` is
  usually avoidable)

## Requirements

### 1. `Item` class
```python
class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def total_value(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.name}: {self.quantity} units @ ${self.price:.2f}"
```

### 2. Flexible logging function
Write `log_action(action, *args, **kwargs)` that builds a log entry from
whatever information is passed to it. For example:
```python
log_action("ADD", item="Widget", quantity=10)
log_action("REMOVE", item="Widget", quantity=3, reason="damaged")
```
It should format each call into a readable string (e.g. by joining the
`kwargs` into `key=value` pairs) and append it to a module-level list
(or write straight to a log file).

### 3. Inventory operations
- `add_item(inventory, name, quantity, price)`: adds a new `Item`, or
  increases quantity if the item already exists. Calls `log_action(...)`.
- `remove_item(inventory, name, quantity)`: raises a `ValueError` if you try
  to remove more than is in stock. Calls `log_action(...)`.
- `total_inventory_value(inventory)`: sums `total_value()` across all items.

### 4. File persistence (CSV)
- `save_inventory(inventory, filename)`: use the `csv` module to write
  `name,quantity,price` rows.
- `load_inventory(filename)`: read the CSV back into a list of `Item`
  objects. Handle `FileNotFoundError` gracefully.

### 5. Scope demo
Add a module-level `action_count = 0` that increments every time
`log_action` runs — **without** using the `global` keyword if you can avoid
it (e.g. by returning the new count and reassigning it in `main`), and then
show what happens if you forget and try to modify it directly inside
the function without `global` (a great "aha" moment about scope!).

## Step-by-Step Guide

1. Build and test the `Item` class alone.
2. Build `log_action` and test it with a few different combinations of
   args/kwargs — print what it produces before wiring it into the rest.
3. Build `add_item`/`remove_item`, using `try`/`except` for bad removals.
4. Build CSV save/load and test round-tripping a small inventory.
5. Build the interactive menu in `main.py`.

## Stretch Goals (optional)
- Write the log to its own file (`inventory_log.txt`) instead of memory.
- Add a "low stock" warning when quantity drops below a threshold.
- Add a `restock_needed(inventory, threshold=5)` function returning items
  below the threshold.

## Testing Checklist
- [ ] Adding an existing item increases its quantity rather than duplicating it
- [ ] Removing more than in stock raises `ValueError`, doesn't crash
- [ ] `log_action` works correctly with different numbers of args/kwargs
- [ ] Saving then loading gives back the same inventory
- [ ] Loading with no existing file starts with an empty inventory, no crash
