/**
 * @param {number[]} arr
 * @return {number}
 */
var peakIndexInMountainArray = function(arr) {
    let bot = 0
    let top = arr.length - 1
    let mid

    while (bot < top){
        mid = bot + Math.floor((top - bot)/2)
        if (arr[mid] >= arr[mid+1]){
            top = mid
        } else{
            bot = mid + 1
        }
    }

    return bot


};
