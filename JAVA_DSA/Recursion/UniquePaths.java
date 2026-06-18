public class UniquePaths {
    public static int uniquePaths(int m, int n) {
        if(m==1 || n==1) return 1;
        return uniquePaths(m-1, n) + uniquePaths(m, n-1);
    }
    public static void main(String[] args) {
        int m = 4;
        int n = 3;
        System.out.println(uniquePaths(m, n));
    }
}
