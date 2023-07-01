import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;
import static java.lang.System.out;

class Main {
  private static int n;
  private static int[][] memo;
  private static int[] radii;

  private static int recursivePegs(int l, int r) {
    if (l >= 0 && r <= n + 1 && memo[l][r] != -1) {
      return (memo[l][r]);
    }
    if (r - l == 2) {
      int max = radii[l] * radii[l + 1] * radii[r];
      memo[l][r] = max;
      // out.print(max + " ");
      return max;
    } else if (r - l < 2) {
      return (0);
    }
    int max = 0;
    for (int m = l + 1; m <= r - 1; m++) {
      int hm = radii[l] * radii[m] * radii[r] + recursivePegs(l, m) + recursivePegs(m, r);
      if (hm > max) {
        max = hm;
      }
    }
    memo[l][r] = max;
    // out.print(max + " ");
    return max;
  }

  public static void main(String[] args) throws IOException {
    /** INPUT **/
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer tok = new StringTokenizer(br.readLine());

    // Number of Pegs
    n = Integer.parseInt(tok.nextToken());

    // Radii of Each Peg
    radii = new int[n + 2];
    radii[0] = 1;
    radii[n + 1] = 1;
    tok = new StringTokenizer(br.readLine());
    for (int i = 1; i < n + 1; i++) {
      radii[i] = Integer.parseInt(tok.nextToken());
    }

    // Memoization Array
    memo = new int[n + 2][n + 2];
    for (int i = 0; i < n + 2; i++) {
      Arrays.fill(memo[i], -1);
    }

    // Checking Input
    // out.print("Number of Pegs: " + n + "\n");
    // out.print("Radii: " + Arrays.toString(radii) + "\n");
    // out.print("Memo: \n");
    // for (int i = 0; i < memo.length; i++) {
    // out.print(Arrays.toString(memo[i]) + "\n");
    // }

    /** ALGORITHM */
    out.print(recursivePegs(0, n + 1) + "\n");
    out.close();

  }

}