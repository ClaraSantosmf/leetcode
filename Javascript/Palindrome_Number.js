// 9. Palindrome Number é easy. Não me julguem, eu estava com umas tasks braba na hora. Prometo melhorar
// https://leetcode.com/problems/palindrome-number/description/
// Você pode rodar no termina com -> node Javascript/Palindrome_Number.js

var isPalindrome = function (x) {
  if (x >= 0) {
    let numeroPositivoStr = x.toString();
    if (numeroPositivoStr.split("").reverse().join("") == numeroPositivoStr) {
      return true;
    }
  }
  return false;
};
