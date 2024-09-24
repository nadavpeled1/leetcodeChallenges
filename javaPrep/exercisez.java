package javaPrep;

import java.util.*;

public class exercisez {

    public static void main(String[] args) {
        System.out.println("Hello World");
        int k = 10;
        for (int i = 0; i < 10; i++) {
            System.out.println(i);
        }
    }

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public boolean wordPattern(String pattern, String s) {
        /**
         * 1) move pattern to char array, open a dict/hashmap for the key-values
         * 2) iterate over s, until null or space
         * 3) space case: trim the readed word, if in dict, check key-value match
         * null: return true if all were matched
         */
        String[] words = s.split(" ");
        if (words.length != pattern.length())
            return false;
        // go over p and listOfwords and check the maping
        Map wordsToChar = new HashMap();
        Map charToWords = new HashMap();

        for (int i = 0; i < words.length; i++) {
            char c = pattern.charAt(i);
            String word = words[i];

            if (!wordsToChar.containsKey(word))
                wordsToChar.put(word, c);

            if (!charToWords.containsKey(c))
                charToWords.put(c, word);

            if ((char) wordsToChar.get(word) != c || !charToWords.get(c).equals(word))
                return false;

        }
        return true;
    }

}
