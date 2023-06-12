#include <bits/stdc++.h>
#define int long long
#define ll long long
#define double long double
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
const int MAX = 1010;
int n, m, cnt, dsu[MAX * MAX];
string s = "RLUD";
set<int> st;

int dy[4] = { 0, 0, -1, 1 };
int dx[4] = { 1, -1, 0, 0 };

int find(int x) {
    if (dsu[x] != x) return dsu[x] = find(dsu[x]);
    return dsu[x];
}

void uni(int a, int b) {
    a = find(a), b = find(b);
    if (a < b) dsu[a] = b;
    else dsu[b] = a;
}

int get(int y, int x) {
    return m * y + x;
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    for (int i = 0; i < MAX * MAX; i++) dsu[i] = i;
    char tmp; int a;
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> tmp;
            for (int u = 0; u < 4; u++) if (s[u] == tmp) a = u;
            int y = i + dy[a], x = j + dx[a];
            uni(get(i, j), get(y, x));
        }
    }

    for (int i = 0; i < n * m; i++) {
        if (st.find(find(i)) == st.end()) st.insert(find(i)), cnt++;
    }

    cout << cnt;
}