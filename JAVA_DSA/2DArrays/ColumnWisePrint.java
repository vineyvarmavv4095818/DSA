public class ColumnWisePrint {
    public static void main(String[] args) {
        int[][] arr = {{8,3,4},{2,1,6},{2,4,1},{1,8,2}};
        
        for(int i=0; i<arr.length; i++){
            for(int j=0; j<arr[0].length; j++){
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }
        System.out.println();
        for(int j=0; j<arr[0].length; j++){
            for(int i=0; i<arr.length; i++){
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }
    }
}
