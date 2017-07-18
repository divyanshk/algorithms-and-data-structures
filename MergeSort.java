import java.io.*;
import java.util.*;

class MergeSort {

	private ArrayList<Integer> arr;
	private int[] helper;

	MergeSort(ArrayList<Integer> arr) {
		this.arr = arr;
		this.helper = new int[arr.size()];
	}

	void merge(int low, int middle, int high) {
		for (int i=low; i<=high; i++) {
			this.helper[i] = arr.get(i);
		}

		int helperLeft = low;
		int helperRight = middle+1;
		int current = low;

		while (helperLeft <= middle && helperRight <= high) {
			if (helper[helperLeft] <= helper[helperRight]) {
				arr.set(current, helper[helperLeft]);
				helperLeft++;
			}
			else {
				arr.set(current, helper[helperRight]);
				helperRight++;
			}
			current++;
		}

		for (int j=helperLeft; j<=middle; j++) {
			arr.set(current, helper[j]);
			current++;
		}	
	}

	void mergeSortUtil(int low, int high) {
		if (low < high) {
			int middle = low + (high - low)/2;
			mergeSortUtil(low, middle);
			mergeSortUtil(middle+1, high);
			merge(low, middle, high);
		}
	}

	void mergeSort() {
		mergeSortUtil(0, arr.size()-1);
	}

	public static void main(String args[]) {
		ArrayList<Integer> arr = new ArrayList<Integer>(Arrays.asList(100,45,67,12,10,2,3)); 
		MergeSort obj = new MergeSort(arr);
		obj.mergeSort();
		System.out.println(arr);
	}
}