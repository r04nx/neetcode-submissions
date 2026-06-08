class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }

        Map<Character, Integer> first = new HashMap<>();
        Map<Character,Integer> second = new HashMap<>();

        for (int i = 0; i<s.length(); i++){
            first.merge(s.charAt(i),1, Integer::sum);
            second.merge(t.charAt(i),1,Integer::sum);
        }

        return first.equals(second);

    }
}
