#include <bits/stdc++.h>

#define int long long

using namespace std;

const int N = 1001;

int A[N], arr[N];

signed main() {

    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    int n, temp, ans = 0;

    cin >> n;

    for (int i = 0; i < n; i++) cin >> A[i];

    for (int i = 0; i < n; i++) {

        cin >> temp;

        arr[i] = temp - A[i];

    }

    for (int i = 0; i < n; i++) {

        ans += abs(arr[i]);

        int target = arr[i];

        arr[i] = 0;

        if (target == 0) continue;

        for (int j = i + 1; j < n; j++) {

            if (target * arr[j] > 0) {

                if (abs(arr[j]) < abs(target)) target = arr[j];

                arr[j] -= target;

            } else break;

        }

    }

    cout << ans;

}