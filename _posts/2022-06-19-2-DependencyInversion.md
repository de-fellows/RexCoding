---
toc: true
layout: post
description: Complete translation of Python code to Java
categories: [Python, Java, OOP]
title: Dependency Inversion in Java
author: <a href="https://github.com/sinapordanesh">Saman Pordanesh</a>
---


# [Dependency Inversion](https://www.youtube.com/watch?v=Kv5jhbSkqLE) **principles code translation in Java** 

*Published by* [Saman Pordanesh](https://github.com/sinapordanesh)

## **General Introduction** 

- This topic discusses how we can implement some object-oriented definitions like [Abstraction](https://en.wikipedia.org/wiki/Abstraction_\(computer_science\)) or [Interfaces](https://en.wikipedia.org/wiki/Interface_\(computing\)) in a language like a python which doesn’t have these definitions locally. 
As Java is a strong OOP language, we already have these definitions for it. We will implement the translation of the video’s code here to understand how these principles work on Java.
- You need to watch the [video](https://www.youtube.com/watch?v=Kv5jhbSkqLE) first, understand all principles, and then look at the translation codes in Java. This documentation will help you to understand the translation better
- This translation is based on the final code source of Dependency Inversion lessons in python programming languages (***dependency-inversion-after.py***)
- We need a separate class with the ***main*** function to run the program, despite Python, in which you can run each ***.py*** file individually. ***Main.java*** is the file with the main function for that purpose.
- Standard naming on java is different. You can find more information [here](https://www.oracle.com/java/technologies/javase/codeconventions-namingconventions.html).

## **Directories changes** 

- This is one of the most significant changes we made to our translation. A **Java** project with an exact directory with all dependencies can be good practice for OOP designing. 
- We defined a package name for this project as ***edu.def.di*** ([package naming standards](https://docs.oracle.com/javase/tutorial/java/package/namingpkgs.html)) and its specific directory under the ***src*** folder. This package name keeps all project components connected to gather when we implement them on different ***.java*** files.
- However, packages are not necessary, you could use a default package, or even have all classes in the same file; this is more Java best practice.
- More information about **Java’s** project directory standards is [here](https://www.ibm.com/docs/en/i/7.1?topic=topics-java-classes-packages-directories).

## **Implementational Instruction**

1. we create one ***.java*** file per each class under ***edu.def.di*** package.
1. We are going to discuss ***Switchable*** class more here. This class is an interface class and we use the “***interface***” keyword instead of “***class***”. But why this is an interface? The answer is that this class just contains the prototypes of methods without any implementation. It is an index which shows a specific structure but can have different functionality when we override it on the child class. Please read about the [interface on OOP](https://en.wikipedia.org/wiki/Interface_\(computing\)) and [interface on java](https://www.w3schools.com/java/java_interface.asp).
1. When we created other classes (***LightBulb.java***, ***Fan.java***, ***ElectricPowerSwitch.java***), we need ***Main.java*** to contain our main function to run the program.
1. After that, we will start to translate all classes to their belonging files based on the ***P*ython** source. We will compare all of them with the original version in the following section.

## **Compiling Instruction**

- Run the command prompt inside the ***src*** folder.
- Run the following command to compile all ***.java*** files:
```
javac edu/def/di/*.java
```
- To execute the program, we should run the ***Main.java*** file from the command prompt. To do this, from the same directory, run the following command on the command prompt:
```
java edu.def.di.Main
```
If your ***main*** function is in a different class, put the name of that class instead of ***Main*** at the end of the command
- You can find more about compiling instruction [here](https://docs.oracle.com/javase/7/docs/technotes/tools/windows/javac.html)

## **Classes changes** 

### ***Switchable***


##### **Python version** 

```python
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass
```

##### **Java version** 

```java
package edu.def.di;

public interface Switchable {
    void turnOn();
    void turnOff();
}
```

1. This class is the main lesson for this session, as we are talking about interface and ***Switchable*** is an interface class. As we can see, we implemented it with “***interface***” keyword and it just contains prototype of each method, without any implementation or parameter.
1. As we don’t have interface in **python**, this class needs to inherit ***ABC*** class to act like an **abstract** class, although in **Java** we already have **abstract** and **interface** definitions locally. (in python version he used ***“@abstractmethod”*** keyword to show that they are abstract methods. Also, there are differences between **abstract** and **interface** which recommend [learning about them](https://stackoverflow.com/questions/1913098/what-is-the-difference-between-an-interface-and-abstract-class#:~:text=The%20key%20technical%20differences%20between,have%20constants%20and%20methods%20stubs.).)
1. Its child classes will inherit all methods from it, and we will implement all methods at child classes under the ***“@Override”*** keyword.
1. As we talked about it before, we don’t need any implementation for both ***turnOn*** and ***turnOff*** methods at the interface.


### ***LightBulb***

##### **Python version** 

```python
class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")
```

##### **Java version** 

```java
package edu.def.di;

public class LightBulb implements Switchable{
    @Override
    public void turnOn() {
        System.out.println("LightBulb: turned on...");
    }

    @Override
    public void turnOff() {
        System.out.println("LightBulb: turned off...");
    }
}
```


1. This is one of the ***Switchable*** children which is inheriting all methods from its parent class.
1. “***Implements Switchable***” is the keyword for inheritance. 
1. As its obvious, all methods from interface parent are being overriding in this class, although we can have more methods and parameters in this class which don’t have any connection whith the parent class. 
1. Notice that in **python** version we simply use general inheritance implementation and redefine all methods without any keyword.

### ***Fan***


##### **Python version** 

```python
class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")
```

##### **Java version** 

```java
package edu.def.di;

public class Fan implements Switchable{
    @Override
    public void turnOn() {
        System.out.println("Fan: turned on...");
    }

    @Override
    public void turnOff() {
        System.out.println("Fan: turned off...");
    }
}
```

The same points as ***LightBulb*** class. 

### ***ElectricPowerSwitch***

##### **Python version** 

```python
class ElectricPowerSwitch:

    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True
```

##### **Java version** 

```java
package edu.def.di;

public class ElectricPowerSwitch {

    private Switchable client;
    private boolean on = false;

    ElectricPowerSwitch(Switchable client){
        this.client = client;
    }

    public void press(){
        if (on){
            client.turnOff();
            on = false;
        } else {
            client.turnOn();
            on = true;
        }
    }
}
```

1. This is a general class with specific functionality to act as an electric device. We will define the kind of device by passing related object to this class (this is an Aggregation relationship. More [here](https://www.scaler.com/topics/association-composition-and-aggregation-in-java/)). 
1. We have two parameters. The first one (***client***) is a non-primary data type with type of ***Switchable*** and we will define its value on the class constructor. The second one (***on***) is a primary data type ***Boolean*** with a default value of ***false***. In addition a public method ***press.***
