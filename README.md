# Crossmint Challenge

candidate id - `245b9d9e-a0ae-4d24-8854-ba383f1e0ef7`

## Overview

- **Phase 1**: Build a grid using only Polyanets based on the target configuration.
- **Phase 2**: Construct a symmetric grid involving multiple object types using a quadrant-based approach to optimize performance.

---

## Code Structure
```
cross-mint/
├── constants.py        # Stores API endpoints, candidate ID, and object names
├── helpers.py          # Shared helper functions for fetching data and creating objects
├── shapes.py           # Astral object classes (Polyanets, Soloons, Comeths)
├── phase_1.py          # Implementation for Phase 1
├── phase_2.py          # Implementation for Phase 2
└── README.md           # Documentation
```


## Phase 1 Intuition

### Approach

1. **Fetch Configuration**: Retrieve the `goal_shape` from the API.
2. **Iterate Through Grid**:
   - For cells marked as `POLYANET`, create a Polyanet at the specified coordinates.
   - Skip cells marked as `SPACE`.
3. **Place Polyanets**: Post the Polyanet data to the API for placement.

---

## Phase 2 Intuition

### Symmetry Insights

1. The grid can be divided into **four quadrants**:
   - **Top-left**
   - **Top-right** (mirrored horizontally from top-left)
   - **Bottom-left** (mirrored vertically from top-left)
   - **Bottom-right** (mirrored horizontally and vertically from top-left)
2. By processing only the **top-left quadrant**, the remaining quadrants can be programmatically derived.

### Approach

1. **Fetch Configuration**: Retrieve the `goal_shape` from the API.
2. **Extract Quadrant**: Use only the top-left quadrant of the grid.
3. **Place Objects in Quadrants**:
   - Process the top-left quadrant and calculate mirrored placements for the other three quadrants.
   - Use the symmetry to minimize redundant API requests.
4. **Post Objects to API**: Place objects by sending their configurations to the API.

