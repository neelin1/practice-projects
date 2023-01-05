package foobar;

// import org.junit.Test;
// import static org.junit.Assert.assertEquals;

import java.util.HashMap;
import java.util.Arrays;
import java.util.ArrayList;

public class Solution {
  public static int[] solution(int[] data, int n) {
    if (n == 0) {
      return (new int[0]);
    }
    HashMap<Integer, Integer> numbers = new HashMap<Integer, Integer>();
    ArrayList<Integer> arr = new ArrayList<Integer>();
    for (int i = 0; i < data.length; i++) {
      Integer val = numbers.get(data[i]);
      if (val == null) {
        arr.add(data[i]);
        numbers.put(data[i], 1);
      } else if (val < n) {
        arr.add(data[i]);
        numbers.replace(data[i], val += 1);
      } else {
        if (val == n) {
          for (int j = 0; j < arr.size(); j++) {
            if (arr.get(j) == data[i]) {
              arr.remove(j);
              j = j - 1;
            }
          }
        }
      }
    }
    return (arr.stream().mapToInt(j -> j).toArray());
  }

  // @Test
  // public void test() {
  // int[] list1 = { 1, 2, 3 };
  // System.out.println(solution(list1, 1));
  // // assertEquals(list1, solution(list1, 1));
  // }

  public static void main(String[] args) {
    int[] list1 = { 1, 2, 3 };
    int[] list2 = { 1, 1, 2, 3, 3, 3, 4 };
    int[] list3 = { 1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 5, 5 };
    System.out.println(Arrays.toString(solution(list1, 0)));
    System.out.println(Arrays.toString(solution(list1, 1)));
    System.out.println(Arrays.toString(solution(list1, 2)));
    System.out.println(Arrays.toString(solution(list2, 0)));
    System.out.println(Arrays.toString(solution(list2, 1)));
    System.out.println(Arrays.toString(solution(list2, 2)));
    System.out.println(Arrays.toString(solution(list2, 3)));
    System.out.println(Arrays.toString(solution(list2, 4)));
    System.out.println(Arrays.toString(solution(list3, 0)));
    System.out.println(Arrays.toString(solution(list3, 1)));
    System.out.println(Arrays.toString(solution(list3, 2)));
    System.out.println(Arrays.toString(solution(list3, 3)));
    System.out.println(Arrays.toString(solution(list3, 4)));
    System.out.println(Arrays.toString(solution(list3, 5)));
  }
}