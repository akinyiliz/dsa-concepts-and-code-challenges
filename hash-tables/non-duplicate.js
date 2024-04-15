/**
 * Write a function that returns the first non-duplicated character in a string.
For example, the string, "minimum" has two characters that only exist
once—the "n" and the "u", so your function should return the "n", since it
occurs first. The function should have an efficiency of O(N)
 */

/** Has a complexity of O(N)
 * 1. iterate over each character in the string
 * 2. create empty hasn table (object)
 * 3. if character does not exist in hash table, add the character as a key with a value of 1 indicating charcter has been found once so far.
 * 4. if character is already in the hash table, increment its value by 1.
 *
 * NB: if character "e" has a value 3, it means the "e" exists 3 times within the string.
 *
 * 5. we iterate over the string again
 * 6. return the first character that only exists once within the string.
 */

function findNonDuplicate(str) {
  let hashTable = {};

  for (let i = 0; i < str.length; i++) {
    if (!hashTable[str[i]]) {
      hashTable[str[i]] = 1;
    } else {
      hashTable[str[i]] += 1;
    }
  }

  for (let j = 0; j < str.length; j++) {
    if (hashTable[str[j]] === 1) {
      return str[j];
    }
  }
}

console.log(findNonDuplicate("minimum"));
