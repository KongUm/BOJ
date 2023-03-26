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
const int MAX = 2000010, INF = (int) 1e9 + 7;
int n, k;

struct sgt {
    int min, max;
};

sgt segTree[MAX * 4];
sgt lazy[MAX * 4];

sgt merge(sgt A, sgt B) {
    return { min(A.min, B.min), max(A.max, B.max) };
}

sgt prop(sgt A, int val, int typ) {
    if (typ == 1) A.min = max(A.min, val); // Query 1
    else A.max = min(A.max, val);          // Query 2

    if (A.min > A.max) return { val, val };
    else return { A.min, A.max };
}

void update_lazy(int st, int ed, int nd) {
    if (lazy[nd].min != -1) {
        segTree[nd] = prop(segTree[nd], lazy[nd].min, 1); // min 업데이트 (typ 1);
        if (st != ed) {
            lazy[nd * 2] = prop(lazy[nd * 2], lazy[nd].min, 1);
            lazy[nd * 2 + 1] = prop(lazy[nd * 2 + 1], lazy[nd].min, 1);
        }
        lazy[nd].min = -1;
    }

    if (lazy[nd].max != INF) {
        segTree[nd] = prop(segTree[nd], lazy[nd].max, 2); // max 업데이트 (typ 2);
        if (st != ed) {
            lazy[nd * 2] = prop(lazy[nd * 2], lazy[nd].max, 2);
            lazy[nd * 2 + 1] = prop(lazy[nd * 2 + 1], lazy[nd].max, 2);
        }
        lazy[nd].max = INF;
    }
} 

void update(int st, int ed, int nd, int ul, int ur, int val, int typ) {
    update_lazy(st, ed, nd);

    if (ur < st || ed < ul) return;

    if (ul <= st && ed <= ur) {
        segTree[nd] = prop(segTree[nd], val, typ); 
        if (st != ed) { // 하위 노드 lazy에 전파
            lazy[nd * 2] = prop(lazy[nd * 2], val, typ);
            lazy[nd * 2 + 1] = prop(lazy[nd * 2 + 1], val, typ);
        }
        return ;
    }

    int mid = (st + ed) / 2;
    update(st, mid, nd * 2, ul, ur, val, typ);
    update(mid + 1, ed, nd * 2 + 1, ul, ur, val, typ);
    segTree[nd] = merge(segTree[nd * 2], segTree[nd * 2 + 1]);
}

sgt query(int st, int ed, int nd, int fl, int fr) {
    update_lazy(st, ed, nd);

   if (fr < st || fl > ed) return { INF, -1 };
   if (fl <= st && fr >= ed) return segTree[nd];

   int mid = (st + ed) / 2;
   sgt l = query(st, mid, nd * 2, fl, fr);
   sgt r = query(mid + 1, ed, nd * 2 + 1, fl, fr);
   return merge(l, r);
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int q, l, r, h;
    cin >> n >> k;

    for (int i = 0; i < MAX * 4; i++) lazy[i] = { -1, INF };

    for (int i = 0; i < k; i++) {
        cin >> q >> l >> r >> h;
        update(0, n - 1, 1, l, r, h, q);
    }

    for (int i = 0; i < n; i++) {
        sgt tmp = query(0, n - 1, 1, i, i);
        cout << tmp.min << "\n";
    }
}