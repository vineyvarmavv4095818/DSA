public class Que2 {
    public static void sort0s1s2s(int[] arr) {
        int numberOfZeros = 0;
        int numberOfOnes = 0;
        int numberOf2s= 0;

        // count number of zeros,ones and 2s.

        for(int ele: arr){
            if(ele==0) numberOfZeros++;
            else if(ele==1) numberOfOnes++;
            else if(ele==2) numberOf2s++;
        }
        // fill zeros
        for(int i=0; i<numberOfZeros; i++){
            arr[i]=0;
        // fill ones
        }
        for(int i=numberOfZeros; i<numberOfOnes+numberOfZeros; i++){
            arr[i]=1;
        }
        // fill 2s
        for(int i=numberOfOnes+numberOfZeros; i<arr.length; i++){
            arr[i]=2;
        }
    }
    public static void main(String[] args) {
        int[] arr = {1,0,0,2,0,2,1,2,1,0,2,1};
        for(int ele: arr) System.out.print(ele+" ");

        System.out.println();

        sort0s1s2s(arr);

        for(int ele:arr) System.out.print(ele+" ");
        
    
    }
}
