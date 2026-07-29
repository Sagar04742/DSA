#include <stdio.h>

int main() {
    char x[] = "aBCdef";
    int n = sizeof(x) - 1; // Subtract 1 to exclude the null terminator

    for (int i = 0; i < n; i++) {
        if (x[i] >= 'A' && x[i] <= 'Z') {
            x[i] = x[i] + 32; // Convert uppercase to lowercase
        } else if (x[i] >= 'a' && x[i] <= 'z') {
            x[i] = x[i] - 32; // Convert lowercase to uppercase
        }
    }

    printf("%s\n", x);
    return 0;
}
