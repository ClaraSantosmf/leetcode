// 9. Palindrome Number Isso é easy. Não me julguem, eu estava com umas tasks braba na hora. Prometo melhorar
// https://leetcode.com/problems/palindrome-number/description/
// Você pode rodar no termina com -> node Javascript/Palindrome_Number.js

var isPalindrome = function (x) {
  if (x >= 0) {
    let palavra = x.toString();
    if (palavra.split("").reverse().join("") == palavra) {
      return true;
    } else {
      return false;
    }
  } else {
    return false;
  }
};
