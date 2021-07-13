package hard;

import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;


public class Result {

  // 排出の順番
  private String[] character = { "R", "SR", "SSR" };

  // 配列の
  private int[] result = new int[100];

  // 回数の管理
  private int shot_time = 1;

  // コンストラクタ
  public Result() {
    int a = 0;
    for (int i = a; i < 80; i++) {
      result[i] = 0;
      a++;
    }
    for (int i = a; i < 95; i++) {
      result[i] = 1;
      a++;
    }
    for (int i = a; i < 100; i++) {
      result[i] = 2;
    }
    // 中身をシャッフル
    result = shuffle(result);
  }

  // ガチャ結果
  void gatcha(int shot) {
    for (int i = 0; i < shot; i++) {
      int rare = result[shot_time - 1];
      System.out.println(character[rare] + "が当たりました。");
      shot_time++;
      if (shot_time > result.length) {
        System.out.println("天井になりましたBOXがリセットされます。");
        // 中身をシャッフル
        result = shuffle(result);
        // 回数リセット
        shot_time = 1;
      }
    }
  }

  private int[] shuffle(int[] array) {
        // 配列が空か１要素ならそのままreturn
        if (array.length > 1) {
          // Fisher–Yates shuffle
          Random rnd = ThreadLocalRandom.current();
          for (int i = array.length - 1; i > 0; i--) {
            int index = rnd.nextInt(i + 1);
            // 要素入れ替え(swap)
            int tmp = array[index];
            array[index] = array[i];
            array[i] = tmp;
          }
        }
        return array;
    }
}
