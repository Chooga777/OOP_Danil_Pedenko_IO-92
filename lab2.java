public class lab2 {
    public static void main(String[] args) {
        short[][] twoDimArray = {{5, 7, 3, 9}, {7, 0, 1, 9}, {8, 1, 2, 3}, {1, 2, 3, 4}};
        short[][] Ctrans = new short[twoDimArray.length][twoDimArray.length];
        short sum_max = 0;
        //Вивід початкової матриці;
        System.out.println("Початкова матриця:");
        for (short i = 0; i < twoDimArray.length; i++) {
            for (short j = 0; j < twoDimArray.length; j++) {
                System.out.print(" " + twoDimArray[i][j] + " ");
            }
            System.out.println();
        }
        //Формування транспанованої матриці;
        for (short i = 0; i < twoDimArray.length; i++) {
            for (short j = 0; j < i; j++) {
                short temp = twoDimArray[i][j];
                twoDimArray[i][j] = twoDimArray[j][i];
                twoDimArray[j][i] = temp;
            }
            Ctrans[i] = twoDimArray[i];
        }
        //Вивід траспанованої матриці;
        System.out.println("Транспонована матриця:");
        for (short i = 0; i < Ctrans.length; i++) {
            for (short j = 0; j < Ctrans.length; j++) {
                System.out.print(" " + Ctrans[i][j] + " ");
            }
            System.out.println();
        }
        //Пошук та сума найбільших елементів кожного рядка;
        System.out.println("Сума максимальних елементів кожного рядка матриці:");
        for (short i = 0; i < Ctrans.length; i++) {
            short max = Ctrans[i][0];
            for (short j = 0; j < Ctrans.length; j++) {
                if (max < Ctrans[i][j]) {
                    max = Ctrans[i][j];
                }
            }
            sum_max += max;
        }
        System.out.println(sum_max);
    }
}
