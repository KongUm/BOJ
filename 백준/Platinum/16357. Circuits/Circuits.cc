#include <bits/stdc++.h>

#define int long long
#define ll long long
using namespace std;
const int MAX = 200010;
int n;
vector<pair<int, int>> arr;
vector<int> v;
vector<pair<int, int>> box[MAX * 3];
int lazy[2][MAX * 4], segTree[2][MAX * 4];

void update_lazy(int start, int end, int node, int t) {
    if (lazy[t][node] != 0) {
        segTree[t][node] += lazy[t][node];
        if (start != end) {
            lazy[t][node * 2] += lazy[t][node];
            lazy[t][node * 2 + 1] += lazy[t][node];
        }
        lazy[t][node] = 0;
    }
}

void update(int start, int end, int node, int rl, int rr, int value, int t) {
    update_lazy(start, end, node, t);

    if (rr < start || rl > end) return;

    if (rl <= start && rr >= end) {
        segTree[t][node] += value;
        if (start != end) {
            lazy[t][node * 2] += value;
            lazy[t][node * 2 + 1] += value;
        }
        return;
    }

    int mid = (start + end) / 2;
    update(start, mid, node * 2, rl, rr, value, t);
    update(mid + 1, end, node * 2 + 1, rl, rr, value, t);
    segTree[t][node] = max(segTree[t][node * 2], segTree[t][node * 2 + 1]);
}

ll query(int start, int end, int node, int fl, int fr, int t) {
    update_lazy(start, end, node, t);

    if (fr < start || fl > end) return 0;
    if (fl <= start && fr >= end) return segTree[t][node];

    int mid = (start + end) / 2;
    long long l = query(start, mid, node * 2, fl, fr, t);
    long long r = query(mid + 1, end, node * 2 + 1, fl, fr, t);
    return max(l, r);
}


signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int x1, y1, x2, y2, cnt = 0;
    cin >> n;

    int ans = 0;

    for (int i = 0; i < n; i++) {
        cin >> x1 >> y1 >> x2 >> y2;
        arr.emplace_back(y1, y2);
        v.push_back(y1);
        v.push_back(y2);
    }
    // 좌표 압축
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(), v.end()), v.end());

    for (int i = 0; i < n; i++) {
        y2 = lower_bound(v.begin(), v.end(), arr[i].first) - v.begin() + 1;
        y1 = lower_bound(v.begin(), v.end(), arr[i].second) - v.begin() + 1;
        arr[i] = make_pair(y2, y1);
        box[y1].emplace_back(y1, y2);
        update(1, MAX, 1, y1, y2, 1, 0); // y1 ~ y2
        cnt += 1;
    }
    ans = query(1, MAX, 1, 1, MAX, 0);

    for (int i = 0; i < MAX * 3; i++) {
        for (auto p: box[i]) {
            update(1, MAX, 1, p.first, p.second, 1, 1); // 1번 세그에 추가
            update(1, MAX, 1, p.first, p.second, -1, 0); // 0번 세그에서 지우기
            int temp = query(1, MAX, 1, 1, MAX, 1) + query(1, MAX, 1, 1, MAX, 0);
            ans = max(temp, ans);

        }
    }

    cout << ans;

}