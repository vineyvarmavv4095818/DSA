public class floorRoot {
    public static int mysqrt(int n) {
        
        // int root = 0;
        // for(int i=1; i<n; i++){
        //     if(i*i>n) break;
        //     root = i;
        // }
        // System.out.println(root);
        int lo = 1,hi = n;
        while(lo<=hi){
            int mid = (lo+hi)/2;
            if(mid*mid==n) return mid;
            else if(mid*mid>n) hi = mid-1;
            else lo = mid+1;
        }
        return hi;
    }
    public static void main(String[] args) {
        
        int result = mysqrt(25);
        System.out.println(result);
        
    }
}
