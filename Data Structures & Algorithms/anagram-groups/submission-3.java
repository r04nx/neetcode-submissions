class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

         Map<String, List<String>> ans = new HashMap<>();

        for(String s: strs){
            char[] strs_array = s.toCharArray();
            Arrays.sort(strs_array);

            String key = new String(strs_array);

            ans.computeIfAbsent(key, k -> new ArrayList<String>());
            ans.get(key).add(s);
        }

        return new ArrayList<>(ans.values());
        
    }
}
