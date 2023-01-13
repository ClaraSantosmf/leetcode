// 1480. Running Sum of 1d Array
// https://leetcode.com/problems/running-sum-of-1d-array/description/
// Você pode rodar no termina com -> node Javascript/Running_Sum_of_1d_Array.js

var runningSum = function (nums) {
  lista_de_retorno = [];
  let soma = 0
  for (let i = 0; i < nums.length; i++) {
    soma += nums[i]
    lista_de_retorno.push(soma)
  }
  return lista_de_retorno;
};


nums = [3,1,2,10,1];
console.log(runningSum(nums));