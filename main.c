#include <stdio.h>
#include <stdlib.h>
void delay(int number_of_seconds) 
{ 
    // Converting time into milli_seconds 
    int milli_seconds = 1000 * number_of_seconds; 
  
    // Stroing start time 
    __clock_t start_time = clock(); 
  
    // looping till required time is not acheived 
    while (clock() < start_time + milli_seconds) 
        ; 
}
int main(void)
{
  delay(5);
  system("python3 start.py");
  printf("Execution stopped.");
}