public class SearchInMountainArr {
    public static void main(String[] args) {
        
    int[] arr = {1,2,3,4,5,8,6,5,4,1,0};
    int n = arr.length,lo = 1, hi = n-1;
        while(lo<=hi){
            int mid = (lo+hi)/2;
            if(arr[mid]>arr[mid+1] && arr[mid]>arr[mid-1]){
                System.out.println("target found at index "+mid);
                break;
            }

            else if(arr[mid]>arr[mid+1] && arr[mid]<arr[mid-1]) hi = mid-1;
            else lo = mid+1;

}
}
}
