import java.util.Arrays;


public class ShallowCopyDeepCopy {
    public static void main(String[] args) {
        int[] arr = {10,20,30,40};
        
        //    shallow copy
        // int[] x = arr;
        // x[0] = 100;
        // x[1] = 200;
        // System.out.println(x[0]);
        // System.out.println(arr[1]);

        //    deep copy
        int[] y = Arrays.copyOf(arr,arr.length);
        y[0] = 100;
        System.out.println(y[0]);
        System.out.println(arr[0]);
    
    }
    
}
