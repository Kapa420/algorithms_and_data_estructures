#include <iostream>
#include "array.hpp"

int main(int argc, char const *argv[]) {

  std::cout << "A" << '\n';

  array<double> a(0);

  std::cout << a.size() << '\n';

  a.add(12.12);

  std::cout << a.size() << '\n';

  a.print();

  a.resize(0);

  std::cout << a.size() << '\n';

  a.resize(7);

  std::cout << a.size() << '\n';

  a.print();

  return 0;
}
