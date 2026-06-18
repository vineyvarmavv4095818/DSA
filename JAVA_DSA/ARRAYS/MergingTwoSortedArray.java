public class MergingTwoSortedArray {
    public static void main(String[] args) {
        int[] a = {2,3,4,5,19,22};
        int[] b = {1,7,11,20,};

        //print 0 array:

        int[] c = new int[a.length+b.length];
        for(int ele: c) System.out.print(ele+" ");
        System.out.println();
        
        //function call:

        merge(a,b,c);
        for(int ele: c) System.out.print(ele+" ");
        System.out.println();
    }

    public static void merge(int[] a, int[] b, int[] c) {
        int i=0, j=0, k=0;

        while(i<a.length && j<b.length){
            if(a[i]<b[j]) c[k++] = a[i++];
            else c[k++] = b[j++];
        }

        while(i<a.length) c[k++] = a[i++];
        while(j<b.length) c[k++] = b[j++];

    }

}
