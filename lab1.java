public class lab1 {
    public static void main(String[] args){
        //Ініціалізація змінних;
        int a=1, b=1, n=20, m=20, i, j;
        int s = 0;
        //Перевірка ділення на 0;
        if (b != 0){
            for (i=a; i<=n; i++){
                //Перевірка ділення на 0;
                if (i-2 != 0){
                    for (j=b; j<=m; j++){
                        s += (i/j)/(i-2);
                    }
                }else {
                    System.out.println("Ділення на 0");
                }
            }
        }else {
            System.out.println("Помилка виконання");
        }
        //Кінцевий результат;
        System.out.println("S = " + s);
    }
}
