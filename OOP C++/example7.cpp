// program to check even or odd
#include <iostream>
using namespace std;

int main() {
    int number;
    
    std::cout << "Enter a number: ";
    std::cin >> number;
    
    if (number % 2 == 0) {
        std::cout << "The number " << number << " is even." << std::endl;
    } else {
        std::cout << "The number " << number << " is odd." << std::endl;
    }
    
    return 0;
}


