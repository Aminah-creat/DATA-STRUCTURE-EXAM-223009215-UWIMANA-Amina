#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

// MenuItem definition
struct MenuItem {
    string name;
    float price;
};

vector<MenuItem> menu = {
    {"Burger", 5.99}, {"Pizza", 7.99}, {"Pasta", 6.49}, {"Fries", 2.99},
    {"Soda", 1.49}, {"Coffee", 1.99}, {"Salad", 3.99}, {"Juice", 2.49},
    {"Wings", 4.99}, {"Ice Cream", 2.99}, {"Steak", 12.99}, {"Fish", 9.99},
    {"Chicken", 8.49}, {"Rice", 3.49}, {"Noodles", 4.29}, {"Tea", 1.29},
    {"Milkshake", 3.59}, {"Cake", 2.79}, {"Bread", 1.49}, {"Soup", 3.19}
};

// Abstract class OrderBase
class OrderBase {
protected:
    vector<MenuItem> items;

public:
    OrderBase(const vector<MenuItem>& items) : items(items) {}
    virtual float totalCost() const = 0;
    virtual void printOrder() const = 0;
    virtual ~OrderBase() = default;
};

// TakeOutOrder
class TakeOutOrder : public OrderBase {
public:
    TakeOutOrder(const vector<MenuItem>& items) : OrderBase(items) {}

    float totalCost() const override {
        float total = 0;
        for (const auto& item : items)
            total += item.price;
        return total + 1.50; // packaging fee
    }

    void printOrder() const override {
        cout << fixed << setprecision(2);
        cout << "Take-Out Order:\n";
        for (const auto& item : items)
            cout << "- " << item.name << ": $" << item.price << endl;
        cout << "Packaging Fee: $1.50\n";
        cout << "Total: $" << totalCost() << "\n\n";
    }
};

// DineInOrder
class DineInOrder : public OrderBase {
public:
    DineInOrder(const vector<MenuItem>& items) : OrderBase(items) {}

    float totalCost() const override {
        float total = 0;
        for (const auto& item : items)
            total += item.price;
        return total + 0.75; // service fee
    }

    void printOrder() const override {
        cout << fixed << setprecision(2);
        cout << "Dine-In Order:\n";
        for (const auto& item : items)
            cout << "- " << item.name << ": $" << item.price << endl;
        cout << "Service Fee: $0.75\n";
        cout << "Total: $" << totalCost() << "\n\n";
    }
};

// OrderManager
class OrderManager {
    vector<OrderBase*> orders;

public:
    ~OrderManager() {
        for (auto order : orders)
            delete order;
    }

    void addOrder(OrderBase* order) {
        orders.push_back(order);
        cout << fixed << setprecision(2);
        cout << "Order #" << orders.size() - 1 << " added. Total Price: $" << order->totalCost() << "\n";
    }

    void removeOrder(int id) {
        if (id < 0 || id >= orders.size()) {
            cout << "Invalid order ID.\n";
            return;
        }
        delete orders[id];
        orders.erase(orders.begin() + id);
        cout << "Order #" << id << " removed.\n";
    }

    void showOrders() const {
        if (orders.empty()) {
            cout << "No orders available.\n";
        } else {
            for (int i = 0; i < orders.size(); i++) {
                cout << "Order #" << i << ":\n";
                orders[i]->printOrder();
            }
        }
    }

    int getOrderCount() const {
        return orders.size();
    }
};

// Show menu
void showMenu() {
    cout << "\n--- MENU ---\n";
    for (int i = 0; i < menu.size(); ++i)
        cout << i + 1 << ". " << menu[i].name << " - $" << fixed << setprecision(2) << menu[i].price << endl;
}

// Main
int main() {
    OrderManager manager;
    int choice;

    while (true) {
        showMenu();
        cout << "\n1. Add Order\n2. Remove Order\n3. Show Orders\n0. Exit\nChoose: ";
        cin >> choice;

        if (choice == 1) {
            int n;
            cout << "How many items in the order? ";
            cin >> n;
            if (n < 1 || n > 10) {
                cout << "Invalid number of items.\n";
                continue;
            }

            vector<MenuItem> selected;
            for (int i = 0; i < n; ++i) {
                int itemNo;
                cout << "Enter item number (1-20): ";
                cin >> itemNo;
                if (itemNo >= 1 && itemNo <= 20)
                    selected.push_back(menu[itemNo - 1]);
                else {
                    cout << "Invalid item. Try again.\n";
                    --i;
                }
            }

            int type;
            cout << "Order type? (1 = TakeOut, 2 = DineIn): ";
            cin >> type;

            if (type == 1)
                manager.addOrder(new TakeOutOrder(selected));
            else if (type == 2)
                manager.addOrder(new DineInOrder(selected));
            else
                cout << "Invalid type. Order cancelled.\n";
        }
        else if (choice == 2) {
            manager.showOrders();
            if (manager.getOrderCount() > 0) {
                int id;
                cout << "Enter order ID to remove: ";
                cin >> id;
                manager.removeOrder(id);
            }
        }
        else if (choice == 3) {
            manager.showOrders();
        }
        else if (choice == 0) {
            cout << "Exiting program.\n";
            break;
        }
        else {
            cout << "Invalid option. Try again.\n";
        }
    }
    return 0;
}

