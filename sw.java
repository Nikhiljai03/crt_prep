// import java.util.HashSet;
// class sw{
//     public static void main(String[] args) {
//         HashSet<String> hs = new HashSet<>();
//         String s = "abacddcbkbb";
//         int k = 4;
//         String sub = "";
//         for(int i = 0;i < k;i++){
//             sub += s.charAt(i);
//         }
//         hs.add(sub);
//         System.out.println(hs);
        
//     }
// }
//  current_sum - l[i-k] + l[i]


import java.util.HashMap;
import java.util.Map;
class sw{
    public static void main(String[] args) {
        String s = "abacddcbkbb";
        int k = 4;
        int i = 0, j = 0;
        Map<Character, Integer> map = new HashMap<>();
        while (j < s.length()) {
            map.put(s.charAt(j), map.getOrDefault(s.charAt(j), 0) + 1);
            if (j - i + 1 < k) {
                j++;
            } else if (j - i + 1 == k) {
                if (map.size() == k) {
                    System.out.println(s.substring(i, j + 1));
                }
                map.put(s.charAt(i), map.get(s.charAt(i)) - 1);
                if (map.get(s.charAt(i)) == 0) {
                    map.remove(s.charAt(i));
                }
                i++;
                j++;
            }
        }
    }
}