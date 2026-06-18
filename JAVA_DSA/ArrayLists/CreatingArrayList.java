import java.util.ArrayList;
import java.util.Collections;

public class CreatingArrayList {
    public static void main(String[] args) {

        ArrayList<Integer> arr = new ArrayList<>();
        arr.add(10);
        arr.add(20);
        arr.add(30);
        arr.add(40);
        arr.add(50);

        System.out.println(arr.get(1));
        arr.set(1,200);
        System.out.println(arr);

        // int n = arr.size();
        // for(int i = 0; i<n; i++){
        //     System.out.print(arr.get(i)+" ");

        // for(int ele: arr) System.out.print(ele+" ");

        arr.add(78);
        arr.add(1, 18);
        System.out.println(arr);
        arr.remove(5);
        System.out.println(arr);
        // Collections.reverse(arr);

        int i = 0, j = arr.size()-1;
        while(i<j){
            int temp = arr.get(i);
            arr.set(i, arr.get(j));
            arr.set(j, temp);
            i++;
            j--;
            
        }

        System.out.println(arr);

        
    }
    
}
