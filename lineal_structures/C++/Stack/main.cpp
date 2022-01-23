#include "stack.hpp"
#include "nodes.hpp"
#include <iostream>

int main(int argc, char const *argv[]) {
  stack ejm = stack();
  ejm.push_up(10);
  ejm.push_up(20);
  ejm.push_up(30);
  ejm.head();
  ejm.print();
  return 0;
}
