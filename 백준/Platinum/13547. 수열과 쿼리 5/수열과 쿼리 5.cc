#include <bits/stdc++.h>
#define int long long
#define ll long long
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
const int MAX = 100010;
int n, m, sq, a, b, arr[MAX], bucker[1010], cnt[MAX * 10], res[MAX];
int totalCnt;

struct query { int s, e, idx; };

bool operator < (query &a, query &b) {
        if (a.s / sq != b.s / sq) return a.s < b.s;
        return a.e < b.e;
    }

vector<query> v;

void push(int num) { if (cnt[num]++ == 0) totalCnt++; }
void pop(int num) { if (cnt[num]-- == 1) totalCnt--; }

void sol() {
    cin >> n; sq = sqrt(n);
    for (int i = 1; i < n + 1; i++) cin >> arr[i];
    cin >> m;
    for (int i = 0; i < m; i++) cin >> a >> b, v.push_back({ a, b, i });
    sort(all(v));

    int lo = v[0].s, hi = v[0].e;

    for (int i = lo; i < hi + 1; i++) push(arr[i]);
    res[v[0].idx] = totalCnt;

    for (int i = 1; i < m; i++) {
        while (lo < v[i].s) pop(arr[lo++]);
        while (lo > v[i].s) push(arr[--lo]);
        while (hi < v[i].e) push(arr[++hi]);
        while (hi > v[i].e) pop(arr[hi--]);
        res[v[i].idx] = totalCnt;
    }

    for (int i = 0; i < m; i++) cout << res[i] << "\n";
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    sol();
}