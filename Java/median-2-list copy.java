/**
 * Median of 2 Sorted Arrays
 */
class Solution {
  public static void main(String args[]) {
    int[] nums1 = { 1, 2, 3 };
    int[] nums2 = { 4, 5, 6, 7 };
    double med = findMedianSortedArrays(nums1, nums2);
    System.out.println(med + ": 4.0"); // should print out 4.0 {1, 2, 3, !4!, 5, 6, 7}
    int[] nums15 = { 1, 2, 3 };
    int[] nums25 = { 4, 5, 6, 7, 8 };
    double med5 = findMedianSortedArrays(nums15, nums25);
    System.out.println(med5 + ": 4.5"); // should print out 4.5 {1, 2, 3, !4, 5!, 6, 7, 8}
    int[] nums11 = { 1, 2, 5, 6 };
    int[] nums21 = { 3, 4, 6, 6, 7 };
    double med1 = findMedianSortedArrays(nums11, nums21);
    System.out.println(med1 + ": 5.0"); // should print out 5.0 {1, 2, 3, 4, !5!, 6, 6, 6, 7}
    int[] nums14 = { 1, 2, 5, 6, 9 };
    int[] nums24 = { 3, 4, 6, 6, 7 };
    double med4 = findMedianSortedArrays(nums14, nums24);
    System.out.println(med4 + ": 5.5"); // should print out 5.5 {1, 2, 3, 4, !5, 6!, 6, 6, 7, 9}
    int[] nums12 = {};
    int[] nums22 = { 3 };
    double med2 = findMedianSortedArrays(nums12, nums22);
    System.out.println(med2 + ": 3.0"); // should print out 3.0 {3}
    int[] nums13 = {};
    int[] nums23 = { 3, 4 };
    double med3 = findMedianSortedArrays(nums13, nums23);
    System.out.println(med3 + ": 3.5"); // should print out 3.5 {3, 4}
  }

  public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
    // Deal with invalid corner case.
    if (nums1 == null || nums2 == null || nums1.length == 0 || nums2.length == 0)
      return 0.0;

    int m = nums1.length, n = nums2.length;
    int l = (m + n + 1) / 2; // left half of the combined median
    int r = (m + n + 2) / 2; // right half of the combined median

    // If the nums1.length + nums2.length is odd, the 2 function will return the
    // same number
    // Else if nums1.length + nums2.length is even, the 2 function will return the
    // left number and right number that make up a median
    return (getKth(nums1, 0, nums2, 0, l) + getKth(nums1, 0, nums2, 0, r)) / 2.0;
  }

  private static double getKth(int[] nums1, int start1, int[] nums2, int start2, int k) {
    // This function finds the Kth element in nums1 + nums2

    // If nums1 is exhausted, return kth number in nums2
    if (start1 > nums1.length - 1)
      return nums2[start2 + k - 1];

    // If nums2 is exhausted, return kth number in nums1
    if (start2 > nums2.length - 1)
      return nums1[start1 + k - 1];

    // If k == 1, return the first number
    // Since nums1 and nums2 is sorted, the smaller one among the start point of
    // nums1 and nums2 is the first one
    if (k == 1)
      return Math.min(nums1[start1], nums2[start2]);

    int mid1 = Integer.MAX_VALUE;
    int mid2 = Integer.MAX_VALUE;
    if (start1 + k / 2 - 1 < nums1.length)
      mid1 = nums1[start1 + k / 2 - 1];
    if (start2 + k / 2 - 1 < nums2.length)
      mid2 = nums2[start2 + k / 2 - 1];

    // Throw away half of the array from nums1 or nums2. And cut k in half
    if (mid1 < mid2) {
      return getKth(nums1, start1 + k / 2, nums2, start2, k - k / 2); // nums1.right + nums2
    } else {
      return getKth(nums1, start1, nums2, start2 + k / 2, k - k / 2); // nums1 + nums2.right
    }
  }
}