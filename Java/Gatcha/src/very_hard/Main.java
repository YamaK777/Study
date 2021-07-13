package very_hard;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// ガチャ
// 10連とBOXガチャ
// ガチャ切り替えで切り替えれる
// Resultクラスで排出結果を表示
// Characterクラスでキャラの詳細を格納
// レア度、名前、詳細...
// 結果はリストに格納
public class Main {
  public static void main(String[] args) throws IOException {
		// 入力準備
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

    // resultクラスのオブジェクト生成
    Result result = new Result();
    // 返答
    String ans = "1";

    while (ans.equals("1")) {
      System.out.println("引くガチャの形式を選択してください。(1：普通、2：BOX、その他：終了)");
      // ガチャ形式
      String select = reader.readLine();
      // 選択があっている
      if (select.equals("1") || select.equals("2")) {
        System.out.println("何連で引きますか。(1：単発、2：10連、その他：終了)");
        // 何連か
        String shot_num = reader.readLine();

        // 選択があっている
        if (shot_num.equals("1") || shot_num.equals("2")) {
          while (ans.equals("1")) {
            // 普通
            if (select.equals("1")) {
              // 結果を出力
              result.gatcha(Integer.parseInt(shot_num));
            } else {
              // BOXガチャの結果を出力
              result.box_gatcha(Integer.parseInt(shot_num));
            }
            System.out.println("もう一度ガチャを引きますか？(1：はい、その他のボタン：いいえ)");
            // 回答を入力
            ans = reader.readLine();
          }
        }
      }
      System.out.println("ガチャを切り替えますか？(1：はい、その他のボタン：いいえ)");
      // 回答を入力
      ans = reader.readLine();
    }
	}
}
