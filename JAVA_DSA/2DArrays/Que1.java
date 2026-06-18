// find the maximum element out of all the maximum elements of each row.

public class Que1 {
    public static void main(String[] args) {
        int[][] arr = {{2,8,3,4,7},{7,2,1,6,3},{3,2,4,1,4},{3,1,8,2,6}};
        for(int[] a: arr){
            for(int ele: a){
                System.out.print(ele+" ");
            }
            System.out.println();
        }
        int minOfMax = Integer.MAX_VALUE;
        int row = -1;
        for(int i=0; i<arr.length; i++){
            int max = Integer.MIN_VALUE;
            for(int j=0; j<arr[0].length; j++){
                if(arr[i][j]>max) max =arr[i][j];
            }
            System.out.println("max element of row "+i+": "+max);
            if(max<minOfMax)
                minOfMax = max;
                row = i;
        }
        System.err.println("minimum between max elements form row "+row+": "+minOfMax);
    }
}
