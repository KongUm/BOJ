#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int n;
    cin >> n;
    int ans = 0;

    for (int i = 0; i < n; i++) {
        string str;
        cin >> str;
        stack<char> s;

        for (char j: str) {
            if (!s.empty() && s.top() == j) {
                s.pop();
            } else s.push(j);
        }
        if (s.empty()) ans += 1;
    }
    cout << ans;
    return 0;
}