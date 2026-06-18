
public class GlobalVariable {
    static int x = 10;
    public static void main(String[] args) {
        fun();
        x = 9;
        System.out.println(x);
        int x = 4;
        System.out.println(x);
        x=6;
        fun();
    }
    public static void fun() {
        System.out.println(x);
        x = 20;
        System.out.println(x);
        x=2;
        System.out.println(x);
    }
}
