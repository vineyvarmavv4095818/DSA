// search an element in sorted and rotated array

public class Example2 {
    public static int find(int[] arr, int tar) {
        int n = arr.length, lo = 0, hi = n-1;
        while(lo<=hi){
            int mid = (lo+hi)/2;
            if(arr[mid]==tar) return mid;
            else if(arr[lo]<=arr[mid]){
                if(arr[lo]<=tar && arr[mid]>tar) hi = mid-1;
                else lo = mid+1;
            }
            else{
                if(arr[mid]<tar && arr[hi]>=tar) lo = mid+1;
                else hi = mid-1;
            }
        }
        return -1;
    }
    public static void main(String[] args) {
        int[] arr = {5,7,8,9,10,11,1,2,3,4};
        int result = find(arr, 4);

        System.out.println(result);
    }
}
