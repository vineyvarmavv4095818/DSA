import java.util.ArrayList;
import java.util.Arrays;

public class commonElements {
    public static ArrayList<Integer> print(int[] a, int[] b){
        int i=0,j=0;
        Arrays.sort(a);
        Arrays.sort(b);
        ArrayList<Integer> ans = new ArrayList<>();
        while(i<a.length && j<b.length){
            if(a[i]==b[j]){
                ans.add(a[i]);
                i++;
                j++;
            }
            else if(a[i]<b[j]) i++;
            else j++;
        }
        return ans;
        
        
    }
    public static void main(String[] args) {
        int[] a = {3,4,7,6};
        int[] b = {1,3,2,4};

        ArrayList<Integer> reuslt = print(a, b);
        System.out.println(reuslt);
    }
}
    

