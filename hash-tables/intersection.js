/**
 * Write a function that returns the intersection of two arrays. The intersec-
tion is a third array that contains all values contained within the first two
arrays. For example, the intersection of [1, 2, 3, 4, 5] and [0, 2, 4, 6, 8] is [2, 4].
Your function should have a complexity of O(N). (If your programming
language has a built-in way of doing this, don’t use it. The idea is to build
the algorithm yourself.)
 */

/** FIRST WAY - has a complexity on O(N²)
 *
 * 1. loop through 1st array
 * 2. loop through 2nd array
 * 3. compare elements in 1st array with those in 2nd array
 * 4. if they are the same push the element to a new array(3rd)
 * 5. return the 3rd array
 */

// function getIntersection(array1, array2) {
//   let array3 = [];

//   for (let i = 0; i < array1.length; i++) {
//     for (let j = 0; j < array2.length; j++) {
//       if (array1[i] === array2[j]) {
//         array3.push(array1[i]);
//       }
//     }
//   }

//   return array3;
// }

/** SECOND WAY - has a complexity of O(N)
 *
 * 1. turn 1st array to a hash table - loop through it and adding the elements as keys to a new object with their values being "true"
 * 2. loop through 2nd array
 * 3. check each value in 2nd array against the 1st array which you turned to object(hash table)
 * 4. push the elements to a new array(3rd)
 * 5. return the 3rd array
 */

function getIntersection(array1, array2) {
  let array3 = [];
  let hashTable = {};

  for (const key of array1) {
    hashTable[key] = true;
  }

  for (const key of array2) {
    if (hashTable[key]) {
      array3.push(key);
    }
  }

  return array3;
}

console.log(getIntersection([1, 2, 3, 4, 5], [0, 2, 4, 6, 8]));

console.log(
  getIntersection([10, 8, 24, 99, 3, 4, 7, 2], [24, 666, 10, 3, 99, 6, 72, 7])
);
