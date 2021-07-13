package very_hard;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Battle {
  // 入力の準備
  BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
  // ランダムクラスメソッド
  Random random = new Random();
  // 手
  String[] hand = { "グー", "チョキ", "パー" };

  // 参加する人数の手を格納するリスト
  List<Integer> nList = new ArrayList<>();

  // 参加人数を取得する
  int human_num = 0;

  public Battle() {
    // 挨拶
    System.out.println("ようこそジャンケンシステムへ");
  }

  public List<Integer> hand_choice(int human_num) throws IOException, InterruptedException {
    this.human_num = human_num;
    System.out.println("手を選んでください。1:グー、2:チョキ、3:パー");
    nList.add(Integer.parseInt(reader.readLine()) - 1);

    for (int i = 1; i < human_num; i++) {
        nList.add(random.nextInt(hand.length));
    }

    System.out.println("それでは");
    System.out.println("じゃんけん！！！！！");
    Thread.sleep(1000);
    System.out.println("ポン！！！");

    for (int value : nList) {
      System.out.print(hand[value] + " ");
    }
    return nList;
  }

  public int win(List<Integer> nList) {
    int rock = 0;
    int scissors = 0;
    int paper = 0;

    for (int value : nList) {
      if (value == 0) {
        // グー
        rock++;
      } else if (value == 1) {
        scissors++;
      } else {
        paper++;
      }
    }
    // あいこ
    if ((rock > 0 && scissors > 0 && paper > 0)||()) {
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
