package normal;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Random;

// じゃんけん
// 複数人でじゃんけん
// 最初に人数の設定
// 最後のひとりまでやる
public class Main {
  // 1対１
  public static void main(String[] args) throws IOException, InterruptedException{
    // 入力の準備
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    // ランダムクラスメソッド
    Random random = new Random();
    // 手
    String[] hand = {"グー","チョキ","パー"};
    // 難易度
    int[] battle = {3,5,10};

    // 挨拶
    System.out.println("ようこそジャンケンシステムへ");
    System.out.println("早速、じゃんけんしましょう");

    System.out.println("難易度を選択してください。1:3連勝、2:5連勝、3:10連勝");
    int select = Integer.parseInt(reader.readLine())-1;
    int win = 0;
    while(win< battle[select]){
      System.out.println("手を選んでください。1:グー、2:チョキ、3:パー");
      int num1 = Integer.parseInt(reader.readLine()) - 1;

      int num2 = random.nextInt(hand.length);

      System.out.println("それでは");
      System.out.println("じゃんけん！！！！！");
      Thread.sleep(1000);
      System.out.println("ポン！！！");

      System.out.println(hand[num1] + "vs" + hand[num2]);
      // あいこ
      if (num1 == num2) {
        System.out.println("あいこ～～！！");
      // プレイヤーの勝ち
      } else if ((num1 == 0 && num2 == 1) || (num1 == 1 && num2 == 2) || (num1 == 2 && num2 == 0)) {
        System.out.println("プレイヤーの勝ち！！");
        win++;
      } else {
        System.out.println("NPCの勝ち！！");
        System.out.println("まったね～～～！！");
        break;
      }
    }
  }
}
