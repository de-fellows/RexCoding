---
toc: true
layout: post
description: Cmpletete traslation of Python code to Java.
categories: [Python, Java, OOP]
title: SOLID principles in Java
author: <a href="https://github.com/sinapordanesh”>Saman Pordanesh</a>
---

# [Object Pool](https://www.youtube.com/watch?v=Rm4JP7JfsKY&t=407s) **code translation in Java**
 **General Introduction** 

*Published by* [Saman Pordanesh](https://github.com/sinapordanesh)

## **General Instructions**

- [Object pool pattern](https://www.geeksforgeeks.org/object-pool-design-pattern/) is a software creational design pattern which is used in situations where the cost of initializing a class instance is very high.
- You need to watch the [video](https://www.youtube.com/watch?v=Rm4JP7JfsKY&t=407s) first, understand all principles, and then look at the translation codes in **Java**. This documentation will help you to understand the translation better.
- This translation is based on the final code source of the **Object Creation** lessons in python programming languages (***object-pool.py***).
We skipped ***Object Pool Context*** and ***Singleton*** lessons in this translation for just focusing on ***Object Pool***. 
- We need a separate class with the ***main*** function to run the program, despite **Python**, in which you can run each ***.py*** file individually. ***Main.java*** is the file with the main function for that purpose.
- Standard naming on **Java** is different. You can find more information [here](https://www.oracle.com/java/technologies/javase/codeconventions-namingconventions.html).

## **Directories changes**
 
- This is one of the most significant changes we made to our translation. A **Java** project with the same directory with all dependencies can be good practice for OOP designing.
- We defined a package name for this project as ***edu.def.op*** ([package naming standards](https://docs.oracle.com/javase/tutorial/java/package/namingpkgs.html)) and its specific directory under the ***src*** folder. This package name keeps all project components connected to gather when we implement them on different ***.java*** files. 
- However, packages are unnecessary; you could use a default package or even have all classes in the same file; this is more **Java** best practice.
- More information about **Java’s** project directory standards is [here](https://www.ibm.com/docs/en/i/7.1?topic=topics-java-classes-packages-directories).

## **Implementational Instruction**

1. this lesson will be an easy one in terms of translation. We recommend focusing on Object Pool definition and principles more. You can find good resources on the internet. In addition, these two articles may help [1](https://en.wikipedia.org/wiki/Object_pool_pattern), [2](https://www.geeksforgeeks.org/object-pool-design-pattern/).
1. We will create one ***.java*** file per class under ***edu.def.op*** package.
They can be interfaces and child classes or simple classes.
1. ***Main.java*** contains our ***main ()*** method to run the program.
1. Note that all steps here are entirely for the best **OOP** practice in **Java** programming; They can be done more straightforwardly, but not the best **OOP** ways.  

## **Compiling Instruction**

- Run the command prompt inside the ***src*** folder.
- Run the following command to compile all ***.java*** files:
```
javac edu/def/op/*.java
```
- To execute the program, we should run the ***Main.java*** file from the command prompt. To do this, from the same directory, run the following command on the command prompt:
```
java edu.def.op.Main
```
- If your main function is in a different class, but the name of that class instead of ***Main*** at the end of the command
- You can find more about compiling instructions [here](https://docs.oracle.com/javase/7/docs/technotes/tools/windows/javac.html).


## **Classes changes** 

### ***Reusable***

##### ***Python version***

```python
class Reusable:
    def test(self):
        print(f"Using object {id(self)}")
```

##### ***Java version***

```java
package edu.def.op;

public class Reusable {
    public void test(){
        System.out.println("Using object " + System.identityHashCode(this));
    }
}
```

1. Not any notable differences.



### ***Controller***

##### ***Python version***

```python
class ReusablePool:

    def __init__(self, size):
        self.size = size
        self.free: List[Reusable] = []
        self.in_use: List[Reusable] = []
        for _ in range(0, size):
            self.free.append(Reusable())

    def acquire(self) -> Reusable:
        assert len(self.free) > 0
        r = self.free[0]
        self.free.remove(r)
        self.in_use.append(r)
        return r

    def release(self, r: Reusable):
        self.in_use.remove(r)
        self.free.append(r)
```

##### ***Java version***

```java
package edu.def.op;

import java.util.ArrayList;

public class ReusablePool {

    private int size;
    private ArrayList<Reusable> free;
    private ArrayList<Reusable> inUse;

    ReusablePool(int size){
        this.size = size;
        this.free = new ArrayList<>();
        this.inUse = new ArrayList<>();

        for (int i = 0; i < size; i++){
            this.free.add(new Reusable());
        }
    }

    public Reusable acquire(){
        assert this.free.size() > 0;
        Reusable r = this.free.get(0);
        this.free.remove(r);
        this.inUse.add(r);

        return r;
    }

    public void release(Reusable r){
        this.inUse.remove(r);
        this.free.add(r);
    }
}
```

1. In this class, we define all our parameters in the constructor. We just passed a value for ***size***; the two **ArrayLists** will be designated empty arrays. 
