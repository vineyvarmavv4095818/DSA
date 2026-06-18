public class descencingOrderSearch {
    public static void main(String[] args) {
        int[] arr = {87,77,68,64,24,20,11};
        int n = arr.length,lo = n-1, hi = 0, tar = 1;
        boolean found = false;
        while(hi<=lo){
            int mid = (lo+hi)/2;
            if(arr[mid]==tar) {
                System.out.println("target found at index "+mid);
            found = true;
            break;
            }
            else if(arr[mid]<tar) lo = mid-1;
            else hi = mid+1;

    }
    if(found==false){
        System.out.println("target not found.");
    }

}
}
