package normal;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 計算機
// 普通
// 無限ループなし
public class Cal_main {
  public static void main(String[] args) throws IOException {
    // 入力の準備
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    String str;

    // 計算内容メッセージ
    String[] calc = {"1:加算","2:減算","3:乗算","4:除算"};

    // 計算結果
    int result;

    // メッセージ
    System.out.println("計算システムです。");
    System.out.println("計算内容を選んでください。");
    System.out.println("1:加算、2:減算、3:乗算、4:除算");

    // 計算内容
    // 入力
    str = reader.readLine();
    // 数値に変換
    int select = Integer.parseInt(str);

    System.out.println(calc[select-1] + "で実施します。");

    // 1個目の数値
    System.out.println("１つ目の数値を入力してください");
    // 入力
    str = reader.readLine();
    // 数値に変換
    result = Integer.parseInt(str);

    // 2個目の数値
    System.out.println("２つ目の数値を入力してください");
    // 入力
    str = reader.readLine();
    // 数値に変換
    int num = Integer.parseInt(str);

    // 計算
    switch (select) {
      // 加算
      case 1:
        result += num;
        break;

      // 減算
      case 2:
        result -= num;
        break;

      // 乗算
      case 3:
        result *= num;
        break;

      // 除算
      case 4:
        result /= num;
        break;
    }
    // 計算結果の表示
    System.out.println("計算結果：" + result);
    // システム終了
    System.out.println("システムを終了します。");
  }
}