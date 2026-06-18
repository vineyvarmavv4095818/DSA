public class FindFloor {
    public static int findFloor(int[] arr, int tar) {
        
        int lo = 0, hi = arr.length-1, idx = -1;
        while(lo<=hi){
            int mid = (lo+hi)/2;
            if(arr[mid]>tar) hi = mid-1;
            else{
                idx = mid;
                lo = mid+1;
            }
            
        }
        return arr[idx];
    }
    public static void main(String[] args) {
        int [] arr = {1,2,4,10,10,12,17};
        
        int result = findFloor(arr, 5);
        System.out.println(result);

    }
}
