# Package Sorting Challenge – Thoughtful AI

## Objective
This project implements a Python function that determines how packages should be routed in an automated robotic system based on their dimensions and mass.

The function follows the rules defined in the Thoughtful AI technical challenge.

---

## Sorting Rules

A package is considered:

### **Bulky** if:
- Its volume (width × height × length) is **greater than or equal to 1,000,000 cm³**, OR
- Any of its dimensions is **greater than or equal to 150 cm**

### **Heavy** if:
- Its mass is **greater than or equal to 20 kg**

---

## Dispatch Logic

| Condition | Stack |
|---------|-------|
| Not bulky AND not heavy | `STANDARD` |
| Bulky OR heavy | `SPECIAL` |
| Bulky AND heavy | `REJECTED` |

---

## Implementation

The main function is:

```python
sort(width, height, length, mass)
