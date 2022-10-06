const mergeSort = arr => {
    let arrayLength = arr.length

    
    if(arrayLength < 2) {
        return;
    }
    //divide the array into left and right halves
    const mid = Math.floor(arr.length/2)
    const left = arr.slice(0,mid)
    const right = arr.slice(mid,arr.length)

    
    mergeSort(left)
    mergeSort(right)
    
    let n=0; //index of array being sorted
    let iLeft = 0; //index of left array
    let iRight = 0; //index or right array
    
    //merge the sorted left and right array
    while (n<arrayLength) {
        if (left[iLeft] <= right[iRight]){
            arr[n] = left[iLeft]
            iLeft+=1
            n+=1
        } else {
            arr[n] = right[iRight]
            iRight+=1
            n+=1
        }
        
        //check left or right has added all elements and add remaining elements of the other array
        if (iLeft === left.length) {
            while (iRight < right.length) {
                arr[n]=right[iRight]
                iRight+=1
                n+=1
            }
            break
        } else if (iRight === right.length) {
            while (iLeft < left.length) {
                arr[n]=left[iLeft]
                iLeft+=1
                n+=1
            }
            break
        }
    }
}



test = [10,9,8,7,6,5,4,3,2,3,1,12]
mergeSort(test)
console.log(test)