---
name: grocery-list
description: >-
  Standalone grocery lists, recipes, and meal planning with local storage. No
  external service required.
homepage: 'https://clawdhub.com/skills/grocery-list'
metadata:
  clawdbot:
    emoji: "\U0001F6D2"
    requires:
      bins:
        - uv
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---

# Grocery List & Meal Planner

Self-contained grocery lists, recipes, and meal planning with local JSON storage. No subscriptions or external services required.

## Features

- **Multiple lists** — Grocery, Costco, Target, etc.
- **Smart categories** — produce, dairy, meat, bakery, frozen, pantry, household
- **Quantity parsing** — "2 gallons milk" → quantity: 2, unit: "gallon"
- **Recipe storage** — Save recipes with ingredients
- **Meal planning** — Plan meals by date and type (breakfast/lunch/dinner)
- **Recipe-to-list** — Add recipe ingredients to any list with one command
- **Family assignment** — Assign items to household members
- **Notifications** — `notify` command for heartbeat/cron integration

## Commands

### Lists

```bash
uv run {baseDir}/scripts/grocery.py lists                    # Show all lists
uv run {baseDir}/scripts/grocery.py list "Grocery"           # Show items in a list
uv run {baseDir}/scripts/grocery.py list "Grocery" --unchecked
uv run {baseDir}/scripts/grocery.py list create "Costco"     # Create new list
uv run {baseDir}/scripts/grocery.py list delete "Costco"     # Delete a list
```

### Items

```bash
uv run {baseDir}/scripts/grocery.py add "Grocery" "Milk"
uv run {baseDir}/scripts/grocery.py add "Grocery" "Milk" --category dairy --qty "2 gallons"
uv run {baseDir}/scripts/grocery.py add "Grocery" "Chicken" --assignee "Erin"
uv run {baseDir}/scripts/grocery.py check "Grocery" "Milk"
uv run {baseDir}/scripts/grocery.py uncheck "Grocery" "Milk"
uv run {baseDir}/scripts/grocery.py remove "Grocery" "Milk"
uv run {baseDir}/scripts/grocery.py clear "Grocery"          # Clear checked items
```

### Recipes

```bash
uv run {baseDir}/scripts/grocery.py recipes                  # List all recipes
uv run {baseDir}/scripts/grocery.py recipe "Tacos"           # View a recipe
uv run {baseDir}/scripts/grocery.py recipe add "Tacos" --ingredients "ground beef,tortillas,cheese,lettuce,tomatoes"
uv run {baseDir}/scripts/grocery.py recipe add "Tacos" --category "Mexican" --servings 4
uv run {baseDir}/scripts/grocery.py recipe delete "Tacos"
uv run {baseDir}/scripts/grocery.py recipe search "chicken"
```

### Meal Planning

```bash
uv run {baseDir}/scripts/grocery.py meals                    # Show this week's meals
uv run {baseDir}/scripts/grocery.py meals --date 2026-01-15
uv run {baseDir}/scripts/grocery.py meal add --date 2026-01-15 --type dinner --recipe "Tacos"
uv run {baseDir}/scripts/grocery.py meal add-to-list --date 2026-01-15 --list "Grocery"
uv run {baseDir}/scripts/grocery.py meal remove --date 2026-01-15 --type dinner
```

### Notifications

```bash
uv run {baseDir}/scripts/grocery.py notify                   # Pending alerts for heartbeat
uv run {baseDir}/scripts/grocery.py stats                    # Quick summary
```

## Categories

Built-in categories with automatic detection:

- **produce** — fruits, vegetables
- **dairy** — milk, cheese, eggs, yogurt
- **meat** — chicken, beef, pork, fish
- **bakery** — bread, rolls, bagels
- **frozen** — ice cream, frozen meals
- **pantry** — canned goods, pasta, rice
- **beverages** — drinks, soda, juice
- **snacks** — chips, crackers
- **household** — cleaning, paper goods
- **personal** — toiletries, medicine
- **other** — uncategorized

## JSON Output

All commands support `--json` for programmatic access:

```bash
uv run {baseDir}/scripts/grocery.py list "Grocery" --json
uv run {baseDir}/scripts/grocery.py recipes --json
uv run {baseDir}/scripts/grocery.py meals --json
```

## Data Storage

Data is stored locally at `~/.clawdbot/grocery-list/data.json`. No cloud account required.

## Usage Examples

**"Add milk and eggs to the grocery list"**

```bash
uv run {baseDir}/scripts/grocery.py add "Grocery" "Milk" --category dairy
uv run {baseDir}/scripts/grocery.py add "Grocery" "Eggs" --category dairy
```

**"What's on the grocery list?"**

```bash
uv run {baseDir}/scripts/grocery.py list "Grocery" --unchecked
```

**"Plan tacos for dinner on Saturday"**

```bash
uv run {baseDir}/scripts/grocery.py meal add --date 2026-01-18 --type dinner --recipe "Tacos"
```

**"Add the taco ingredients to the grocery list"**

```bash
uv run {baseDir}/scripts/grocery.py meal add-to-list --date 2026-01-18 --list "Grocery"
```

**"Check off the milk"**

```bash
uv run {baseDir}/scripts/grocery.py check "Grocery" "Milk"
```
