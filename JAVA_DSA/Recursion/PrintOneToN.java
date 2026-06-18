import java.util.Scanner;
public class PrintOneToN {
    // public static void main(String[] args) {
    //     Scanner sc = new Scanner(System.in);
    //     int n = sc.nextInt();
    //     print(1,n);
    // }
    // public static void print(int x,int n) {
    //     if(x>n) return;
    //     System.out.println(x);
    //     print(x+1, n);
    // }
    // static int n;
    // public static void main(String[] args) {
    //     Scanner sc = new Scanner(System.in);
    //     n = sc.nextInt();
    //     print(1);
    // }
    // public static void print(int x) {
    //     if(x>n) return;
    //     System.out.println(x+" ");
    //     print(x+1);
    // }

    static int n;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        print(n);
    }
    public static void print(int n) {
        if(n==1){
            System.out.print(n+" ");
            return;
        }
        System.out.print(n+" ");
        print(n-1);
        System.out.print(n+" ");   //if(n!=1)
        
    }
}
