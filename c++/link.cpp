#include "pstream.h"
#include <string>
#include <iostream>

int main()
{
  // run a process and create a streambuf that reads its stdout and stderr
  redi::ipstream proc("ls", redi::pstreams::pstdout | redi::pstreams::pstderr);
  std::string line;
  // read child's stdout
  while (std::getline(proc.out(), line))
    std::cout << "stdout: " << line << '\n';
  // read child's stderr
  while (std::getline(proc.err(), line))
    std::cout << "stderr: " << line << '\n';
}  
