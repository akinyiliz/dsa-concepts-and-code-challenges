/**
 * Write a function that uses a stack to reverse a string. (For example, "abcde"
would become "edcba".) You can work with our earlier implementation of
the Stack class.
 */

// Earlier implementation of Stack class
class Stack {
  constructor() {
    this.data = [];
  }

  // check if stack is empty
  isEmpty() {
    return this.data.length === 0;
  }

  // inserts element into the stack
  pushElement(element) {
    this.data.push(element);
  }

  // removes element from the stack
  popElement() {
    if (this.isEmpty()) {
      return "Stack is empty";
    }

    return this.data.pop();
  }

  // reads last element on the stack
  readElement() {
    if (this.isEmpty()) {
      return "Stack is empty";
    }

    return this.data[this.data.length - 1];
  }
}

/**
 * 1. Create an instance of the Stack class
 * 2. loop through the string you want to reverse
 * 3. in the loop, use pushElement() method to insert each character of the string into the stack.
 * 4. create an empty variable that will hold the reversed string
 * 5. add a condition to check if stck is empty, if it isn't, use popElement() method to remove each last character in the string and add it to the reversed string variable
 * 6. return the reversed string variable
 */

function reverseString(str) {
  const stack = new Stack();

  for (let i = 0; i < str.length; i++) {
    stack.pushElement(str[i]);
  }

  let reversedString = "";

  while (!stack.isEmpty()) {
    reversedString += stack.popElement();
  }

  return reversedString;
}

console.log(reverseString("abcde"));
