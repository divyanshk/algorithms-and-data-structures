import java.io.*;
import java.util.*;

class TrieNode {
		
	char key;
	boolean isLeaf;
	HashMap<Character, TrieNode> childMap = new HashMap<Character, TrieNode>();
	
	public TrieNode() { }

	public TrieNode(char key) {
		this.key = key;
	}

}

class Trie {
	
	private TrieNode root;

	public Trie() {
		this.root = new TrieNode();
	}

	public void insertKey(String s) {
		HashMap<Character, TrieNode> childMap = this.root.childMap;

		for (int i=0; i<s.length(); i++) {
			char c = s.charAt(i);
			TrieNode t;
			if (childMap.containsKey(c)) {
				t = childMap.get(c);
			}else {
				t= new TrieNode(c);
				if (i==s.length()-1)
					t.isLeaf = true;
				childMap.put(c, t);
			}
			childMap = t.childMap;
		}
	}

	public boolean searchKey(String s) {
		TrieNode t = this.root;
		for (int i=0; i<s.length(); i++) {
			char c = s.charAt(i);
			if (!t.childMap.containsKey(c)) {
				return false;
			}
			t = t.childMap.get(c);
		}
		if (t.isLeaf == true) {
			return true;
		}else {
			return false;
		}
	}


	public static void main(String args[]) {

		Trie trie = new Trie();
		trie.insertKey("at");
		trie.insertKey("hell");
		trie.insertKey("home");
		trie.insertKey("hello");
		trie.insertKey("apples");
		System.out.println(trie.searchKey("apple"));
		System.out.println(trie.searchKey("hello"));
	}

}