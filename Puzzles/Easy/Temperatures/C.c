// https://www.codingame.com/training/easy/temperatures

#include <stdlib.h>
#include <stdio.h>

int main()
{
    int n;
    int o = 5526;
    scanf("%d", &n);
    if (n > 0) {
        for (int i = 0; i < n; i++) {
            int t;
            scanf("%d", &t);
            if (abs(t) < abs(o)) {
                o = t;
            } else if (abs(t) == abs(o)) {
                o = t>o ? t : o;
            }
        }
    } else {o = 0;}
    printf("%d\n", o);
    return 0;
}
