import java.io.*;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.StringTokenizer;
import static java.lang.System.out;

class Main {
  public static void galeShapley(LinkedList<Integer> fMentor, int[] cMentor, int[][] mPrefs, int[] nProp,
      int[][] rStudent) {
    /** Algorithm While Loop **/
    while (fMentor.size() > 0) {
      int pMentor = fMentor.poll();
      int offer = mPrefs[pMentor][nProp[pMentor]];
      if (cMentor[offer] == -1) {
        cMentor[offer] = pMentor;
      } else {
        if (rStudent[offer][cMentor[offer]] >= rStudent[offer][pMentor]) {
          fMentor.add(cMentor[offer]);
          cMentor[offer] = pMentor;
        } else {
          fMentor.add(0, pMentor);
        }
      }
      nProp[pMentor] = nProp[pMentor] + 1;
    }

    /** OUTPUT **/
    for (int c = 0; c < cMentor.length; c++) {
      if (cMentor[c] != -1) {
        out.print((mPrefs[cMentor[c]][0] + 1) + "\n");
      } else {
        out.print("0\n");
      }
    }
    out.close();
  }

  public static void main(String[] args) throws IOException {
    /** INPUT **/

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer tok = new StringTokenizer(br.readLine());

    /** Number of hospitals **/
    int m = Integer.parseInt(tok.nextToken());
    /** Number of students **/
    int n = Integer.parseInt(tok.nextToken());

    /** Capacity of Each Hospital **/
    int[] hCap = new int[m];
    int[] beforeSum = new int[m];
    int totalSlots = 0;
    for (int i = 0; i < m; i++) {
      tok = new StringTokenizer(br.readLine());
      hCap[i] = Integer.parseInt(tok.nextToken());
      beforeSum[i] = totalSlots;
      totalSlots += hCap[i];
    }

    /**
     * Mentor Preference List
     * makes a preference list for eahc mentor where the
     * first slot in eachlist is the hospital number they represent
     **/
    int[][] mPrefs = new int[n][n + 1];
    int cSlot = 0;
    for (int i = 0; i < m; i++) {
      tok = new StringTokenizer(br.readLine());
      int[] pref = new int[n + 1];
      Arrays.fill(pref, -1);
      pref[0] = i;
      for (int j = 1; j < n + 1; j++) {
        pref[j] = Integer.parseInt(tok.nextToken()) - 1;
      }
      for (int c = 0; c < hCap[i]; c++) {
        mPrefs[cSlot] = pref;
        cSlot++;
      }
    }

    /** Student Preference List **/
    int[][] sPrefs = new int[n][n];
    for (int i = 0; i < n; i++) {
      int[] pref = new int[n];
      Arrays.fill(pref, -1);
      tok = new StringTokenizer(br.readLine());
      int acc = 0;
      for (int j = 0; j < m; j++) {
        int p = Integer.parseInt(tok.nextToken()) - 1;
        for (int k = 0; k < hCap[p]; k++) {
          pref[acc] = beforeSum[p] + k; // beforeSum[p] + k; //p
          acc++;
        }
      }
      sPrefs[i] = pref;
    }

    // out.print("m" + m);
    // out.print("n" + n + "\n");
    // out.print("totalSlots" + totalSlots);
    // out.print("hCap" + Arrays.toString(hCap) + "\n");
    // for (int i = 0; i < mPrefs.length; i++) {
    // out.print("mPRefs" + Arrays.toString(mPrefs[i]) + "\n");
    // }
    // out.print("mPrefs Length" + mPrefs.length + "\n");

    // for (int i = 0; i < sPrefs.length; i++) {
    // out.print("sPRefs" + Arrays.toString(sPrefs[i]) + "\n");
    // }
    // out.print("sPrefs Length" + sPrefs.length + "\n");

    // ALGORITHM

    /** List of Next Proposals For Each Mentor **/
    int[] nProp = new int[n];
    Arrays.fill(nProp, 1);
    // out.print("nProp:" + Arrays.toString(nProp) + "\n");

    /** List of Current Mentors of Each Student **/
    int[] cMentor = new int[n];
    Arrays.fill(cMentor, -1);
    // out.print("nProp:" + Arrays.toString(cMentor) + "\n");

    /** Linked List of Free Mentors **/
    LinkedList<Integer> fMentor = new LinkedList<>();
    for (int c = 0; c < totalSlots; c++) {
      fMentor.add(c);
    }
    // for (Integer value : fMentor) {
    // out.println(value);
    // }

    /** List of Rankings for Each Student **/
    int[][] rStudent = new int[n][n];
    for (int r = 0; r < n; r++) {
      int[] rank = new int[n];
      for (int c = 0; c < n; c++) {
        int pref = sPrefs[r][c];
        if (pref != -1) {
          rank[pref] = c;
        } else {
          rank[c] = n - 1;
        }
      }
      rStudent[r] = rank;
    }
    galeShapley(fMentor, cMentor, mPrefs, nProp, rStudent);
  }

}