class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currentSum = 0;
        int maximumSum = nums[0];

        for(int i = 0; i < nums.size(); i++)
        {
            currentSum += nums[i];

            maximumSum = max(maximumSum, currentSum);

            if(currentSum < 0)
            {
                currentSum = 0;
            }
        }

        return maximumSum;
        
    }
};

