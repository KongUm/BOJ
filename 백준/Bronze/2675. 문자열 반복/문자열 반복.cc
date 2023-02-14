#include <stdio.h>
#include <cstring>
using namespace std;

int main(){
    int T, R;
    char S[1000];

    scanf("%d", &T);
    for(int i = 0; i < T; i++){
        scanf("%d %s", &R, S);
        for(int j = 0; j < strlen(S); j++){
            for(int k = 0; k < R; k++) {printf("%c", S[j]);}
        }
        printf("\n");
    }
}