public class Transpose {
    // public static void print(int[][] arr) {
    //     for(int[] a: arr){
    //         for(int ele: a){
    //             System.out.print(ele+" ");
    //         }
    //         System.out.println();
    //     }
    //     System.out.println();
    // }
    // public static void main(String[] args) {
    //     int[][] arr = {{2,8,3,4},{7,2,1,6},{3,2,1,4},{3,1,8,2}};
    //     print(arr);

    //      //Transpose(changing in main matrix)
    //     for(int i=1; i<arr.length; i++){
    //         for(int j=0; j<i; j++){
    //             int temp = arr[i][j];
    //             arr[i][j] = arr[j][i];
    //             arr[j][i] = temp;
    //             }
    //     }
    //     print(arr);
    // }
    public static int[][] transpose(int[][] arr) {
        int row = arr.length, col = arr[0].length;
        int[][] b = new int[col][row];
        for(int i=0; i<b.length; i++){
            for(int j=0; j<b[0].length; j++){
                b[i][j]=arr[j][i];
            }
        }
        return b;
    }
    public static void main(String[] args) {
        int[][] arr = {{2,8,3,4},{7,2,1,3},{3,2,1,4},{3,1,2,6}};
        for(int[] a: arr){
            for(int ele: a){
                System.out.print(ele+" ");
            }
            System.out.println();
        }
        System.out.println();
        int[][] result = transpose(arr);

        for(int i=0; i<result.length; i++){
            for(int j=0; j<result[0].length; j++){
                System.out.print(result[i][j]+" ");
            }
            System.out.println();
        }
    }
}
