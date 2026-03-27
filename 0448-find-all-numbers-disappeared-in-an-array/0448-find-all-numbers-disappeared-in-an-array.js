/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    const n = nums.length;
    const exist = new Array(n+1).fill(false);
    
    for (const num of nums) {
        exist[num] = true;
    }

    const result = [];
    for (let i = 1; i <= n; i++) {
        if (!exist[i]) result.push(i);
    }

    return result;
};