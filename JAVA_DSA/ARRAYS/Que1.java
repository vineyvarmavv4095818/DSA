public class Que1 {
    public static void segregateoand1(int[] arr) {
        // int numberOfZeros = 0;
        // int numberOfOnes = 0;

        // // count number of zeros and ones.

        // for(int ele: arr){
        //     if(ele==0) numberOfZeros++;
        //     else numberOfOnes++;

        // }
        // // fill zeros
        // for(int i=0; i<numberOfZeros; i++){
        //     arr[i]=0;
        // }
        // for(int i=numberOfZeros; i<arr.length; i++){
        //     arr[i]=1;
        // }

        int n = arr.length;
        int i=0, j=n-1;

        while(i<j){
            if(arr[i]==0) i++;
            if(arr[j]==1) j--;
            if(i>j) break;

            if(arr[i]==1 && arr[j]==0)
                arr[i]=0;
                arr[j]=1;
                i++;
                j--;
                
        }

    }
    
    public static void main(String[] args) {
        int[] arr = {1,0,0,0,1,1,0,1};
        for(int ele: arr) System.out.print(ele+" ");

        System.out.println();

        segregateoand1(arr);

        for(int ele:arr) System.out.print(ele+" ");
        
    }

    
}
