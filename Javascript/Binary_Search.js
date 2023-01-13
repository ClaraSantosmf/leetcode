// 704. Binary Search
// https://leetcode.com/problems/running-sum-of-1d-array/description/
// Você pode rodar no termina com -> node Javascript/Binary_Search.js
// Um classico da busca binária, adoro. Esse é easy também

var search = function (nums, target) {
    let baixo = 0
    let alto = nums.length-1
    while (baixo <= alto){
        let meio = Math.floor((alto + baixo) / 2);
        let chute = nums[meio]
        if (chute == target) {
          return meio;
        } else if (chute > target) {
            alto = meio - 1
        } else {
            baixo = meio + 1
        }
    }
    return -1;
};

let nums = [-1, 0, 3, 5, 9, 12];
let target = 3;

console.log(search(nums,target));
