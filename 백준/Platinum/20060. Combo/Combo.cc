#include "combo.h"
using namespace std;


string guess_sequence(int N) {
    int r = N + 2;
    string now, alp, bt = "ABXY";
    
    for (int i = 0; i < 3; i++) {
        string tmp = ""; tmp += bt[i], r--;
        if (press(tmp) == 1) { now += bt[i]; break; }
    }
    if (now.size() == 0) now += bt[3];

    for (int i = 0; i < 4; i++) if (now[0] != bt[i]) alp += bt[i];

    while (now.size() < N - 1) { // r 조건 추가 필요
        int sz = now.size();
        string tmp;
        tmp = tmp + now + alp[0] + alp[0];
        tmp = tmp + now + alp[1] + alp[0];
        tmp = tmp + now + alp[1] + alp[1];
        
        int ret = press(tmp); r--;

        if (ret == sz) now += alp[2];
        else if (ret == sz + 1) { // AB AX BX
            tmp = now + alp[0] + alp[1]; // AB press
            ret = press(tmp);
            if (ret == sz) now = now + alp[1] + alp[2]; // BX
            else if (ret == sz + 1) now = now + alp[0] + alp[2]; // AX
            else now = now + alp[0] + alp[1]; // AB
        }
        else { // AA BA BB
            tmp = now + alp[1] + alp[0]; // BA press
            ret = press(tmp);
            if (ret == sz) now = now + alp[0] + alp[0]; // AA
            else if (ret == sz + 1) now = now + alp[1] + alp[1]; // BB
            else now = now + alp[1] + alp[0]; // BA
        }

    }

    if (now.size() < N) {
        for (int i = 0; i < 2; i++) {
            if (press(now + alp[i]) == N) { now = now + alp[i]; break; } 
        }
        if (now.size() < N) now = now + alp[2];
    }
    return now;
}

