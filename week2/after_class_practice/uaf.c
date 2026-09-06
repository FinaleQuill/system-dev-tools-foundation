#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    char *greeting = malloc(32);
    if (greeting == NULL) {
        return 1;
    }
    strcpy(greeting, "Hello, world!");
    printf("%s\n", greeting);
    free(greeting);
    greeting[0] = 'J';
    printf("%s\n", greeting);
    return 0;
}
