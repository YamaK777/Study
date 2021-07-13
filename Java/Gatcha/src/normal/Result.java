package normal;

import java.util.Random;

public class Result {
  // ランダム生成クラスのオブジェクト生成
  Random random = new Random();
  // ガチャ
  void gatcha(int shot) {
    for (int i = 0; i < shot; i++) {
      // 0から99までの整数をランダムで生成
      int rate = random.nextInt(100);
      if (95 <= rate) {
        System.out.println("SSRが当たりました。");
      } else if (80 <= rate) {
        System.out.println("SRが当たりました。");
      } else {
        System.out.println("Rが当たりました。");
      }
    }
  }
}
