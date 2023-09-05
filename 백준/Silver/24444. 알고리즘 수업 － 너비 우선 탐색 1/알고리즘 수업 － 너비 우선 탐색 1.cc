#include <bits/stdc++.h>
#define all(a) (a).begin(), (a).end()

using namespace std;
const int MAX = 100010;
int n, m, r, vis[MAX], cnt;
vector<int> graph[MAX];
queue<int> que;
// graph[i] = 노드 i와 연결되어 있는 노드의 번호들이 들어있는 리스트
// visited[i] = 0 : 노드 i를 방문하지 않았음
// visited[i] = n : 노드 i를 n번째에 방문했음

void bfs(int st) {
    vis[st] = ++cnt; 
    que.push(st);

    while (que.size() > 0) {
        int cur = que.front(); que.pop();
        for (int nxt : graph[cur]) {
            if (vis[nxt] == 0) {
                vis[nxt] = ++cnt;
                que.push(nxt);
            }
        }
    }
}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int a, b;
    cin >> n >> m >> r;
    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        graph[a].push_back(b), graph[b].push_back(a);
    }

    for (int i = 1; i < n + 1; i++) sort(graph[i].begin(), graph[i].end());
    bfs(r);
    for (int i = 1; i < n + 1; i++) cout << vis[i] << " ";
}