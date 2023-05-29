#include <bits/stdc++.h>

#define MAX 2000001

#define INF 987654321

using namespace std;

struct node {

    int min, max;

    node() {min = max = 0;}

    node(int n, int m) : min(n), max(m) {}

};

const int TREE_MAX = 1 << (int)(ceil(log2(MAX) + 1));

node seg[TREE_MAX];

node lazy[TREE_MAX] = {node(-1, INF), };

int n, q;

/*

    lazy propagation

*/

node add(node curr, int val) {

   // curr.max = max(curr.max, val);

    curr.min = max(curr.min, val);

    if(curr.min > curr.max) curr.min = curr.max = val;

    return {curr.min, curr.max};

}

node sub(node curr, int val) {    

    curr.max = min(curr.max, val);

   // curr.min = min(curr.min, val);

    if(curr.min > curr.max) curr.min = curr.max = val;

    return {curr.min, curr.max};

}

void im_feeling_lazy(int curr, int start, int end) {

    if(lazy[curr].min != -1) {

        seg[curr] = add(seg[curr], lazy[curr].min);

         if(start != end) {

            lazy[curr*2] = add(lazy[curr*2], lazy[curr].min);

            lazy[curr*2+1] = add(lazy[curr*2+1], lazy[curr].min);

         }

         lazy[curr].min = -1;

    }

    

    if(lazy[curr].max != INF) {

        seg[curr] = sub(seg[curr], lazy[curr].max);

        if(start != end) {

            lazy[curr*2] = sub(lazy[curr*2], lazy[curr].max);

            lazy[curr*2+1] = sub(lazy[curr*2+1], lazy[curr].max);

        }

        lazy[curr].max = INF;

    }

}

 

void update(int curr, int start, int end, int t_start, int t_end, int arg, int val){

    im_feeling_lazy(curr, start, end);

    if(t_end < start || end < t_start) return;

    if(t_start <= start && end <= t_end) {

        if(arg == 1){

            seg[curr] = add(seg[curr], val);

            lazy[curr*2] = add(lazy[curr*2], val);

            lazy[curr*2+1] = add(lazy[curr*2+1], val); 

        } else {

            seg[curr] = sub(seg[curr], val);

            lazy[curr*2] = sub(lazy[curr*2], val);

            lazy[curr*2+1] = sub(lazy[curr*2+1], val);

        }

        return;

    }

    

    int mid = (start + end) >> 1;

    update(curr * 2, start, mid, t_start, t_end, arg, val);

    update(curr * 2 + 1, mid + 1, end, t_start, t_end, arg, val);

    seg[curr].min = min(seg[curr*2].min, seg[curr*2+1].min);

    seg[curr].max = max(seg[curr*2].max, seg[curr*2+1].max);

}

void getHeight(int curr, int start, int end, int idx) {

    im_feeling_lazy(curr, start, end);

    if(idx < start || end < idx) return;

    if(start == end) {

      cout<<seg[curr].max<<'\n';

      return;

    }

    

    int mid = (start + end) >> 1;

    getHeight(curr*2, start, mid, idx);

    getHeight(curr*2+1, mid+1, end, idx);

}

void fastIO() {

    ios::sync_with_stdio(false); cin.tie(0);

}

void input(){

    cin>>n;

}

void solve() {

    int arg, l, r, v;

    cin>>q;

    for(int i = 0; i < q; i++) {

        cin>>arg>>l>>r>>v;

        if(arg == 1) {

            update(1, 0, n-1, l, r, 1, v);

        } else {

            update(1, 0, n-1, l, r, 2, v);

        } 

    }

    

    for(int i = 0; i<n; i++) {

        getHeight(1, 0, n-1, i);

    }

}

int main() {

    fastIO();

    input();

    solve();

    return 0;

}