
---

# **Gravity Simulation Project (Built Without AI Agents)**

## **About the Project**

This project is developed **entirely without AI agents**, with the purpose of improving my programming skills and strengthening my computational thinking.
All logic, behavior, and structure are written manually, with a focus on correctness, clarity, and real-world physics.

---

## **Project Goal**

To build a **fully accurate physical gravity simulation** that can run under different gravitational conditions on various celestial bodies (Earth, Moon, Mars, custom worlds, etc.).
The long-term objective is to achieve:

* Physically correct gravitational acceleration
* Support for multiple bodies with variable mass and shape
* Interactions between objects
* Collisions with restitution
* Custom gravity models
* Realistic time-step integration

This aims to be a **scientific-grade simulation**, not an arcade-style approximation.

---

## **Current Progress**

The project is in its early foundational stage. Implemented so far:

### ✔ Square Entities

Basic square objects with size, mass, color, velocity, and screen position.

### ✔ Earth Gravity Model (Basic Physics)

* Constant gravitational acceleration (9.81 m/s² scaled to pixels)
* Velocity integration
* Position integration
* Ground collision with coefficient of restitution
* Fully deterministic frame-step physics

### ✔ Mouse Dragging System

* Ability to click and drag individual squares
* Object follows the mouse movement precisely
* Stops falling while being dragged, resumes falling when released
* Clean separation between physics updates and user interaction

---

## **Technologies Used**

* **Python 3**
* **Pygame** for real-time rendering and user input
* Pure manual programming — no AI agents

---

## **Next Steps**

* Implement different planetary gravities (Moon, Mars, Jupiter, etc.)
* Add friction and air resistance models
* Introduce circular/irregular shapes (not only squares)
* Implement object-to-object collisions
* Add mass-based gravitational attraction between bodies
* Create a full simulation engine with adjustable time-scale
* Build UI controls for selecting the planet and physical conditions

---

![gravity\_sim\_screenshot](https://github.com/user-attachments/assets/fa3c4496-b36a-42f9-9efd-cfd1a87ef993)


