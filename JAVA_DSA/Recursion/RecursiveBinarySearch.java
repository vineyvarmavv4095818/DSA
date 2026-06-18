public class RecursiveBinarySearch {
    public static int BinarySearch(int[] arr, int lo, int hi, int target) {
        if(lo > hi){
            return -1;
        }

        int mid = (lo+hi)/2;

        if(arr[mid]==target){
            return mid;
        }
        if(arr[mid] > target){
            return BinarySearch(arr, lo, mid-1, target);
        }
        
        return BinarySearch(arr, mid+1, hi, target);
    }

    public static void main(String[] args) {
        int[] arr= {2,3,4,5,6,7,8,9};
        int n = arr.length;

        int result = BinarySearch(arr, 0, n-1, 7);

        if(result != -1){
            System.out.println("target element found at index: "+ result);
        }
        else{
            System.out.println("Target not found...");
        }
    }
}
