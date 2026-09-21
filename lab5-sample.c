/* CYSC-620 Lab 5 sample - FIXED: gets() replaced with a bounded read. */
#include <stdio.h>

int main() {
    char src[40];
    fgets(src, sizeof(src), stdin);
    return 0;
}
