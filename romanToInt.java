import java.util.HashMap;
import java.util.Map;

public class romanToInt {

    public int romanToInt(String s) {
        Map<Character, Integer> map = new HashMap();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);
        int prev = 1000; // holds the prev symbol, to check if we have special combi.
        // if the current val of key bigger the prev-val, check special comb
        int sum = 0;
        for (char ch : s.toCharArray()) {
            switch (ch) {
                case 'I':
                    sum += 1;
                    break;
                case 'V':
                    if (prev == 1) {
                        sum += 3;
                    } else {
                        sum += 5;
                    }
                    break;
                case 'X':
                    if (prev == 1) {
                        sum += 8;
                    } else {
                        sum += 10;
                    }
                    break;
                case 'L':
                    if (prev == 10) {
                        sum += 30;
                    } else {
                        sum += 50;
                    }
                    break;
                case 'C':
                    if (prev == 10) {
                        sum += 80;
                    } else {
                        sum += 100;
                    }
                    break;
                case 'D':
                    if (prev == 100) {
                        sum += 300;
                    } else {
                        sum += 500;
                    }
                    break;
                case 'M':
                    if (prev == 100) {
                        sum += 800;
                    } else {
                        sum += 1000;
                    }
                    break;
            }
            prev = ch;
        }
        return sum;
    }
}
