// find kth missing positive integer.

public class Example3 {
    public static int find(int[] arr, int k) {
        int lo = 0, hi = arr.length-1;
        while(lo<=hi){
            int mid = (lo+hi)/2;
            int correctNo = mid+1;
            int missingCount = arr[mid]-correctNo;
            if(missingCount>=k) hi = mid-1;
            else lo = mid+1;
        }
        return lo+k;
    }
    public static void main(String[] args) {
        int[] arr = {1,2,4,6,8,10};
        int result = find(arr, 1);
        System.out.println(result);
    }
}
