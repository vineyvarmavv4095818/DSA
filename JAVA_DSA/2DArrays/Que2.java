public class Que2 {
    public static void main(String[] args) {
        int[][] arr = {{2,8,3,4,7},{7,2,1,6,3},{3,2,4,1,4},{3,1,8,2,6}};
        int[][] rev = new int[arr.length][arr[0].length];
        for(int i=0; i<arr.length; i++){
            for(int j=arr[0].length-1; j>=0; j--){
                System.out.print(arr[i][j]+" ");
                }
                System.out.println();
            }
            int[][] b = new int[arr.length][arr[0].length];
            for(int i=0; i<b.length; i++){
            for(int j=0; j<b[0].length; j++){
                b[i][j]=arr[i][j];
            }
        }
            System.out.println();
        for(int i=0; i<b.length; i++){
            int stCol=0, endCol=b[0].length-1;
            while(stCol<=endCol){
                int temp = b[i][stCol];
                b[i][stCol] = b[i][endCol];
                b[i][endCol] = temp;
                stCol++;
                endCol--;
            }
        }
        for(int[] a: b){
            for(int ele: a){
                System.out.print(ele+" ");
            }
            System.out.println();
        }
        
    }
        
}

