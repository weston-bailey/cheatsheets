# C Langauge basics

Header files are imported at the top of a .c file with an `include directive`. 

A headers contain function and macro definitions and can be created for a project or included with a library/compiler.

```c
#include <file.h>
#include "file.h"
```

The `entry point` is always an function named `main` that returns 0. `main` initializes the c program.

```c
int main() {
  // do some stuff
}
```

defining a function in c:

```c
return_type function_name(parameter, list) {
  // body of the function
} 

int my_function(int my_param) {
  // do some stuff
  return my_param;
}
```

C lang naming conventions:

```c
/* 
function names should be verbs that describe their action
lower_case_with_underscores_for_spaces
*/

int square_int(int number) {
  return number * number;
}

// inlcude units in names when relevent 
uint32 timeout_msecs;
int weight_lbs;

// global constants in all caps
const int A_GLOBAL_CONSTANT = 10;

// global variables prefixed with g_
int g_global_int = 10;

// enums in capitol case with labels in caps
enum DaysOfTheWeek {
  MONDAY,
  TUESDAY,
  WEDNESDAY,
  THURSDAY,
  FRIDAY,
  SATURDAY,
  SUNDAY
}
```



