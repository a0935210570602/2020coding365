import java.util.Scanner;
public class ScannerDemo {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Please type your name:");
        System.out.printf("Hello! %s!\n", scanner.next());
       }
}