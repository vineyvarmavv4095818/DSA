import java.util.Scanner;
public class tutorial {
    public static void main(String[] args) {
        // char[] s = {'v','i','n','a','y'};
        // for(char ele: s){
        //     System.out.print(ele+" ");
        // }
        // Scanner sc = new Scanner(System.in);
        // String s = sc.nextLine();
        // System.out.println(s);
        // System.out.println(s.charAt(4));
        // System.out.println(s.charAt(5));
        // System.out.println(s.charAt(6));
        // String s = "eoiuiowuerioieoruioapiuou";
        // int count = 0;
        // for(int i=0; i<s.length(); i++){
        //     char ch = s.charAt(i);
        //     if(ch=='i' || ch=='e' || ch=='o' || ch=='a' ||ch=='u')
        //         count++;
        // }
        // System.out.println(count);

        
        // System.out.println(s1.equals(s2));
        // String s1 = "vinay";
        // String s2 = "vinay";
        // System.out.println(s1==s2);

        String s1 = new String("vinay");
        String s2 = new String("vinay");
        
        boolean isEql = true;
        if(s1.length()!=s2.length()) isEql = false;
        for(int i=0; i<s1.length(); i++){
            if(s1.charAt(i)!=s2.charAt(i)) isEql = false;
        }
        System.out.println(isEql);
    }
}
