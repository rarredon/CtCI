#include <stdio.h>

void swap(int* a, int* b);

int main(){
  int a, b;
  a = 55;
  b = 71;
  printf("Before swap: a=%d, b=%d\n", a, b);
  swap(&a, &b);
  printf("After swap: a=%d, b=%d\n\n", a, b);

  a = 13;
  b = -72;
  printf("Before swap: a=%d, b=%d\n", a, b);
  swap(&a, &b);
  printf("After swap: a=%d, b=%d\n\n", a, b);

  a = -21;
  b = -105;
  printf("Before swap: a=%d, b=%d\n", a, b);
  swap(&a, &b);
  printf("After swap: a=%d, b=%d\n\n", a, b);

  a = 33;
  b = 10756;
  printf("Before swap: a=%d, b=%d\n", a, b);
  swap(&a, &b);
  printf("After swap: a=%d, b=%d\n\n", a, b);

  return 0;
}

void swap(int* a, int* b){ // NOTE: a and b are passed by reference
  *b = *b - *a;
  *a = *a + *b; //== *b original
  *b = *a - *b;
}
