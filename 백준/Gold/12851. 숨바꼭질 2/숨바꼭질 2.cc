#include <bits/stdc++.h>

using namespace std;

int visited[100001];
int cnt;

void bfs(int s, int K) {
    queue<pair<int, int>> q;
    for (int &i: visited) i = (int) -1;
    visited[s] = 0;
    q.emplace(s, 0);

    while (!q.empty()) {
        int u = q.front().first;
        int c = q.front().second;
        q.pop();

        if (visited[u] < 0) visited[u] = c;
        if (u == K && (visited[u] < 0 || visited[u] == c)) cnt++;

        int d[3] = {u - 1, u + 1, 2 * u};
        for (int i: d) {
            if (i >= 0 && i <= 100000 && visited[i] == -1) q.emplace(i, c + 1);
        }
    }
}

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int N, K;
    cin >> N >> K;
    bfs(N, K);
    cout << visited[K] << "\n" << cnt;
}