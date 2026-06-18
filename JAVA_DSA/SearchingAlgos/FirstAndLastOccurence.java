public class FirstAndLastOccurence {
    public static int first(int[] arr, int tar) {
        //First occurence
        int lo = 0, hi = arr.length-1,idx = -1;
        while(lo<=hi){
            int mid = (lo+hi)/2;
            if(arr[mid]<tar) lo = mid+1;
            else if(arr[mid]>tar) hi = mid-1;
            else{
                idx = mid;
                hi = mid-1;
            }
        }
        return idx;
        
    }
    
    public static int last(int[] arr, int tar) {
        // Second occurence
        int lo = 0, hi = arr.length-1,idx2 = -1;
        while(lo<=hi){
            int mid = (lo+hi)/2;
            if(arr[mid]<tar) lo = mid+1;
            else if(arr[mid]>tar) hi = mid-1;
            else{
                idx2 = mid;
                lo = mid+1;
            }
        }
        return idx2;
        
    }
    public static void main(String[] args) {
        int[] arr = {1,2,4,5,5,5,6,7,8};
        int result1 = first(arr, 5);
        System.out.println(result1);

        int result2 = last(arr, 5);
        System.out.println(result2);

    }
    
}
