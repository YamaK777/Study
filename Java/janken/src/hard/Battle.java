package hard;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Random;

public class Battle {
  // 入力の準備
  BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
  // ランダムクラスメソッド
  Random random = new Random();
  // 手
  String[] hand = { "グー", "チョキ", "パー" };

  int[] num = new int[2];

  public Battle() {
    // 挨拶
    System.out.println("ようこそジャンケンシステムへ");
  }

  public int[] hand_choice() throws IOException, InterruptedException {
    System.out.println("手を選んでください。1:グー、2:チョキ、3:パー");
    num[0] = Integer.parseInt(reader.readLine()) - 1;

    num[1] = random.nextInt(hand.length);

    System.out.println("それでは");
    System.out.println("じゃんけん！！！！！");
    Thread.sleep(1000);
    System.out.println("ポン！！！");

    System.out.println(hand[num[0]] + "vs" + hand[num[1]]);
    return num;
  }

  public int win(int[] num) {
    // あいこ
    if (num[0] == num[1]) {
      System.out.println("あいこ～～！！");
      return 0;
    // プレイヤーの勝ち
    } else if ((num[0] == 0 && num[1] == 1) || (num[0] == 1 && num[1] == 2) || (num[0] == 2 && num[1] == 0)) {
      System.out.println("プレイヤーの勝ち！！");
      return 1;
    } else {
      System.out.println("NPCの勝ち！！");
      System.out.println("まったね～～～！！");
      return 2;
    }
  }
}
