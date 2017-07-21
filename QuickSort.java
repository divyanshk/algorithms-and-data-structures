import java.io.*;
import java.util.*;

class QuickSort {

	// Partition algorithm: Swap elements from the left and right side of the pivot
	int partition(ArrayList<Integer> arr, int left, int right) {
		int pivot = arr.get((left+right)/2);
		while (left <= right) {
			while (arr.get(left)<pivot) left++;
			while (arr.get(right)>pivot) right--;			
			if (left<=right) {
				Collections.swap(arr, left, right);
				left++;
				right--;
			}
		}
		return left;
	}

	void quickSortUtil(ArrayList<Integer> arr, int low, int high) {
		if (low < high) {
			int partition_index = partition(arr, low, high);
			if (low < partition_index-1)
				quickSortUtil(arr, low, partition_index-1);
			if (partition_index < high)
				quickSortUtil(arr, partition_index+1, high);
		}
	}

	void quickSort(ArrayList<Integer> arr) {
		quickSortUtil(arr, 0, arr.size()-1);
	}

	public static void main(String args[]) {
		ArrayList<Integer> arr = new ArrayList<Integer>(Arrays.asList(100,45,67,12,10,2,3));
		QuickSort obj = new QuickSort();
		obj.quickSort(arr);
		System.out.println(arr);
	}
}