// # binary search function

// #define left and right pointers


// # loop until the left pointer is greater than the right pointer

// # Find the middle index of the current subarray

// # If the target value is equal to the middle element, return the index

// # If the target value is less than the middle element, move the right pointer to the left of the middle index

// # If the target value is greater than the middle element, move the left pointer to the right of the middle index

// # If the target value is not found, return -1

// # Test the function with some examples

const arr = [ 2, 5,6,7,8,9]
function findAr( t, s , e) {
    if (s > e){
        return 'not found';
    }
    const mid = Math.floor( (s + e)/2);
    if (arr[mid] === t){
        return `t found at ${mid}`;
    }
    if (arr[mid] > t){
        return findAr(t,s, mid - 1);
    }

        
    if (t > arr[mid]){
       return findAr(t, mid +1, e) 
    }

}
console.log(findAr(5, 0, arr.length - 1));

