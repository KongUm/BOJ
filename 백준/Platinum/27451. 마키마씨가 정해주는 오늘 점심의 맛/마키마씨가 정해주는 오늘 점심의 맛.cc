#include <bits/stdc++.h>

#define int long long
#define ll long long
using namespace std;
using ti3 = tuple<int, int, int>;
const int MAX = 50;
int n, m;
int visited[MAX][MAX][MAX];
ti3 path[MAX][MAX][MAX];
vector<int> graph[MAX];
vector<int> route[3];

void init() {
    for (int i = 0; i < MAX; i++) {
        for (int j = 0; j < MAX; j++) {
            for (int u = 0; u < MAX; u++) visited[i][j][u] = -1;
        }
    }
}

int bfs(int sa, int sb, int sc) {
    init();
    queue<ti3> q;
    q.push({ sa, sb, sc });
    visited[sa][sb][sc] = 0;

    while (!q.empty()) {
        ti3 tp = q.front(); q.pop();
        int a = get<0>(tp), b = get<1>(tp), c = get<2>(tp);

        if (a == b && b == c) return a; 
        
        for (int i : graph[a]) {
            for (int j : graph[b]) {
                for (int u : graph[c]) {
                    if (visited[i][j][u] == -1) {
                        visited[i][j][u] = visited[a][b][c] + 1;
                        path[i][j][u] = { a, b, c };
                        q.push({ i, j, u });
                    }  
                }
            }
        }
    }
    return -1;
}

void getRoute(int sa, int sb, int sc, int dst) {
    int na = dst, nb = dst, nc = dst;
    for (int i = 0; i < 3; i++) route[i].push_back(dst);

    while (na != sa | nb != sb | nc != sc) {
        ti3 tp = path[na][nb][nc];
        na = get<0>(tp), nb = get<1>(tp), nc = get<2>(tp);
        route[0].push_back(na);
        route[1].push_back(nb);
        route[2].push_back(nc);
    }
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int sa, sb, sc, a, b;
    cin >> n >> m >> sa >> sb >> sc;

    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        graph[a].push_back(b);
    }
    int dst = bfs(sa, sb, sc);
    if (dst < 0) cout << -1;
    else {
        getRoute(sa, sb, sc, dst);
        
        cout << dst << " " << visited[dst][dst][dst] << "\n";
        for (int i = 0; i < 3; i++) {
            int sz = route[i].size();
            for (int j = sz - 1; j > -1; j--) cout << route[i][j] << " ";
            cout << "\n"; 
        }
    }
}