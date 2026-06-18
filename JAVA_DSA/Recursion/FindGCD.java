public class FindGCD {
    public static int gcd(int a, int b) {
        if(a==0) return b;
        return gcd(b%a, a);
    }
    public static void main(String[] args) {
        int result = gcd(24, 0);
        System.out.println(result);
    }
}
