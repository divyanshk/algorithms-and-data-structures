import java.io.*;
import java.util.*;

class ExponentialSearch {
	
	static int binarySearch(int[] arr, int low, int high, int x) {
		int mid;
		while (low <= high) {
			mid = low + (high - low)/2;
			if (arr[mid] == x) 
				return mid;
			else if (arr[mid] > x) 
				high = mid-1;
			else
				low = mid+1;
		}
		return -1;
	}

	static int exponentialSearch(int[] arr, int x) {
		int i=1, n = arr.length;

		if (arr[0] == x)
			return 0;

		while(i < n && arr[i] < n)
			i = i*2;

		return binarySearch(arr, i/2, Math.min(i,n), x);
	}

	public static void main(String args[]) {
		int key=10;
		int arr[] = {2,3,4,10,40,100};
		System.out.println(ExponentialSearch.exponentialSearch(arr, key));
	} 
}