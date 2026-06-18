public class Arrangingcoins {
    public static int sqrt(int n) {   //kisi number n ka sqrt nikalna. 
        int lo = 1,hi = n;
        while(lo<=hi){
            int mid = (lo+hi)/2;
            if(mid*mid==n) return mid;
            else if(mid*mid>n) hi = mid-1;
            else lo = mid+1;
        }
        return hi;
    }
    public static int Arrangingcoin(int m) {   // yaha pr n = (8*m+1) hai, OR m = number of coins.
        return (sqrt(8*m+1)-1)/2;
    }
    public static void main(String[] args) {
        int result = Arrangingcoin(20);
        System.out.println(result);
    }
}
