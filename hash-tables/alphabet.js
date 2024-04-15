/**
 * Write a function that accepts a string that contains all the letters of the
alphabet except one and returns the missing letter. For example, the string,
"the quick brown box jumps over a lazy dog" contains all the letters of the alphabet
except the letter, "f". The function should have a time complexity of O(N).
 */

/** Has a complexity of O(N)
 *
 * 1. create a hash table of out of all the characters in the string
 * 2. iterate over each character of the alphabet
 * 3. check if the character is contained within the hash table created above
 * 4. If it isn’t, it means the character is missing from the string, so we return it
 */

function findMissingLetter(str) {
  const hashTable = {};

  for (const key of str) {
    hashTable[key] = true;
  }

  let alphabet = "abcdefghijklmnopqrstuvwxyz";

  for (let i = 0; i < alphabet.length; i++) {
    if (!hashTable[alphabet[i]]) {
      return alphabet[i];
    }
  }

  return "no missing letter";
}

console.log(findMissingLetter("the quick brown fox jumps over a lazy dog"));
