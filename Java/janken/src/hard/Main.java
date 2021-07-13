package hard;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

// じゃんけんクラスと
// 個人情報クラスを作成
public class Main {
  // 1対１
  public static void main(String[] args) throws IOException, InterruptedException{
    // 入力の準備
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

    // じゃんけんクラスのオブジェクト生成
    Battle battle = new Battle();
    // 個人情報クラスのオブジェクト生成
    Human human = new Human();

    List<Human> humans = new ArrayList<>();

    // 難易度
    int[] difficult = { 3, 5, 10 };

    // 勝ち数
    int win = 0;

    System.out.println("まずは年齢を記入してね");
    int age = Integer.parseInt(reader.readLine()) - 1;
    human.setAge(age);

    System.out.println("次は名前を記入してね");
    String name = reader.readLine();
    human.setName(name);

    System.out.println("難易度を選択してください。1:3連勝、2:5連勝、3:10連勝");
    int select = Integer.parseInt(reader.readLine()) - 1;

    System.out.println("早速、じゃんけんしましょう");

    while (win < difficult[select]) {
      int[] num = battle.hand_choice();
      int result = battle.win(num);

      if (result == 1) {
        win++;
      } else if (result == 2) {
        break;
      }
    }
    human.setWin(win);
    humans.add(human);
  }
}