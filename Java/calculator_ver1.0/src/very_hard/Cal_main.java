package very_hard;
// 計算機

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;


// 無限ループあり
// 数値はリストに格納
// 数値は最初に指定した数だけ計算する
public class Cal_main {
  public static void main(String[] args) throws IOException {
    // 入力の準備
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

    // メッセージ
    System.out.println("計算システムです。");

    while (true) {
      // 計算結果
      int result = 0;

      // 数値入力
      List<Integer> numList = new ArrayList<>();

      // 計算内容
      System.out.println("計算内容を選んでください。");
      System.out.println("1:加算、2:減算、3:乗算、4:除算");
      // 入力
      // 数値に変換
      int select = Integer.parseInt(reader.readLine());

      // 無効な入力
      if (select >= 5 || select <= 0) {
        System.out.println("選択肢が無効です。");
        continue;
      }

      // 何個で計算するか
      System.out.println("何個計算しますか？");
      // 入力
      // 数値に変換
      int num = Integer.parseInt(reader.readLine());

      // 1個目の数値
      System.out.println("１つ目の数値を入力してください");
      // 入力
      // 数値に変換
      result = Integer.parseInt(reader.readLine());

      for (int i = 2; i < num + 1; i++) {

        System.out.println(i + "つ目の数値を入力してください");
        // 入力
        // 数値に変換してリストに格納
        numList.add(Integer.parseInt(reader.readLine()));
      }


      // 計算
      for (int value : numList) {
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

      // 入力
      // 数値に変換
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