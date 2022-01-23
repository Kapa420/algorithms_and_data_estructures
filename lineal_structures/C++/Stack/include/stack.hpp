#ifndef STACK_HPP
#define STACK_HPP
#include "nodes.hpp"
#include <iostream>

class stack {
private:
  nodes* m_head;

public:
  stack();
  void push_up(const T &val);
  void pop_up();
  void head();
  void print();
  virtual ~stack ();
};


#endif //STACK_HPP
