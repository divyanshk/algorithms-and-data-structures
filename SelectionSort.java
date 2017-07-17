import java.io.*;
import java.util.*;

class SelectionSort {
	void selectionSort(ArrayList<Integer> arr) {
		int n = arr.size();
		for (int i=0; i<n; i++) {
			int smallest_index = i;
			for (int j=i+1; j<n; j++) {
				if (arr.get(j) < arr.get(smallest_index)) {
					smallest_index = j;
				}
			}
			Collections.swap(arr, i, smallest_index);
		}
	}

	public static void main(String args[]){
		ArrayList<Integer> arr = new ArrayList<Integer>(Arrays.asList(100,45,67,12,10,2,3));
		SelectionSort obj = new SelectionSort();
		obj.selectionSort(arr);
		System.out.println(arr);
	}
}