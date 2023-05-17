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
int n, m, sq, total;
int arr[MAX], bucker[1010], val[MAX * 10], res[MAX];

struct qry { int s, e, idx; };

bool operator < (qry &a, qry &b) {
        if (a.s / sq != b.s / sq) return a.s < b.s;
        return a.e < b.e;
    }

vector<qry> query;

void push(int num) {
    total -= val[num] * val[num] * num; val[num]++;
    total += val[num] * val[num] * num;
}

void pop(int num) { 
    total -= val[num] * val[num] * num; val[num]--;
    total += val[num] * val[num] * num;
}

void sol() {
    int a, b; cin >> n >> m; sq = sqrt(n); 
    for (int i = 1; i < n + 1; i++) cin >> arr[i];
    for (int i = 0; i < m; i++) cin >> a >> b, query.push_back({ a, b, i });
    sort(all(query));

    int lo = query[0].s, hi = query[0].e;

    for (int i = lo; i < hi + 1; i++) push(arr[i]);
    res[query[0].idx] = total;

    for (int i = 1; i < m; i++) {
        while (lo < query[i].s) pop(arr[lo++]);
        while (lo > query[i].s) push(arr[--lo]);
        while (hi < query[i].e) push(arr[++hi]);
        while (hi > query[i].e) pop(arr[hi--]);
        res[query[i].idx] = total;
    }

    for (int i = 0; i < m; i++) cout << res[i] << "\n";
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    sol();
}