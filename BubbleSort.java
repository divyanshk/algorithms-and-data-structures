import java.io.*;
import java.math.*;
import java.util.*;

class BubbleSort {

	static void BubbleSort(ArrayList<Integer> arr) {
		int n = arr.size();
		for (int i=0; i<n-1; i++) {
			for (int j=0; j<n-1-i; j++) {
				if (arr.get(j) > arr.get(j+1)) {
					Collections.swap(arr, j, j+1);
				}
			}
		}
	}

	public static void main(String args[]) {
		ArrayList<Integer> arr = new ArrayList<Integer>(Arrays.asList(100,45,67,12,10,2,3));
		BubbleSort(arr);
		System.out.println(arr);
 	}
}