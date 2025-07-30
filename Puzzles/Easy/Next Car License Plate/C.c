// https://www.codingame.com/training/easy/next-car-license-plate

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int letter_duo_to_idx(char *d);
int plate_to_idx(char *p);
char *idx_to_letter_duo(int i);
char *idx_to_plate(int i);

int main()
{
    char in_plate[10];
    scanf("%9[^\n]", in_plate);
    int n;
    scanf("%d", &n);

    int idx = plate_to_idx(in_plate) + n;
    char *out_plate = idx_to_plate(idx);

    printf("%s\n", out_plate);

    return 0;
}

int letter_duo_to_idx(char *d) {
    return (d[0] - 'A') * 26 + d[1] - 'A';
}

int plate_to_idx(char *p) {
    int prefix = letter_duo_to_idx(p);
    int number = (p[3]-'0')*100 + (p[4]-'0')*10 + (p[5]-'0') - 1;
    int suffix = letter_duo_to_idx(p+7);
    return (prefix*676 + suffix)*999 + number;
}

char *idx_to_letter_duo(int i) {
    static char duo[3];
    div_t res = div(i, 26);
    snprintf(duo, sizeof duo, "%c%c", (char)(res.quot + 'A'), (char)(res.rem  + 'A'));
    return duo;
}

char *idx_to_plate(int i) {
    static char plate[10];
    div_t mod1 = div(i, 999);
    div_t mod2 = div(mod1.quot, 676);
    int number = mod1.rem + 1;
    char prefix[3], suffix[3];
    strcpy(prefix, idx_to_letter_duo(mod2.quot));
    strcpy(suffix, idx_to_letter_duo(mod2.rem));
    snprintf(plate, sizeof plate, "%s-%03d-%s", prefix, number, suffix);
    return plate;
}
