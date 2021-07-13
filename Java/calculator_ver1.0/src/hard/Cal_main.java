package hard;
// 計算機

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 無限ループあり
// 数値は配列に格納
public class Cal_main {
  public static void main(String[] args) throws IOException {
    // 入力の準備
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

    // 計算内容メッセージ
    String[] calc = { "1:加算", "2:減算", "3:乗算", "4:除算" };

    // メッセージ
    System.out.println("計算システムです。");

    while (true) {
      // 計算結果
      int result = 0;

      // 数値入力
      int[] num = new int[1];

      System.out.println("計算内容を選んでください。");
      System.out.println("1:加算、2:減算、3:乗算、4:除算");

      // 計算内容
      // 入力 + 数値に変換0
      int select = Integer.parseInt(reader.readLine());

      // 無効な入力
      if (select >= 5 || select <= 0) {
        System.out.println("選択肢が無効です。");
        continue;
      }

      System.out.println(calc[select-1] + "で計算します。");

      // 1個目の数値
      System.out.println("１つ目の数値を入力してください");
      // 入力 + 数値に変換
      result = Integer.parseInt(reader.readLine());

      // 2個目の数値
      System.out.println("2つ目の数値を入力してください");
      // 数値に変換
      num[0] = Integer.parseInt(reader.readLine());

      // 計算
      for (int value : num) {
        switch (select) {
          // 加算
          case 1:
            result += value;
            break;

          // 減算
          case 2:
            result -= value;
            break;

          // 乗算
          case 3:
            result *= value;
            break;

          // 除算
          case 4:
            result /= value;
            break;
        }
      }

      // 計算結果の表示
      System.out.println("計算結果：" + result);

      System.out.println("終了しますか?");
      System.out.println("1：はい、2：いいえ");

      // 入力 + 数値に変換
      select = Integer.parseInt(reader.readLine());
      // はいの場合
      if (select == 1) {
        break;
      }
    }
    // システム終了
    System.out.println("システムを終了します。");
  }
}