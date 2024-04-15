abstract class Animal {
  private String name;

  public Animal(String name) {
      this.name = name;
  }

  public abstract void makeSound();

  public void sleep() {
      System.out.println(name + " is sleeping.");
  }
}

class Lion extends Animal {
  public Lion(String name) {
      super(name);
  }

  public void makeSound() {
      System.out.println("The lion roars.");
  }
}

class Tiger extends Animal {
  public Tiger(String name) {
      super(name);
  }

  public void makeSound() {
      System.out.println("The tiger growls.");
  }
}

public class Main {
  public static void main(String[] args) {
      Lion lion = new Lion("Simba");
      lion.makeSound();
      lion.sleep();

      Tiger tiger = new Tiger("Raja");
      tiger.makeSound();
      tiger.sleep();
  }
}