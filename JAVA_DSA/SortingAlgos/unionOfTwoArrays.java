import java.util.ArrayList;
import java.util.Arrays;


public class unionOfTwoArrays {
    public static ArrayList<Integer> union(int[] a,int[] b){
        int i = 0, j = 0;

        Arrays.sort(a);
        Arrays.sort(b);

        ArrayList<Integer> ans = new ArrayList<>();

        while(i<a.length && j<b.length){
            if(a[i]==b[j]){
                if(ans.size()==0 || ans.get(ans.size()-1)!=a[i])
                    ans.add(a[i]);
                    i++;
                    j++;
                    
                }
            else if(a[i]<b[j]){
                    if(ans.size()==0 || ans.get(ans.size()-1)!=a[i])
                        ans.add(a[i]);
                        i++;
                    
                }
            else{
                if(ans.size()==0 || ans.get(ans.size()-1)!=b[j])
                    ans.add(b[j]);
                    j++;
                    
                }
        while(i<a.length){
            if(ans.size()==0 || ans.get(ans.size()-1)!=a[i])
                ans.add(a[i]);
                i++;
                
            }

        while(j<b.length){
            if(ans.size()==0 || ans.get(ans.size()-1)!=b[j])
                    ans.add(b[j]);
                    j++;
                
            }
    
        }
        return ans;
}
public static void main(String[] args) {
    int[] a = {3,4,5,6};
    int[] b = {1,2,3,4};

    System.out.println(union(a,b));
}
}

        
