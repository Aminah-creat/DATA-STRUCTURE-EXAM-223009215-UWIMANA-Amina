// sample calculator
#include <iostream>

// Function prototypes
double add(double a, double b);
double subtract(double a, double b);
double multiply(double a, double b);
double divide(double a, double b);

int main() {
    char operation;
    double num1, num2, result;

    // Display available operations
    std::cout << "Select an operation:\n";
    std::cout << "+ : Addition\n";
    std::cout << "- : Subtraction\n";
    std::cout << "* : Multiplication\n";
    std::cout << "/ : Division\n";
    std::cout << "Enter your choice: ";
    std::cin >> operation;

    // Input numbers
    std::cout << "Enter two numbers: ";
    std::cin >> num1 >> num2;

    // Perform the chosen operation
    switch (operation) {
        case '+':
            result = add(num1, num2);
            break;
        case '-':
            result = subtract(num1, num2);
            break;
        case '*':
            result = multiply(num1, num2);
            break;
        case '/':
            if (num2 != 0) {
                result = divide(num1, num2);
            } else {
                std::cout << "Error: Division by zero is undefined.\n";
                return 1; // Exit the program with an error code
            }
            break;
        default:
            std::cout << "Error: Invalid operation selected.\n";
            return 1; // Exit the program with an error code
    }

    // Display the result
    std::cout << "Result: " << result << std::endl;
    return 0;
}

// Function definitions
double add(double a, double b) {
    return a + b;
}

double subtract(double a, double b) {
    return a - b;
}

double multiply(double a, double b) {
    return a * b;
}

double divide(double a, double b) {
    return a / b;
}
