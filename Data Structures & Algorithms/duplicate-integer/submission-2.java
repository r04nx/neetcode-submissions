
class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> checkset =  new HashSet<>();
        for(int i=0; i<nums.length; i++){
            if (checkset.contains(nums[i])){
                return true;
            }
            else{
                checkset.add(nums[i]);
            }
        }

     return false;   
    }
}