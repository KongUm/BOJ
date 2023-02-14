#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int A[n];

    for (int i = 0; i < n; i++) cin >> A[i];

    if (n == 1) {
        cout << A[0];
    } else {
        sort(A, A + n);
        int s;
        s = accumulate(A, A + n, 0);
        cout << fixed << setprecision(6) << max((double) A[n - 2], (double) s / (double) n);
    }
    return 0;
}
