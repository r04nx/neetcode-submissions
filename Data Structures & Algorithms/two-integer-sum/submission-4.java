class Solution {
    public int[] twoSum(int[] nums, int target) {

        Map<Integer, Integer> checkreg = new HashMap<>();

        for(int i=0;i<nums.length;i++){
            int complement = target-nums[i];

            if(checkreg.containsKey(complement)){
                    return new int[]{checkreg.get(complement),i};  
            }else{
                 checkreg.put(nums[i],i);
            }
           

        } 
        return new int[]{};
    }
}

