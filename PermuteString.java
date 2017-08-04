import java.io.*;
import java.util.*;

class PermuteString {

	public static void permute(String s, int l, int r) {
		if (l == r) {
			System.out.println(s);
		}
		else {
			for (int i=l; i<=r; ++i) {
				s = swap(s, i, l);
				permute(s, l+1, r);
				s = swap(s, i, l);
			} 
		}
	}

	public static String swap(String a, int i, int j) {

        char temp;
        char[] charArray = a.toCharArray();
        temp = charArray[i] ;
        charArray[i] = charArray[j];
        charArray[j] = temp;
        return String.valueOf(charArray);
    
    }

	public static void main(String args[]) {

		String str = "ABC";
		PermuteString.permute(str, 0, str.length()-1);

	}

}