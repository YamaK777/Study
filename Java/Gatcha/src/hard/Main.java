package hard;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// ガチャ
// resultクラスで排出結果を表示
// BOXガチャ
// R,SR,SSRで天井まで回せばキャラは全部出る
// ヒント：R:80個、SR:15個、SSR:5個の配列を作成する
// キャラ名等なし
public class Main {
  public static void main(String[] args) throws IOException {
		// 入力準備
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

    // resultクラスのオブジェクト生成
    Result result = new Result();

    // 何連を格納
    int[] shot = { 1, 10 };

    System.out.println("引くガチャの形式を選択してください。(1：単発、2：10連、その他：終了)");

    // ガチャ形式
    String select = reader.readLine();

    if (select.equals("1") || select.equals("2")) {
      System.out.println("ガチャを引きますか？(1：はい、その他のボタン：いいえ)");
      // ガチャを引くか確認
      String ans = reader.readLine();
      // はいを選択
      if (ans.equals("1")) {
        while (true) {
          // 結果を出力
          result.gatcha(shot[Integer.parseInt(select) - 1]);

          System.out.println("もう一度ガチャを引きますか？(1：はい、その他のボタン：いいえ)");

          ans = reader.readLine();

          if (!ans.equals("1")) {
            break;
          }
        }
      }
      System.out.println("システムを終了します。");
    }
	}
}
