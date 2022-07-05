#include <stdio.h>
using namespace std;

bool a(){
    printf ("a output");
    return true;
}

bool b(){
    printf ("b output");
    return false;
}

int main()
{
    if (a()|b()) printf("yes\n");
    if (a()||b()) printf("yes\n");
    return 0;
}
