public class ReverseSB {
    public static void main(String[] args) {
        String s = "hello";
        StringBuilder sb = new StringBuilder(s);

        // int i=0, j=sb.length()-1;
        // while(i<=j){
        //     char temp = sb.charAt(i);
        //     char temp2 = sb.charAt(j);
            
        //     sb.setCharAt(i, temp2);
        //     sb.setCharAt(j, temp);
        //     i++;
        //     j--;
        // }

        // sb.reverse();
        sb.delete(0, 2);
        sb.insert(0,'h');
        sb.deleteCharAt(0);

        s = sb.toString();
        System.out.println(s);


    }
}
