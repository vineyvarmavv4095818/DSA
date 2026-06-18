import java.util.Scanner;
public class changeTheString {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // System.out.println("enter a string:");
        // String s = sc.nextLine();
        // char ch = s.charAt(0);
        // if(Character.isLowerCase(ch)) s = s.toLowerCase();
        // else s = s.toUpperCase();
        // System.out.println(s);


        String s = "gopi";
        for(int j =0; j<s.length(); j++){
        for(int i = j+1; i<=s.length(); i++){  //j+1 isliye kiya kyuki i ko hr bar 1 se start nhi kr skte i hmesha j se ek index aage jayega
            System.out.print(s.substring(j,i)+" ");
            }
            System.out.println();
        }


        // int n = sc.nextInt();
        // String s = "" + n;
        // System.out.println(s.length());


        // String s = "vinay";
        // s = s.toUpperCase();
        // System.out.println(s);


        // String str = "123456";
        // int n = Integer.parseInt(str);
        // System.out.println(n+1);


        //String to CharArray...

        // String s = "vinay";
        // char[] arr = s.toCharArray();
        // for(char ch:arr){
        //     System.out.print(ch+" ");
        // }


        // String s = "jaishankar";
        // System.out.println(s.substring(7));
        // System.out.println(s.substring(1,3));



    }
}
