/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findErrorNums = function(nums) {
    const n = nums.length;
    const count = new Array(n + 1).fill(0);

    for (const num of nums) {
        count[num]++;
    }

    let duplicated = -1;
    let missing = -1;

    for (let i = 1; i <= n; i++) {
        if (count[i] === 2) duplicated = i;
        if (count[i] === 0) missing = i;
    }

    return [duplicated, missing];
};