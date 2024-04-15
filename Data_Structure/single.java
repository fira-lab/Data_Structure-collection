class Animal { 
protected String name; 
protected void display() { 
	System.out.println("I am an animal.");  } 
} 
class Dog extends Animal { 
public void getInfo() { 
	System.out.println("My name is " + name); 
} 
} 
class single { 
public static void main(String[] args) { 
       Dog dog1 = new Dog(); 
       dog1.name = "Rocky"; 
       dog1.display(); 
       dog1.getInfo(); 
} 
}