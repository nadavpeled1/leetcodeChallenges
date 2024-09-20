
// Problem: 89. Gray Code
// leetcode: https://leetcode.com/problems/gray-code/

import java.util.*;

class Solution {

    public List<Integer> grayCode(int n) {
        List<Integer> rs = new ArrayList<Integer>();
        rs.add(0); // n=1 0
        for (int i = 0; i < n; i++) { // for each extra bit
            int size = rs.size(); // get the size of the list so far, a power of 2
            for (int k = size - 1; k >= 0; k--) // from the end to the start
                rs.add(rs.get(k) | 1 << i); // mirror the list and add 1 to the i-th bit
            // | 1<<i turns the i-th bit to 1 which is the MSB
        }
        return rs;
    }
}
