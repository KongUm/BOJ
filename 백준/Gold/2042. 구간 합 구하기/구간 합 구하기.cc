#include <bits/stdc++.h>

# define MAX 1000001
# define int long long

using namespace std;

int arr[MAX];
int tree[MAX * 4]; // 4를 곱하면 모든 범위를 커버할 수 있음. 갯수에 대해서 2의 제곱 형태의 길이를 가지기 때문임.


int init(int start, int end, int node) {
    if (start == end) return tree[node] = arr[start];
    int mid = (start + end) / 2;

    return tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1);
}


int find(int start, int end, int node, int fl, int fr) {

    if (fl > end || fr < start) return 0;

    if (fl <= start && end <= fr) return tree[node];

    int mid = (start + end) / 2;
    return find(start, mid, node * 2, fl, fr) + find(mid + 1, end, node * 2 + 1, fl, fr);
}


void update(int start, int end, int node, int index, int dif) {

    if (index < start || index > end) return;
    tree[node] += dif;

    if (start == end) return;

    int mid = (start + end) / 2;
    update(start, mid, node * 2, index, dif);
    update(mid + 1, end, node * 2 + 1, index, dif);
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int n, m, k;
    cin >> n >> m >> k;
    arr[0] = 0;
    for (int i = 1; i < n + 1; i++) cin >> arr[i];
    init(1, n, 1);

    for (int i = 0; i < m + k; i++) {
        int q, a, b;
        cin >> q >> a >> b;
        if (q == 1) {
            update(1, n, 1, a, b - arr[a]);
            arr[a] = b;
        } else {
            cout << find(1, n, 1, a, b) << "\n";
        }
    }
    return 0;
}