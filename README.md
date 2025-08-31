# python-bcm-framework

Classes & Objects 🏗️
We started by creating blueprints for our components, like the BodyControlModule class, and then we created specific instances (objects) of them, like my_bcm.

Encapsulation 🔒
We bundled our data (like power_status) and methods (like power_on) together. This protected our data by ensuring we could only change it in controlled ways, preventing invalid states.

Inheritance 👪
We avoided code duplication by creating a general parent ECU class and having specialized child classes like BodyControlModule and EngineControlUnit inherit the common features.

Polymorphism 🎭
We treated different objects in the same way. Our run_system_check function could call power_on on any object that was a type of ECU, demonstrating the "many forms" principle.

Abstraction 🎨
Finally, we created a "contract" using an Abstract Base Class. We made the run_self_test method a requirement for all child ECUs, ensuring a standard for safety and testing across the whole system.
