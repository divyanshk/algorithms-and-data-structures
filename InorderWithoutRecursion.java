import java.io.*;
import java.util.*;

class Node {

	int key;
	Node left, right;

	public Node(int value) {
		key = value;
		left = right = null;
	}

}

class InorderWithoutRecursion {

	void inorder(Node root) {

		if (root == null) {
			return;
		}

		Stack<Node> stk = new Stack<Node>();
		Node node = root;

		while (node != null) {
			stk.push(node);
			node = node.left;
		}

		while (stk.size() > 0) {
			node = stk.pop();
			System.out.print(node.key + " ");
			if (node.right != null) {
				node = node.right;
				while(node != null) {
					stk.push(node);
					node = node.left;
				}
			}
		}

	}

	public static void main(String args[]) {

		InorderWithoutRecursion tree = new InorderWithoutRecursion();
		Node root = new Node(1);
		root.left = new Node(2);
		root.left.left = new Node(4);
		root.left.right = new Node(5);
		root.right = new Node(3);
		tree.inorder(root);

	}
}