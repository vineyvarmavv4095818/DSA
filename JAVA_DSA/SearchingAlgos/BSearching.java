public class BSearching {
    public static void main(String[] args) {
        int[] arr = {7,3,8,2,4,9,11,0,35,62,34};
        int n = arr.length;
        int tar = 1;
        boolean found = false;
        int lo = 0, hi = n-1;
        while(lo<=hi){
            int mid = (lo+hi)/2;
            if(arr[mid]==tar) {
                System.out.println("target found at index "+mid);
                found = true;
                break;
            }
            else if(arr[mid]>tar) hi = mid-1;
            else lo = mid+1;
            
        }
        if(found==false){
            System.out.println("target not found.");
        }
    }
    
}
