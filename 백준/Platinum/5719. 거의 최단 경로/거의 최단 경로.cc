#include <bits/stdc++.h>
#define int long long
#define debug(x) cout << (#x) << ": " << (x) << '\n'

using namespace std;
using pii = pair<int, int>;
const int MAX = 510, INF = (int) 1e9 + 7;

vector<pii> graph[MAX], revGraph[MAX]; // 인접 리스트
int dist[MAX]; // 최단 거리 테이블, 경로 테이블 
int n, m, st, ed;
bool checker[MAX][MAX];

void init() {
    for (int i = 0; i < n + 10; i++) {
        dist[i] = INF;
        graph[i].clear();
        revGraph[i].clear();
        //for (int j = 0; j < n + 1; j++) checker[i][j] = false;
    }
}

void dijkstra(int start) {
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    pq.push({ 0, start }); dist[start] = 0;

    while (!pq.empty()) {
        int cost = pq.top().first;
        int now = pq.top().second;
        pq.pop();

        if (cost > dist[now]) continue;
        // 이미 구한 거리가 더 짧으면 무시 

        for (auto i : graph[now]) {
            int nxt = i.first; // 다음 노드 
            int nxtCost = cost +  i.second; // 현재까지의 거리 + 간선의 가중치 
            if (nxtCost < dist[nxt] && i.second != INF) {
                dist[nxt] = nxtCost;
                pq.push({ nxtCost, nxt });
            }
        }
    }
}


void revDijkstra(int start) {
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    pq.push({ 0, start }); dist[start] = 0;

    while (!pq.empty()) {
        int cost = pq.top().first;
        int now = pq.top().second;
        pq.pop();

        if (cost > dist[now]) continue;
        // 이미 구한 거리가 더 짧으면 무시 

        for (auto i : revGraph[now]) {
            int nxt = i.first; // 다음 노드 
            int nxtCost = cost +  i.second; // 현재까지의 거리 + 간선의 가중치 
            if (nxtCost < dist[nxt] && i.second != INF) {
                dist[nxt] = nxtCost;
                pq.push({ nxtCost, nxt });
            }
        }
    }
}

void bfs(int start, int end) {
    queue<int> q; q.push(end);
    
    while (!q.empty()) {
        int u = q.front(); q.pop();
        int sz = revGraph[u].size();

        for (int i = 0; i < sz; i++) {
            int nxt = revGraph[u][i].first, w = revGraph[u][i].second;
            if (dist[nxt] + w == dist[u]) {
                q.push(nxt); revGraph[u][i].second = INF;
                // checker[nxt][u] = true;
                // cout << nxt << " -> " << u << "\n";
            }
        }
    }
}

void edgeErase() {
    for (int i = 0; i < n + 1; i++) {
        int sz = graph[i].size();
        for (int j = 0; j < sz; j++) {
            int nxt = graph[i][j].first;
            //cout << i << " >> " << nxt << "\n";
            if (checker[i][nxt]) {
                graph[i][j].second = INF;
                //cout << i << " -> " << nxt << "\n";
            }        
        }
    }
    
}


void solution() {
    int a, b, w;
    cin >> st >> ed;
    init();
    for (int i = 0; i < m; i++) {
        cin >> a >> b >> w;
        graph[a].push_back({ b, w });
        revGraph[b].push_back({ a, w });
    }
    dijkstra(st);
    bfs(st, ed);
    for (int i = 0; i < n + 1; i++) dist[i] = INF;
    revDijkstra(ed);

    if (dist[st] >= INF) cout << -1 << "\n";
    else cout << dist[st] << "\n";

}

signed main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    
    while (true) {
        cin >> n >> m;
        if (n == 0 && m == 0) break; 
        solution();
    }
}

