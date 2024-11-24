import java.util.Scanner;

public class MayorOMenor {
    public static void main(String[] args) {
        // Crear un objeto Scanner para leer la entrada del usuario
        Scanner scanner = new Scanner(System.in);

        // Solicitar al usuario que ingrese un número
        System.out.print("Ingresa un número: ");
        int numero = scanner.nextInt();

        // Comparar el número con 10 y mostrar el resultado
        if (numero > 10) {
            System.out.println("Es mayor que 10");
        } else if (numero < 10) {
            System.out.println("Es menor que 10");
        } else {
            System.out.println("Es igual a 10");
        }

        // Cerrar el objeto Scanner
        scanner.close();
    }
}
