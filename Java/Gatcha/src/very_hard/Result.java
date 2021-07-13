package very_hard;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class Result {
  Random random = new Random();

  // 何連を格納
  final int[] shot_num = { 1, 10 };
  // レア度を格納
  final String[] rare = { "R", "SR", "SSR" };

  private Character character;

  String[][] nama = { { "1", "ローラ" }, { "1", "サラ" }, { "1", "ジェニファ" }, { "1", "ヘレン" }, { "1", "エリザベス" }, { "1", "アンナ" },
      { "1", "アン" }, { "1", "エイミ" }, { "1", "ジョディ" }, { "1", "ケリァ" }, { "1", "モリー" }, { "1", "エリザベス" }, { "1", "キム" },
      { "1", "レベッカ" }, { "1", "エイミー" }, { "1", "ジュリー" }, { "1", "メラニー" }, { "1", "アン・ジョ" }, { "1", "メラニー" },
      { "1", "ステファニ" }, { "1", "アンジェラ" }, { "1", "シンシア" }, { "2", "ニコール" }, { "2", "リー・テッリ" }, { "2", "メアリー" },
      { "2", "ローラ・K" }, { "2", "サマンサ・E" }, { "2", "キャサリン" }, { "3", "ベッツィ" } };

  // ガチャの中身のリスト
  private List<Character> charaList = new ArrayList<>();

  // 回数の管理
  private int shot_time = 1;

  // コンストラクタ
  public Result() {
    for (String value[] : nama) {
      // ガチャの排出キャラクラスのオブジェクト生成
      character = new Character();

      character.setRare(Integer.parseInt(value[0]));
      character.setName(value[1]);

      charaList.add(character);
    }
    // 中身をシャッフル
    Collections.shuffle(charaList);
  }

  // Boxガチャ結果
  void box_gatcha(int shot) {
    for (int i = 0; i < shot_num[shot-1]; i++) {
      character = charaList.get(shot_time - 1);
      int num = character.getRare();
      System.out.println(rare[num-1] + ":" + character.getName() + "が当たりました。");
      shot_time++;
      if (shot_time > charaList.size()) {
        System.out.println("天井になりましたBOXがリセットされます。");
        // 中身をシャッフル
        Collections.shuffle(charaList);
        // 回数リセット
        shot_time = 1;
      }
    }
  }

  // 普通
  void gatcha(int shot) {
    for (int i = 0; i < shot_num[shot - 1]; i++) {
      // ランダム数
      int num = random.nextInt(charaList.size());
      character = charaList.get(num);
      // レア度取得
      num = character.getRare();
      System.out.println(rare[num-1] + ":" + character.getName() + "が当たりました。");
    }
  }
}