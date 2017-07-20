import java.io.*;
import java.util.*;

class RadixSort {

	void countingSort(int arr[], int exp) {
		int n = arr.length;
		int output[] = new int[n];
		int count[] = new int[10];
		Arrays.fill(count, 0);
		
		for (int i=0; i<n; i++)
			count[(arr[i]/exp)%10]++;

		for (int i=1; i<10; i++)
			count[i] += count[i-1];

        for (int i=n-1; i>=0; i--)
        {
            output[count[(arr[i]/exp)%10]-1] = arr[i];
            count[(arr[i]/exp)%10]--;
        }

        for (int i=0; i<n; i++)
            arr[i] = output[i];

	}

	void radixSort(int arr[]) {
		int max = Arrays.stream(arr).max().getAsInt();
		for (int exp=1; max/exp>0; exp*=10) {
			countingSort(arr, exp);
		}
	}

	public static void main(String args[]) {
		int arr[] = {100,45,67,12,10,2,3}; 
		RadixSort obj = new RadixSort();
		obj.radixSort(arr);
		System.out.println(Arrays.toString(arr));
	}
}