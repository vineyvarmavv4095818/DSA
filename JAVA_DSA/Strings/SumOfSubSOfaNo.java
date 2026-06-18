public class SumOfSubSOfaNo {
    public static void main(String[] args) {
        String s = "6759";
        int sum = 0;
        for(int j =0; j<s.length(); j++){
        for(int i = j+1; i<=s.length(); i++){  //j+1 isliye kiya kyuki i ko hr bar 1 se start nhi kr skte i hmesha j se ek index aage jayega
            sum += Integer.parseInt(s.substring(j,i));
            }
        }
        System.out.println(sum);
    }
}
