Restaurant Order Manager

 Introduction

The Restaurant Order Manager project is about a C++ application for processing customer orders for dine-in and take-out orders. It uses object-oriented programming principles such as inheritance and polymorphism to model different types of orders, and uses vectors and smart pointers for safe and efficient dynamic memory allocation. The application makes it possible for users to view a menu, place orders, remove them, and display all current orders.

In this Restaurant Order Manager project, Inheritance helps to define a general order structure (OrderBase) for all types of orders, i.e., Take-Out and Dine-In. Instead of writing each type of order from scratch in the individual code, you define general behavior once in the base class and then inherit and extend it in the derived classes. This not only keeps the code cleaner but also more maintainable and flexible so if ever you want to add new kinds of orders (like Delivery), you can simply add a new class inheriting from OrderBase without having to repeat existing logic. Polymorphism allows the program to treat different types of orders (TakeOutOrder and DineInOrder) uniformly through a common base class, OrderBase. The OrderManager stores all orders as pointers to OrderBase, but when calling methods like totalCost() or printOrder(), the program dynamically decides which version to execute based on the actual order type. This enables flexible and scalable handling of multiple order types without changing the order management logic.  Main features

• Static menu of 20 items • Abstract base class with derived classes • Virtual method ‘totalcost()’ overridden in each derived class • Pointer arithmetic to calculate totals • User select items via ‘cin’ • Add orders (Take-Out or Dine-In) • Orders stored dynamically using pointers • Remove orders • Display all current orders

 Code Structure -“MenuItem” struct: //Stores name and price

“OrderBase abstract” class:// Holds dynamic MenuItem** items and int nItems, Declares virtual float totalCost() = 0
“TakeOutOrder” class:// Inherits from OrderBase, Adds packaging fee of $1.50
“DineInOrder” class:// Inherits from OrderBase, adds service fee of $0.75
“OrderManager” class:// Manages dynamic array of OrderBase*, Provides addOrder, removeOrder, and listOrders
Let explain codes line by line

Libraries #include // This includes the iostream library, which allows the use of standard input (cin) and output (cout) streams. #include //This includes the vector library, which provides the std::vector container a dynamic array that can grow or shrink in size. #include // This includes the iomanip library, used for manipulating the format of input/output, e.g., setting decimal precision using setprecision. using namespace std; // This allows you to use standard library names (like vector, string, cout, cin, etc.) without needing to prefix them with std::

MenuItem Struct struct MenuItem { char name[30]; float price; }; // these codes store the name and price of a menu item.

Static Menu Array std::vector menu = { {"Burger", 5.99}, {"Pizza", 7.99}, ... }; // these codes present Pre-defined vector of 20 MenuItems.

OrderBase (Abstract Class) class OrderBase { protected: // data members can be accessed from within the class itself and by derived classes. std::vector<MenuItem*> items; public: // data members are accessible anywhere virtual float totalCost() = 0; virtual void printOrder() = 0; virtual ~OrderBase() {} }; // Base class for all orders, Stores a list of pointers to menu items, and Requires derived classes to implement totalCost() and printOrder().

TakeOutOrder (Derived Class) class TakeOutOrder : public OrderBase { float totalCost() override { return item sum + $1.50 (packaging fee); } void printOrder() override { prints items and total. } }; // Adds a $1.50 packaging fee.

DineInOrder (Derived Class) class DineInOrder : public OrderBase { float totalCost() override { return item sum + $0.75 (service fee); } void printOrder() override { prints items and total. } }; // Adds a $0.75 service fee.

OrderManager Class class OrderManager { std::vector<std::unique_ptr> orders; public: // can be accessed outside the class void addOrder(OrderBase*); void removeOrder(int id); void showOrders(); }; // Manages all orders, Adds, deletes, and displays orders using a vector of smart pointers.

ShowMenu() Function void showMenu(); // Displays the full menu.

main() Function • Contains the user interface loop. • Prompts user to add, remove, or show orders. • Handles user input and order creation. • Finally, the main function returns 0 to indicate successful execution of the program.

 Usage

Choose to add a dine-in or take-out order.
Enter how many items to include.
Choose items by their index.
Program displays total cost and saves the order. 5. View all orders at any time.
 Example of Output

Add Order
Remove Order
Show Orders
Exit Choose: 1 How many items in the order? 1 Enter item number (1-20): 8 Order type? (1 = TakeOut, 2 = DineIn): 2 The order [0] added. Total Price: $3.24
