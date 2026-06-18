public class Power {
    // public static void main(String[] args) {
    //     System.out.println(pow(3,4));
    // }
    // public static int pow(int a, int b){
    //     if(b==0) return 1;
    //     return a*pow(a,b-1);
    // }
    public static void main(String[] args) {
        System.out.println(pow(2,4));
    }
    public static int pow(int a, int b){
        if(b==0) return 1;
        int call = pow(a, b/2);
        if(b%2==0) return call*call;
        return a*call*call;
    }
}
