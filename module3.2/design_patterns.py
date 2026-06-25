"""
Creational
Purpose:
- OBject creation mechanism

Use when:
flexible and controlled object creation
Examples:
Singleton, factory method, builder


Structural
How classes/objects are composed
Use when:
flexible structures or resusalbilty of code

Examples:
Flyweight, adapter

Behavioral
Communication between objects
USe when:
flexible interactions between objects

Examples:
Observer, strategy, state

Flyweight
-Is a structural design patter that reduces memory usage by sharing common data among similar objects
Divides data into 2 pieces:
- Intrinsic:
    - Data which can be shared and is common
- Extrinsic:
    - Data which is unique and supplied from outside when needed
    
Flyweight components:
Client:
    - Code that needs objects or uses them
Factory:
    - Manages shared flyweights
Flyweight:
     - Stores intrinsic state only
Context:
    - Stores extrinisc state and refers to flyweight
"""