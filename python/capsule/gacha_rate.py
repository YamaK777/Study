import sys
import random as ran

class capsule_toy():
  # コンストラクタ
  def __init__(self):
    print("ようこそガチャ沼へ")
    self.normal = ["N1", "N2", "N3", "N4", "N5"]
    self.rare = ["R1", "R2", "R3", "R4", "R5", "R6", "N7"]
    self.ultra_rare = ["UR1","UR2"]
    # self.capsule = ["N","R","SR"]
    # self.probably = [0.8,0.15,0.05]
    self.diamond = 100
    self.result = []


  # ガチャの回数を選択
  def select(self):
    while True:
      try:
        print("ガチャを選んでください １:単発,２：１０連")
        print(f"残りダイヤ:{self.diamond}")
        self.num = int(input())
      except ValueError:
        print("無効な入力です。")
      else:
        if self.num == 2:
            self.num = 10
        break
    return self.num

  # ガチャの排出
  def choice(self,num):
    print(num)
    # self.result = ran.choices(self.capsule, weights=self.probably, k=num)
    for i in range(0,num):
      a = ran.randint(1,100)
      if a >=80:
        self.result.append(self.normal[ran.randint(0, len(self.normal)-1)])

      elif a>=15:
        self.result.append(self.rare[ran.randint(0, len(self.rare)-1)])

      else:
        self.result.append(self.ultra_rare[ran.randint(0, len(self.ultra_rare)-1)])

    return self.result

  def show(self,result):
    print("ガチャの結果は")
    for value in result:
      print(value)
    print("です")





