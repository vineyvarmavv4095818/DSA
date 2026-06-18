import java.util.ArrayList;
import java.util.Collections;

public class AddOneInArray {
    public static void main(String[] args) {
        
        ArrayList<Integer> arr = new ArrayList<>();
        
        arr.add(1);
        arr.add(2);
        arr.add(3);
        System.out.println(arr);

        int carry = 1;
        for(int i = arr.size()-1; i>=0; i--){
        if(arr.get(i)+carry<=9){
            arr.set(i,arr.get(i)+carry);
            carry = 0;
            break; //carry khtm hone ke bad extra iterations na ho isliye yaha break lgaya (uses for efficiency)
        }
        else{
            arr.set(i,0);
            carry = 1;
        }
    }
    if(carry==1){
        arr.add(0,1);
    }
    System.out.println(arr);
    
    
}
    
}
