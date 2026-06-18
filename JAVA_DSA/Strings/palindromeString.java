import java.util.Scanner;
public class palindromeString {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter a string:");
        String s = sc.nextLine();
        int n = s.length(), i = 0, j=n-1;
        boolean isPlaindrome = true;
        while(i<=j){
            if(s.charAt(i)!=s.charAt(j)) isPlaindrome = false;
        i++;
        j--; }
        if(isPlaindrome) System.out.println("this string is a palindrome string.");
        else System.out.println("this string is not a palindrome string.");
    }
}
