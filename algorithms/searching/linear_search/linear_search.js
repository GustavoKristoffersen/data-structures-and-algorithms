// On an unordered array
const linearSearch = function(arr, value) {
    for(let i=0; i < arr.length; i++) {
        if(arr[i] == value){
            return i;
        }
    }
    return -1;
}

// On an ordered array
const linearSearchOnOrderedArr = function(arr, value) {
    for (let i=0; i < arr.length; i++) {
        if (arr[i] == value) {
            return i;
        }
        else if (arr[i] > value) {
            break;
        }
    }
    return -1;
}


// Export functions for use in other files
module.exports = {linearSearch, linearSearchOnOrderedArr}
