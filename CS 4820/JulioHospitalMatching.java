import java.io.*;
import java.util.LinkedList;
import java.util.StringTokenizer;
import java.util.Arrays;

class Main {

  public static int[] stableMatching(int m, int n, int[] capacity, int[][] hospitalPreferences,
      int[][] studentPreferences) {
    int[][] newStudentPreferences = new int[n][n];
    // for each student i, add the student's preferences

    for (int i = 0; i < n; i++) {
      int counter = 0;
      for (int j = 0; j < m; j++) {
        int hospital = studentPreferences[i][j];
        for (int k = 0; k < capacity[hospital - 1]; k++) {
          newStudentPreferences[i][counter] = studentPreferences[i][j];
          counter++;
        }
      }
    }

    int[][] ranking = new int[n][n];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (newStudentPreferences[i][j] > 0) {
          ranking[i][newStudentPreferences[i][j] - 1] = j;
        }
      }
    }

    LinkedList<Integer> freeMentors = new LinkedList<>();
    for (int i = m; i >= 1; i--) {
      for (int j = 0; j < capacity[i - 1]; j++) {
        freeMentors.addFirst(i);
      }
    }

    int[] next = new int[freeMentors.size()];
    int[] current = new int[n];

    while (freeMentors.size() > 0) {
      int m1 = freeMentors.getFirst();
      int s = hospitalPreferences[m1 - 1][next[m1 - 1]];

      if (current[s - 1] == 0) {
        current[s - 1] = m1;
        freeMentors.removeFirst();
      } else {
        int m2 = current[s - 1];
        if (ranking[s - 1][m1 - 1] < ranking[s - 1][m2 - 1]) {
          current[s - 1] = m1;
          freeMentors.removeFirst();
          freeMentors.addFirst(m2);
        } else {
          next[m1 - 1]++;
        }
      }
    }
    return current;
  }

  public static void main(String[] args) throws IOException {

    // f is the reader for the input file
    BufferedReader f = new BufferedReader(new InputStreamReader(System.in));

    PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
    // out is the writer for th e output file

    // st is the tokenizer for the input file.
    // A tokenizer breaks up the input file into tokens
    StringTokenizer st = new StringTokenizer(f.readLine());

    // m is the number of hospitals, n is the number of students
    int m = Integer.parseInt(st.nextToken());
    int n = Integer.parseInt(st.nextToken());

    // create an array to store the capacity of each hospital
    // we define each capacity based off the input file
    int[] capacity = new int[m];
    for (int i = 0; i < m; i++) {
      capacity[i] = Integer.parseInt(f.readLine());
    }

    // create a 2D array to store the preferences of each hospital
    // the length of the outer array is the number of hospitals,
    // the length of the inner array is the number of students
    int[][] hospitalPreferences = new int[m][n];
    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(f.readLine());
      for (int j = 0; j < n; j++) {
        hospitalPreferences[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    int[][] studentPreferences = new int[n][m];
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(f.readLine());
      for (int j = 0; j < m; j++) {
        studentPreferences[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    int[] assignments = stableMatching(m, n, capacity, hospitalPreferences, studentPreferences);
    // use out to make a standard output file
    for (int i = 0; i < n; i++) {
      out.printf("%d\n", assignments[i]);
    }
    out.close();
  }

}