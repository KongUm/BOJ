#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    long long n;
    cin >> n;
    vector<long long> v;


    for (int i = 0; i < n; i++) {
        string str;
        cin >> str;
        reverse(str.begin(), str.end());
        long long result = stoll(str);
        v.push_back(result);
    }
    sort(v.begin(), v.end());

    for (long long i: v) {
        cout << i << "\n";
    }
    return 0;
}