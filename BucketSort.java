import java.io.*;
import java.util.*;

class BucketSort {

	void bucketSort(float arr[]) {

		int n = arr.length;
		Map<Integer, List<Float>> buckets = new HashMap<Integer, List<Float>>();
		for (int i=0; i<n; ++i) {
			int key = (int)(n*arr[i]);
			if (!buckets.containsKey(key))
				buckets.put(key, new ArrayList<Float>());
			buckets.get(key).add(arr[i]);
		}

		buckets.forEach( (k,v) -> Collections.sort(v) );

		int index = 0;
		for (Map.Entry<Integer, List<Float>> pair : buckets.entrySet()) {
			for (Float elem: pair.getValue()) {
				arr[index++] = elem;
			}
		}
	}

	public static void main(String args[]) {
		float arr[] = {0.897f, 0.565f, 0.656f, 0.1234f, 0.665f, 0.3434f};
		BucketSort obj = new BucketSort();
		obj.bucketSort(arr);
		System.out.println(Arrays.toString(arr));
	}

}