import java.util.Scanner;
public class crt9_9_25 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // System.out.println("enter number");
        // int n = sc.nextInt();
        // System.out.println("enter start");

        // 2 4 8 16 32
        // int start = sc.nextInt();
        // for(int i = 0; i < n;i++){
        //     System.out.print(start + " ");
        //     start *= 2;
        // }

        // // 2 4 8 16 32 64
        // int start = sc.nextInt();
        // for(int i = 0; i < n;i++){
        //     System.out.print(start + " ");
        //     start *= 2;
        // }

        // 5 7 9 11 13 15 
        // int start = sc.nextInt();
        // for(int i = 0; i < n;i++){
        //     System.out.print(start + " ");
        //     start += 2;
        // }        


        // for(int i = 0; i < 4; i++){
        //     System.out.println("* $ @");
        // }

        // int start = 65;
        // int end = 90;
        // int n = sc.nextInt(); 
        // for(int i = 0; i < n; i++){
        //     System.out.println((char)start + "" + (char)end);
        //     start++;
        //     end--;
        // }


        // int start = 97;
        // int end = 65;
        // int n = sc.nextInt(); 
        // for(int i = 0; i < n; i++){
        //     System.out.println((char)start + "" + (char)end);
        //     start++;
        //     end++;
        // }

        int n =  sc.nextInt();
        int m = sc.nextInt();
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                System.out.print("* ");
            }
            System.out.println();
        }   
    }
}

