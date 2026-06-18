import java.util.Scanner;
public class QuadrantCheck {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enetr x coordinate:");
        int x = sc.nextInt();
        System.out.println("Enter y coordinate:");
        int y = sc.nextInt();

        if(x==0 && y==0)
            System.out.println("the point lies on the origin.");
        else if (x==0)
            System.out.println("the point lies on y axis.");
        else if(y==0)
            System.out.println("the point lies on x axis.");
        else if(x>0 && y>0)
            System.out.println("the point lies in 1st qua.");
        else if(x<0 && y>0)
            System.out.println("the point lies in 2nd qua.");
        else if(x<0 && y<0)
            System.out.println("the point lies in 3rd qua.");
        else System.out.println("the point lies in 4th qua.");
                    
        


        }
    
}
