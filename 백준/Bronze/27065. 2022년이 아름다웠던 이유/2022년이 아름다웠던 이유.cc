#include <bits/stdc++.h>

using namespace std;

vector<int> factorization(int n) {
    vector<int> v;
    for (int i = 1; i <= (int) sqrt(n); i++) {
        if (n % i == 0) {
            v.push_back(i);
            if (i * i != n && i != 1) {
                v.push_back(n / i);
            }
        }
    }
    return v;
}

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int n;
        cin >> n;
        vector<int> v = factorization(n);
        bool checker = true;

        if (accumulate(v.begin(), v.end(), 0) <= n) {
            checker = false;
        }

        for (int j: v) {
            vector<int> temp = factorization(j);
            if (accumulate(temp.begin(), temp.end(), 0) > j) {
                checker = false;
            }
        }

        if (checker) {
            cout << "Good Bye" << "\n";
        } else {
            cout << "BOJ 2022" << "\n";
        }
    }
}
