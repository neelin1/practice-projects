import java.io.*;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.StringTokenizer;
import static java.lang.System.out;

class Main {
  private static int n;
  private static int[][] memo;
  private static int[] radii;

  private static int recursivePegs(int l, int r) {
    if (memo[l][r] != -1) {
      return (memo[l][r]);
    }
    if (r - l == 2) {
      memo[l][r] = radii[l + 1];
      return radii[l + 1];
    }
    int max = 0;
    for (int m = l + 2; m <= r - 2; m++) {
      int hm = (l + 1) * m * (r - 1) + recursivePegs(l, m) + recursivePegs(m, r);
      if (hm > max) {
        max = hm;
      }
    }
    memo[l][r] = max;
    return max;
  }

  public static void main(String[] args) throws IOException {
    /** INPUT **/
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer tok = new StringTokenizer(br.readLine());

    // Number of Pegs
    n = Integer.parseInt(tok.nextToken());

    // Radii of Each Peg
    radii = new int[n];
    tok = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      radii[i] = Integer.parseInt(tok.nextToken());
    }

    // Memoization Array
    memo = new int[n][n];
    for (int i = 0; i < n; i++) {
      Arrays.fill(memo[i], -1);
    }

    // Checking Input
    // out.print("Number of Pegs: " + n + "\n");
    // out.print("Radii: " + Arrays.toString(radii) + "\n");

    /** ALGORITHM */
    out.print(recursivePegs(0, n + 1) + "\n");

  }

}