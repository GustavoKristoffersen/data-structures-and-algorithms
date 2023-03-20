function merge(leftArr, rightArr){
    let result = [];
    let leftIndex = 0;
    let rightIndex = 0;
  
    while(leftIndex < leftArr.length && 
          rightIndex < rightArr.length) {
       if(leftArr[leftIndex] < rightArr[rightIndex]) {
         result.push(leftArr[leftIndex]);
         leftIndex++;
       }
       else {
         result.push(rightArr[rightIndex]);
         rightIndex++
      }
    }
  
    return result.concat(leftArr.slice(leftIndex)).concat(rightArr.slice(rightIndex));
  }


function mergeSort (array) {
  if (array.length === 1) {
    return array;
  }

  let length = array.length;
  let middleIndex = Math.floor(length / 2);
  let leftArr = array.slice(0, middleIndex); 
  let rightArr = array.slice(middleIndex);
  
  return merge(
    mergeSort(leftArr),
    mergeSort(rightArr)
  )
}
