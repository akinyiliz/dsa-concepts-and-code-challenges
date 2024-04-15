/**
 *  Write a function that accepts an array of strings and returns the first
duplicate value it finds. For example, if the array is ["a", "b", "c", "d", "c", "e",
"f"], the function should return "c", since it’s duplicated within the array.
(You can assume that there’s one pair of duplicates within the array.)
Make sure the function has an efficiency of O(N). 
*/

/** FIRST WAY - has a complexity of O(N²)
 *
 * 1. loop through the array 2 times(nested loops) - outer loop picks an element, inner loop compares this element with the rest of the array.
 * 2. if a match is found return it.
 */

// function findDuplicate(arr) {
//   for (let i = 0; i < arr.length; i++) {
//     for (let j = i + 1; j < arr.length; j++) {
//       if (arr[i] == arr[j]) {
//         return arr[i];
//       }
//     }
//   }
// }

/** SECOND WAY - has a complexity of O(N)
 *
 * 1. create a loop to check each string in the array.
 * 2. If the string is in the hash table, that means it’s been added before, which means it’s a duplicate! hence it is returned.
 * 3. If the string isn’t yet in the hash table(object), the string gets added to it.
 */
function findDuplicate(arr) {
  const hashTable = {};

  for (let i = 0; i < arr.length; i++) {
    if (hashTable[arr[i]]) {
      return arr[i];
    }

    hashTable[arr[i]] = true;
  }
}
console.log(findDuplicate(["a", "b", "a", "c", "d", "c", "e", "f"]));
