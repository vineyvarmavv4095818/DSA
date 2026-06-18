import java.util.ArrayList;

public class tutorial {
    public static void main(String[] args) {
        ArrayList<Integer> a = new ArrayList<>();
        a.add(1); a.add(2); a.add(4);
        ArrayList<Integer> b = new ArrayList<>();
        b.add(5); b.add(2); b.add(6);
        ArrayList<Integer> c = new ArrayList<>();
        c.add(0); c.add(9); c.add(7);

        ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
        arr.add(a); arr.add(b); arr.add(c);

        System.out.println(arr);

        // for(int i=0; i<arr.size(); i++){
        //     for(int j=0; j<arr.get(i).size(); j++){
        //         System.out.print(arr.get(i).get(j)+" ");
        //     }
        //     System.out.println();
        // }

        arr.get(1).set(0,4);
        System.out.println(arr);

        System.out.println(arr.get(0).get(2));

        arr.add(new ArrayList<>());
        arr.get(arr.size()-1).add(1); arr.get(arr.size()-1).add(2);


        for(ArrayList<Integer> List: arr){
            for(int ele: List){
                System.out.print(ele+" ");
            }
            System.out.println();
        }




    }
}
