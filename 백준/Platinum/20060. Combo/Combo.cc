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
        string tmp = now + alp[0] + alp[1] + now + alp[1] + alp[0];
        int ret = press(tmp); r--;

        if (ret == sz) now += alp[2];
        else if (ret == sz + 1) { // 둘 다 같은 경우 or 13 or 23
            tmp = now + alp[0] + alp[0]; r--;
            ret = press(tmp);
            if (ret == sz + 2) now = now + alp[0] + alp[0];
            else if (ret == sz + 1) now = now + alp[0] + alp[2];
            else {
                tmp = now + alp[1] + alp[1];
                ret = press(tmp); r--;
                if (ret == sz + 2) now = now + alp[1];
                else now = now + alp[1] + alp[2];
            }
        }
        else {
            tmp = now + alp[0] + alp[1]; r--;
            if (press(tmp) == sz + 2) now = now + alp[0] + alp[1];
            else now = now + alp[1] + alp[0];
        }
    }

    if (now.size() < N) {
        for (int i = 0; i < 3; i++) {
            if (press(now + alp[i]) == N) { now = now + alp[i]; break; } 
        }
        if (now.size() < N) now = now + alp[3];
    }

    return now;
}
