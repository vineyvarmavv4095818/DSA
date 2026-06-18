import java.util.Scanner;
public class OddEven {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // System.out.println("Enter length:");
        // int length = sc.nextInt();
        // System.out.println("Enter width:");
        // int width = sc.nextInt();

        // String re = (num%5==0)?"yes":"no";
        // System.out.println(re);

        // int abs;
        // if(num < 0) abs = -num;
        // else abs = num;
        // System.out.println("Absolute Value: "+abs);

        // double num = sc.nextDouble();
        // if(num == (int)num) System.out.println("It is an integer");
        // else System.out.println("Not an integer");

        // if(costPrice > sellPrice) System.out.println("Loss of Rs"+(costPrice-sellPrice));
        // else if(costPrice < sellPrice) System.out.println("Profit of Rs"+(sellPrice-costPrice));
        // else System.out.println("No loss No profit.");

        // int area = length*width;
        // System.out.println("area is: "+area);
        // int perimeter = 2*(length+width);
        // System.out.println("perimeter is: "+perimeter);

        // if(area > perimeter)  System.out.println("perimeter is not greater.");
        // else System.out.println("area is not greater than perimeter");

        // System.out.println("Enter a number:");
        // int num = sc.nextInt();

        // if(num%5==0 && num%3==0) System.out.println("sahu");
        // else if(num%3==0) System.out.println("Banu");
        // else if(num%5==0) System.out.println("Riya");
        // else System.out.println("vinay");

        System.out.println("Enter x:");
        int x = sc.nextInt();
        System.out.println("Enter y:");
        int y = sc.nextInt();

        if(x==0 && y==0) System.out.println("point lies on origin");
        else if(x==0 && y!=0) System.out.println("point lies on y-axis.");
        else if(y==0 && x!=0) System.out.println("point lies on x-axis.");
        else if(x>0 && y>0) System.out.println("point lies in 1st Quadrant.");
        else if(x<0 && y>0) System.out.println("lies in 2nd Quadrant.");
        else if (x<0 && y<0) System.out.println("lies in 3rd Quadrant.");
        else System.out.println("lies in 4th Quadrant.");
    }
    
}
