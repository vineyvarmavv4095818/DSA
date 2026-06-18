// maximum count of positive integer and negative integer

public class Example {
    public static int neg(int[] arr) {
        int n = arr.length;
        int lo = 0, hi = n-1, negCount = 0;
        while(lo<=hi){
            int mid = (lo+hi)/2;
            if(arr[mid]>=0) hi = mid-1;
            else lo = mid+1;
            negCount = lo;
        }
        return negCount;
    }
    public static int pos(int[] arr) {
        int n = arr.length;
        int lo = 0, hi = n-1, posCount = 0;
        while(lo<=hi){
            int mid = (lo+hi)/2;
            if(arr[mid]<=0) lo = mid+1;
            else hi = mid-1;
            posCount = n-1-hi;
        }
        return posCount;
    }
    public static void main(String[] args) {
        int[] arr = {-5,-4,-3,-2,-1,1,2,3,5,6,8,9,10};
        int result = neg(arr);
        int result2 = pos(arr);

        System.out.println(result);
        System.out.println(result2);
    }
}
