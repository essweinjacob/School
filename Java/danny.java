package fibonacci;
import java.util.*;

public class danny{
    public static void main(String[] args){
        int[][] fibArray = new int[3][100];
        for(int rows = 0; rows < fibArray.length; rows++){
            for(int cols = 0; cols < fibArray[rows].length; cols++){
                fibArray[rows][cols] = 0;
            }
        }
        fibArray[0][99] = 0;
        fibArray[1][99] = 1;

        Scanner input_scan = new Scanner(System.in);
        System.out.print("Enter the n terms: ");
        int user_input;
        user_input = input_scan.nextInt();

        int carry = 0;
        int counter = 2;
        for(int i =2; i <= user_input; i++){
            if((fibArray[(i+1)%3][0] + fibArray[(i+2)%3][0] + carry) >= 10){
                System.out.println("Error");
                break;
            }
            for(int digit = 99; digit >= 0; digit--){
                int num = fibArray[(i+3)%3][digit] + fibArray[(i+2)%3][digit] + carry;
                fibArray[(i+3)%3][digit] = num % 10;
                carry = num / 10;
            }
            counter++;
        }
        for(int cols = 0; cols < fibArray[(counter - 1) % 3].length; cols++){
            System.out.print(fibArray[(counter - 1 + 3) % 3][cols]);
        }
        System.out.println();
        System.out.println("Number of times: " + (counter - 1));
        input_scan.close();
    }
}
