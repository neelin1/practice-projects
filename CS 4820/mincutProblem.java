import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.StringTokenizer;
import static java.lang.System.out;

class Main {
  /**
   * number of nodes in G
   */
  private static int n;
  /**
   * number of edges in G
   */
  private static int m;

  private static int[] scores;
  private static int[][] graph;
  private static int[][] r_graph;

  private static boolean bfs(int[][] r_G, int s, int t, int parent[], int np) {
    // Source: Geeks for Geeks
    // Create a visited array and mark all vertices as
    // initialize to not visited
    boolean visited[] = new boolean[np];
    for (int i = 0; i < np; ++i)
      visited[i] = false;

    // Create a queue, enqueue source vertex and mark
    // source vertex as visited
    LinkedList<Integer> queue = new LinkedList<Integer>();
    queue.add(s);
    visited[s] = true;
    parent[s] = -1;

    // Standard BFS Loop
    while (queue.size() != 0) {
      int u = queue.poll();

      for (int v = 0; v < np; v++) {
        if (visited[v] == false
            && r_G[u][v] > 0) {
          // If we find a connection to the sink
          // node, then there is no point in BFS
          // anymore We just have to set its parent
          // and can return true
          if (v == t) {
            parent[v] = u;
            return true;
          }
          queue.add(v);
          parent[v] = u;
          visited[v] = true;
        }
      }
    }

    // We didn't reach sink in BFS starting from source,
    // so return false
    return false;
  }

  private static int[][] fordFulkersonResidualGraph(int[][] G, int s, int t) {
    // Inspired by Geeks for Geek Pseudocode
    int u, v;

    int r_G[][] = new int[n][n];

    for (u = 0; u < n; u++)
      for (v = 0; v < n; v++)
        r_G[u][v] = G[u][v];

    int parent[] = new int[n];

    int max_flow = 0;

    while (bfs(r_G, s, t, parent, n)) {
      int path_flow = Integer.MAX_VALUE;
      for (v = t; v != s; v = parent[v]) {
        u = parent[v];
        path_flow = Math.min(path_flow, r_G[u][v]);
      }

      for (v = t; v != s; v = parent[v]) {
        u = parent[v];
        r_G[u][v] -= path_flow;
        r_G[v][u] += path_flow;
      }

      max_flow += path_flow;
    }

    return r_G;
  }

  private static int fordFulkerson(int[][] G, int s, int t, int np) {
    // Inspired by Geeks for Geeks Pseudocode
    int u, v;

    int r_G[][] = new int[np][np];

    for (u = 0; u < np; u++)
      for (v = 0; v < np; v++)
        r_G[u][v] = G[u][v];

    int parent[] = new int[np];

    int max_flow = 0;

    while (bfs(r_G, s, t, parent, n + 2)) {
      int path_flow = Integer.MAX_VALUE;
      for (v = t; v != s; v = parent[v]) {
        u = parent[v];
        path_flow = Math.min(path_flow, r_G[u][v]);
      }

      for (v = t; v != s; v = parent[v]) {
        u = parent[v];
        r_G[u][v] -= path_flow;
        r_G[v][u] += path_flow;
      }

      max_flow += path_flow;
    }

    return max_flow;
  }

  private static HashSet<Integer> bfsAT(int[][] r_G, int s) {
    HashSet<Integer> AT = new HashSet<>();

    boolean visited[] = new boolean[n];
    for (int i = 0; i < n; ++i)
      visited[i] = false;

    LinkedList<Integer> queue = new LinkedList<Integer>();
    queue.add(s);
    visited[s] = true;
    AT.add(s);

    while (queue.size() != 0) {
      int u = queue.poll();
      AT.add(u);
      for (int v = 0; v < n; v++) {
        if (visited[v] == false
            && r_G[u][v] > 0) {
          queue.add(v);
          visited[v] = true;
        }
      }
    }

    return AT;
  }

  public static int[][] transpose(int[][] r_G) {
    int[][] r_Gt = new int[n][n];

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        r_Gt[i][j] = r_G[j][i];
      }
    }

    return r_Gt;
  }

  public static void main(String[] args) throws IOException {
    /** INPUT **/
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer tok = new StringTokenizer(br.readLine());

    // Number of nodes
    n = Integer.parseInt(tok.nextToken());
    // Number of edges
    m = Integer.parseInt(tok.nextToken());

    // Score of each node
    scores = new int[n];
    tok = new StringTokenizer(br.readLine());
    for (int i = 1; i < n; i++) {
      scores[i - 1] = Integer.parseInt(tok.nextToken());
    }

    // Graph
    graph = new int[n][n];
    for (int i = 0; i < m; i++) {
      tok = new StringTokenizer(br.readLine());
      int startNode = Integer.parseInt(tok.nextToken());
      int endNode = Integer.parseInt(tok.nextToken());
      int capacity = Integer.parseInt(tok.nextToken());
      graph[startNode - 1][endNode - 1] = capacity;
    }

    // Checking Input
    // out.print("Number of Nodes: " + n + "\n");
    // out.print("Number of Edges: " + m + "\n");
    // out.print("Capacities " + Arrays.toString(scores) + "\n");
    // out.print("Graph:: \n");
    // for (int i = 1; i < n; i++) {
    // out.print(Arrays.toString(graph[i]) + "\n");
    // }

    /** ALGORITHM */

    // Running Ford Fulkerson
    r_graph = fordFulkersonResidualGraph(graph, 0, n - 1);

    // Checking residual graph
    // for (int i = 1; i < n; i++) {
    // out.print(Arrays.toString(r_graph[i]) + "\n");
    // }

    // Creating A_s and B_t
    HashSet<Integer> A_s = bfsAT(r_graph, 0);

    int[][] r_graph_transpose = transpose(r_graph);

    HashSet<Integer> B_t = bfsAT(r_graph_transpose, n - 1);

    // Creating V_p
    ArrayList<Integer> Vp = new ArrayList<Integer>();
    for (int i = 0; i < n; i++) {
      if (!A_s.contains(i) && !B_t.contains(i)) {
        Vp.add(i);
      }
    }

    // Creating C
    int C = 0;
    for (int i = 0; i < Vp.size(); i++) {
      int val = Vp.get(i);
      if (scores[val] > 0) {
        C += scores[val];
      }
    }
    int[][] ps_graph = new int[n + 2][n + 2];
    for (int i = 0; i < Vp.size(); i++) {
      int val = Vp.get(i);
      if (scores[val] < 0) {
        ps_graph[val][n + 1] = -1 * scores[val];
      } else if (scores[val] > 0) {
        ps_graph[n][val] = scores[val];
      }
      for (int j = 0; j < Vp.size(); j++) {
        if (j != i && r_graph[val][Vp.get(j)] != 0) {
          ps_graph[val][Vp.get(j)] = C + 1;
        }
      }
    }
    // for (int i = 1; i < n + 2; i++) {
    // out.print(Arrays.toString(ps_graph[i]) + "\n");
    // }

    int val_A_s = 0;
    for (Integer i : A_s) {
      val_A_s += scores[i];
    }

    int maxMinCut = val_A_s + C - fordFulkerson(ps_graph, n, n + 1, n + 2);

    // Solution
    out.println(maxMinCut);
    out.close();

  }

}