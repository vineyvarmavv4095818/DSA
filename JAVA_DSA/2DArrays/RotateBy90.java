public class RotateBy90 {
    public static void main(String[] args) {
        int[][] arr = {{2,8,3,4},{7,2,1,3},{3,2,1,4},{3,1,2,6}};
             //Transpose(changing in main matrix)
        for(int i=1; i<arr.length; i++){
            for(int j=0; j<i; j++){
                int temp = arr[i][j];
                arr[i][j] = arr[j][i];
                arr[j][i] = temp;
                }
        }
        // reverse each row
        for(int i=0; i<arr.length; i++){
            int stCol=0, endCol=arr[0].length-1;
            while(stCol<=endCol){
                int temp = arr[i][stCol];
                arr[i][stCol] = arr[i][endCol];
                arr[i][endCol] = temp;
                stCol++;
                endCol--;
            }
        }
        for(int[] a: arr){
            for(int ele: a){
                System.out.print(ele+" ");
            }
            System.out.println();
        }
    }
}

