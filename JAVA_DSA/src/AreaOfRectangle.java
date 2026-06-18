import java.util.Scanner;


public class AreaOfRectangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("enter the length of rectangle:");
        int l = sc.nextInt();
        System.out.print("enter width of rectangle:");
        int w = sc.nextInt();
        
        double area = l*w;
        double perimeter = 2*(l+w);

        if(area > perimeter) System.out.println("the area "+area+" is greater than its perimeter " +perimeter);
        else System.out.println("the area "+area+" is not greater than its perimeter " +perimeter);


    }
} 
