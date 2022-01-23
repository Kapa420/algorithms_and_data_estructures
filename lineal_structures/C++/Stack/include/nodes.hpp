#ifndef NODES_HPP
#define NODES_HPP

#include <iostream>

using T=int;

class nodes{
public:
  T data;
  nodes *next;
  virtual ~nodes () {delete next;}
};

#endif // NODES_HPP
