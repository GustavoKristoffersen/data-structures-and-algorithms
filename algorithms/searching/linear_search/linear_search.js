function linearSearch(arr, value) {
    for(let i=0; i < arr.length; i++) {
        if(arr[i] == value){
            return i;
        }
    }
    return -1;
}


function linearSearch(arr, value) {
    for(let i=0; i < arr.length; i++) {
        if(arr[i] == value) {
            return i;
        }
        else if(arr[i] > value) {
            break;
        }
    }
    return -1;
}