public class pattern7 {
    public static void main(String[] args) {
        for(int i=1; i<=5; i++){
            for(int j=1; j<=5; j++){
                if(i%2==0) System.out.print((char)(i+64) + " ");
                else System.out.print((char)(i+96) + " ");
            }
            System.out.println();
        }
    
    }
    
}
