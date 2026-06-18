public class MaxElement {
    public static void main(String[] args) {
        
    
    int[] arr = {-4,2,3,4,5,6,99,89};
    for(int i=0; i<arr.length; i++){
        System.out.print(arr[i]+" ");
    }
    System.out.println();
    int max = arr[0];

    for(int i=0; i<arr.length; i++)
    if(arr[i]>max){
        max = arr[i];
    }
    System.out.println("max element of the array is: "+max);

}
}
