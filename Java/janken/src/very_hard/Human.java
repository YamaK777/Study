package very_hard;

public class Human {
  private int age;
  private String name;
  private int win;

  public Human() {
    System.out.println("まずはユーザ情報を記入してね！！");
  }

  public int getAge() {
    return age;
  }
  public void setAge(int age) {
    this.age = age;
  }
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public int getWin() {
    return win;
  }

  public void setWin(int win) {
    this.win = win;
  }
}
