import java.util.ArrayList;
import java.util.List;

public class PascalTriangle {
    public List<List<Integer>> generates(int n) {
        List<List<Integer>> ans = new ArrayList<>();
        for(int i=0; i<n; i++){
            List<Integer> list = new ArrayList<>();
            for(int j=0; j<=i; j++){
                list.add(1);
            }
            ans.add(list);
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<=i; j++){
                if(j==0 || j==i) ans.get(i).set(j,1);
                else{
                    int val = ans.get(i-1).get(j)+ans.get(i-1).get(i-1);
                    ans.get(i).set(j,val);
                }
            }
        }
        return ans;
    }
    public static void main(String[] args) {
        PascalTriangle obj = new PascalTriangle();
        List<List<Integer>> result = obj.generates(5);

        for(List<Integer> row: result){
            System.out.println(row);
        }
    }
}