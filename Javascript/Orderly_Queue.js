// Isso é um HARD. 
// Isso serve para reorganizar um a uma! Então a gente vai puxando 
// https://leetcode.com/problems/orderly-queue/description/

var orderlyQueue = function (s, k) {
  let nova_palavra = s;

  if (k === 1) {
    let tamanho_da_string = s.length;
    for (let i = 0; i < tamanho_da_string; i++) {
      let letra = s[0];
      s = s.substring(1, tamanho_da_string) + letra;
      if (s < nova_palavra) nova_palavra = s;
    }

    return nova_palavra;
  }

  return [...s].sort().join("");
};