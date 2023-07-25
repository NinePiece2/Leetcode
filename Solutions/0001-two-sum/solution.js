/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let out = []
    for (let i = 0; i < nums.length; i++){
        for (let j = 0; j < nums.length; j++){
            if (nums[i] + nums[j] == target && i != j){
                console.log('[' +i + ',' + j + ']')
                out[0] = i
                out[1] = j
                return out
                
            }
        }
    }
    return out
};
