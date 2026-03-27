/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    const counts = new Array(101).fill(0);
    const smaller = new Array(101).fill(0);

    for (const num of nums) {
        counts[num] += 1;
    }

    smaller[0] = 0;
    for (let i = 1; i < 101; i++) {
        smaller[i] = smaller[i-1] + counts[i-1];
    }

    const result = [];
    for (const num of nums) {
        result.push(smaller[num]);
    }

    return result;

};