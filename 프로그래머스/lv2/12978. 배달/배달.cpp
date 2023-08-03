#include <bits/stdc++.h>
#define fi first
#define se second
using namespace std;
using pii = pair<int, int>;

const int MAX = 100, INF = (int) 1e9 + 7;
int dist[MAX];
vector<pii> graph[MAX];

void dijkstra(int start) {
    for (int i = 0; i < MAX; i++) dist[i] = INF;
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    pq.push({ 0, start }); dist[start] = 0;

    while (!pq.empty()) {
        int cost = pq.top().first;
        int now = pq.top().second;
        pq.pop();

        if (cost > dist[now]) continue;

        for (auto i : graph[now]) {
            int nxt = i.first; // 다음 노드 
            int nxtCost = cost +  i.second; // 현재까지의 거리 + 간선의 가중치 
            if (nxtCost < dist[nxt]) {
                dist[nxt] = nxtCost;
                pq.push({ nxtCost, nxt });
            }
        }
    }
}

int solution(int N, vector<vector<int>> road, int K) {
    for (int i = 0; i < road.size(); i++) {
        int a = road[i][0], b = road[i][1], w = road[i][2];
        graph[a].push_back({ b, w }), graph[b].push_back({ a, w });
    }
    for (int i = 0; i < N + 1; i++) dist[i] = INF;
    dijkstra(1);
    int cnt = 0;
    for (int i = 1; i < N + 1; i++) if (dist[i] <= K) cnt++;
    
    return cnt;
}