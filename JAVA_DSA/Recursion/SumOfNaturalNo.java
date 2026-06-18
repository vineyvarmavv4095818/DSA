public class SumOfNaturalNo {
    public static int findSum(int n) {
        if(n==1) return 1;
        return n + findSum(n-1);
    }
    public static void main(String[] args) {
        int result = findSum(3);
        System.out.println(result);
    }
}