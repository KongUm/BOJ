#include <bits/stdc++.h>
#define int long long
#define ll long long
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
const int MAX = 100010, INF = 1e9 + 7;
int n, m, arr[MAX];

struct Node {
    int all, l, r, m;
};

struct Seg {
    Node segTree[MAX * 4];

    void init() {
        for (int i = 0; i < MAX * 4; i++) {
            segTree[i].all = 0;
            segTree[i].l = -INF;
            segTree[i].r = -INF;
            segTree[i].m = -INF;
        }
    }

    Node update(int start, int end, int node, int idx, int value) {
        if (idx < start || idx > end) return segTree[node];

        if (start == end) {
            segTree[node] = { value, value, value, value };
            return segTree[node];
        }

        int mid = (start + end) / 2; 
        Node lu = update(start, mid, node * 2, idx, value);
        Node ru = update(mid + 1, end, node * 2 + 1, idx, value);

        segTree[node].l = max(lu.l, lu.all + ru.l);
        segTree[node].r = max(ru.r, lu.r + ru.all);
        segTree[node].all = lu.all + ru.all;
        segTree[node].m = max(max(lu.m, ru.m), lu.r + ru.l);
        return segTree[node];
    }

    Node query(int start, int end, int node, int fl, int fr) {
        if (fr < start || fl > end) {
            Node tmp = {0, -INF, -INF, -INF};
            return tmp;
        }

        if (fl <= start && end <= fr) return segTree[node];

        int mid = (start + end) / 2;
        Node lq = query(start, mid, node * 2, fl, fr);
        Node rq = query(mid + 1, end, node * 2 + 1, fl, fr);
        Node qu;

        qu.l = max(lq.l, lq.all + rq.l);
        qu.r = max(rq.r, lq.r + rq.all);
        qu.all = lq.all + rq.all;
        qu.m = max(max(lq.m, rq.m), lq.r + rq.l);
        return qu;
    }
} seg0;


signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int s, e;
    cin >> n; 
    for (int i = 1; i < n + 1; i++) cin >> arr[i];
    seg0.init();
    for (int i = 1; i < n + 1; i++) seg0.update(1, n, 1, i, arr[i]);
    
    cin >> m;
    for (int q = 0; q < m; q++) {
        cin >> s >> e;
        cout << seg0.query(1, n, 1, s, e).m << "\n";
    }
}