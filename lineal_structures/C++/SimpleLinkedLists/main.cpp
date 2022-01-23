#include "list.h"
#include "nodes.h"
#include <iostream>


int main(int argc, char const *argv[]) {

  list a = list(5);//example for a 5 elements size of the list

  a[0] = 1;
  a[1] = 2;
  a[2] = 3;
  a[3] = 4;
  a[4] = 5;

  a.print();

  std::cout << "List a, element: " << '4' << a[4] << '\n';

  std::cout << "Size: " << a.size() << '\n';

  a.resize(6);

  std::cout << "Resize: " << a.size() << '\n';

  std::cout << "List a, element 4: " << a[5] << '\n';

  std::cout << "List a contains 7? " << a.contains(7) <<'\n';

  std::cout << "List a contains 1? " << a.contains(1) <<'\n';

  std::cout << "List a, where is the 1? " << a.find(1) <<'\n';

  std::cout << "List a, where is the 5? " << a.find(5) <<'\n';

  std::cout << "Size: " << a.size() << '\n';

  a.push_back(8);

  std::cout << "Size: " << a.size() << '\n';

  std::cout << "List a, push_back: 8" << '\n';

  std::cout << "List a, element: 7:  " << a[6] << '\n';

  a.resize(0);

  std::cout << "Resize: " << a.size() << '\n';

  std::cout << "List a, element: " << a[5] << '\n';

  std::cout << "List a contains 7? " << a.contains(7) <<'\n';

  std::cout << "List a contains 1? " << a.contains(1) <<'\n';

  std::cout << "List a, where is the 1? " << a.find(1) <<'\n';

  a.print();

  a.push_back(10);

  a.print();

  std::cout << "Resize: " << a.size() << '\n';

  std::cout << "List a contains 8? " << a.contains(8) <<'\n';

  std::cout << "print a: "; a.print();

  std::cout << "***************************************************" << '\n';


  list b = list();

  std::cout << "Size B: " << b.size() << '\n';

  b.push_back(50);

  std::cout << "List b, element 1: " << b[1] << '\n';

  b.push_back(1);

  b.push_back(1);

  b.push_back(1);


  b.print();

  std::cout << "***************************************************" << '\n';

  list c = list(5, 69);

  std::cout << "Size c: " << c.size() << '\n';

  std::cout << "List c, element 4: " << c[4] << '\n';

  c.resize(1);

  c.print();

  c.push_back(0);

  c.print();


  return 0;
}
