#ifndef NODES_H
#define NODES_H

#include <iostream>

using T=int;

class nodes{
public:
T data;
nodes *next;

virtual ~nodes () {delete next;}
};

#endif // NODES_H
