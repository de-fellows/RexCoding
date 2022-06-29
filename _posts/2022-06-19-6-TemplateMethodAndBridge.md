---
toc: true
layout: post
description: Complete translation of Python code to Java
categories: [Python, Java, OOP]
title: Template Method & Bridge in Java
author: <a href="https://github.com/sinapordanesh”>Saman Pordanesh</a>
---

# [Template Method & Bridge](https://www.youtube.com/watch?v=t0mCrXHsLbI) **code translation in Java** 

*Published by* [Saman Pordanesh](https://github.com/sinapordanesh)

## **General Introduction** 

- The [Template Method](https://www.geeksforgeeks.org/template-method-design-pattern/) design pattern is to define an algorithm as a skeleton of operations and leave the details to be implemented by the child classes. The parent class preserves the overall structure and sequence of the algorithm.
Also, In computer science, [bridging](https://en.wikipedia.org/wiki/Bridging_\(programming\)#:~:text=In%20computer%20science%2C%20bridging%20describes,two%20sides%20of%20the%20bridge.) describes systems that map the runtime behaviour of different programming languages so they can share common resources.
- You need to watch the [video](https://www.youtube.com/watch?v=t0mCrXHsLbI) first, understand all principles, and then look at the translation codes in **Java**. This documentation will help you to understand the translation better
- This translation is based on the final code source of the **Template method and Bridge** lessons in python programming languages (***with-bridge.py***). That is the complete file, which contains all principles such as Abstraction, Inheritance, etc.
- We need a separate class with the ***main*** function to run the program, despite **Python**, in which you can run each ***.py*** file individually. ***Main.java*** is the file with the main function for that purpose.
- Standard naming on **Java** is different. You can find more information [here](https://www.oracle.com/java/technologies/javase/codeconventions-namingconventions.html).
- There is a ***UML.png*** file in this repository’s folder, which shows relationships between different classes. Please check it as a good reference for understanding this code. 

## **Directories changes** 

- This is one of the most significant changes we made to our translation. A **Java** project with the same directory with all dependencies can be good practice for OOP designing.
- We defined a package name for this project as ***edu.def.tmab*** ([package naming standards](https://docs.oracle.com/javase/tutorial/java/package/namingpkgs.html)) and its specific directory under the ***src*** folder. This package name keeps all project components connected to gather when we implement them on different ***.java*** files. 
- However, packages are unnecessary; you could use a default package or even have all classes in the same file; this is more **Java** best practice.
- More information about **Java’s** project directory standards is [here](https://www.ibm.com/docs/en/i/7.1?topic=topics-java-classes-packages-directories).

## **Implementational Instruction**

1. We will create one ***.java*** file per class under ***edu.def.tmab*** package.
They can be interfaces, abstractions, child classes or simple classes.
1. After that, we will translate all classes to their belonging files based on the **Python** source. We will compare them with the original version in the following section.
1. This article will introduce the [Abstract](https://www.w3schools.com/java/java_abstract.asp#:~:text=Abstract%20class%3A%20is%20a%20restricted,the%20subclass%20\(inherited%20from\).) class and method. The [abstract](https://www.w3schools.com/java/java_abstract.asp#:~:text=Abstract%20class%3A%20is%20a%20restricted,the%20subclass%20\(inherited%20from\).) is a kind of parent class with both methods and parameters. Methods can be in two different categories; [Abstract methods](https://www.w3schools.com/java/java_abstract.asp#:~:text=Abstract%20class%3A%20is%20a%20restricted,the%20subclass%20\(inherited%20from\).)  are those that we implement in the abstract class, and all children will inherit them the same as the parent. The other kind of method is just a prototype that shows the return type, name and arguments needed. Still, we will implement the content of the method on each child individually using the ***override*** keyword. We implement an [abstract](https://www.w3schools.com/java/java_abstract.asp#:~:text=Abstract%20class%3A%20is%20a%20restricted,the%20subclass%20\(inherited%20from\).) class by using the “***abstract***” keyword at the start of the class definition. 
1. ***Main.java*** contains our ***main()*** method to run the program.
1. Note that all steps here are entirely for the best OOP practice in Java programming; They can be done more straightforwardly, but not the best OOP ways.  

## **Compiling Instruction**

- Run the command prompt inside the ***src*** folder.
- Run the following command to compile all .java files:
```
javac edu/def/tmab/*.java
```
- To execute the program, we should run the Main.java file from the command prompt. To do this, from the same directory, run the following command on the command prompt:
```
java edu.def.tmab.Main
```
- If your main function is in a different class, but the name of that class instead of Main at the end of the command
- You can find more about compiling instructions [here](https://docs.oracle.com/javase/7/docs/technotes/tools/windows/javac.html).

## **Classes changes** 

### ***Exchange***

##### ***Python version***

```python
class Exchange(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_market_data(self, coin: str) -> List[float]:
        pass
```

##### ***Java version***

```java
package edu.def.tmab;

import java.util.ArrayList;

public interface Exchange {

    public void connect();
    public ArrayList<Float> getMarketData(String coin);
}
```

1. This class is defined as an [interface](https://www.w3schools.com/java/java_interface.asp) class, although it was described as an [abstract](https://www.w3schools.com/java/java_abstract.asp) one on the **Python** version. The reason is that we don’t have an [interface](https://www.w3schools.com/java/java_interface.asp) class specifically on Python programming languages. Please read about the [differences between interface and abstract class](https://www.guru99.com/interface-vs-abstract-class-java.html#:~:text=An%20interface%20is%20abstract%20so,code%20which%20should%20be%20overridden.&text=You%20cannot%20use%20access%20modifiers%20for%20the%20method%2C%20properties%2C%20etc.).
1. In this class, we define the prototype of each method that a child will inherit. Then, we will override it at the child class later. 

### ***Binance***

##### ***Python version***

```python
class Binance(Exchange):
    def connect(self):
        print(f"Connecting to Binance exchange...")

    def get_market_data(self, coin: str) -> List[float]:
        return [10, 12, 18, 14]
```

##### ***Java version***

```java
package edu.def.tmab;

import java.util.ArrayList;

public class Binance implements Exchange{

    @Override
    public void connect() {
        System.out.println("Connecting to Binance exchange...");
    }
    @Override
    public ArrayList<Float> getMarketData(String coin) {
        return new ArrayList<>(){{
            add(10f);
            add(12f);
            add(18f);
            add(14f);
        }};
    }
}
```

1. This is a child class which inherits the interface ***Exchange***. As you can see, we override both interface methods in this class. Also, we don’t have any limitations to adding more parameters and methods in this class beyond the inherited interface.  
1. In the ***getMarketData()*** method, we initialized the ***ArrayList*** by some numbers differently from **Python**. This is the proper way to do that In **Java**. You can find more [here](https://www.geeksforgeeks.org/initialize-an-arraylist-in-java/). (“**f**” in front of each number means “***float***” data type)

### ***Coinbase***

##### ***Python version***

```python
class Coinbase(Exchange):
    def connect(self):
        print(f"Connecting to Coinbase exchange...")

    def get_market_data(self, coin: str) -> List[float]:
        return [10, 12, 18, 20]
```

##### ***Java version***

```java
package edu.def.tmab;

import java.util.ArrayList;

public class Coinbase implements Exchange{
    @Override
    public void connect() {
        System.out.println("Connecting to Binance exchange...");
    }
    @Override
    public ArrayList<Float> getMarketData(String coin) {
        return new ArrayList<>(){{
            add(10f);
            add(12f);
            add(18f);
            add(14f);
        }};
    }
}
```

The same point as the ***Binance*** class. 

### ***TradingBot***

##### ***Python version***

```python
class TradingBot(ABC):

    def __init__(self, exchange: Exchange):
        self.exchange = exchange

    def check_prices(self, coin: str):
        self.exchange.connect()
        prices = self.exchange.get_market_data(coin)
        should_buy = self.should_buy(prices)
        should_sell = self.should_sell(prices)
        if should_buy:
            print(f"You should buy {coin}!")
        elif should_sell:
            print(f"You should sell {coin}!")
        else:
            print(f"No action needed for {coin}.")

    @abstractmethod
    def should_buy(self, prices: List[float]) -> bool:
        pass

    @abstractmethod
    def should_sell(self, prices: List[float]) -> bool:
        pass
```

##### ***Java version***

```java
package edu.def.tmab;

import java.util.ArrayList;

public abstract class TradingBot {
    private Exchange exchange;

    TradingBot(Exchange exchange){
        this.exchange = exchange;
    }

    public void checkPrices(String coin){
        this.exchange.connect();
        ArrayList<Float> prices = this.exchange.getMarketData(coin);

        boolean shouldBuy = this.shouldBuy(prices);
        boolean shouldSell = this.shouldSell(prices);

        if (shouldBuy){
            System.out.println("You should buy " + coin + "!");
        } else if (shouldSell) {
            System.out.println("You should sell " + coin + "!");
        } else {
            System.out.println("No action needed for " + coin + ".");
        }
    }

    public abstract boolean shouldBuy(ArrayList<Float> prices);

    public abstract boolean shouldSell(ArrayList<Float> prices);
}
```

1. This class is an [Abstract](https://www.w3schools.com/java/java_abstract.asp) class, as we discussed at *Implementation Instruction*. You can see the “***abstract***” keyword in the class implementation, which is necessary for implementation. 
1. As you can see, we have both implemented method and [**abstract method**](https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html) (only prototype) methods in this class. We will override all [**abstract methods**](https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html) for the children who will inherit from. In terms of the implemented method, all children will inherit them precisely with the same functionality we defined for the method in the abstraction class. We won’t override them later.
1. ***checkPrices()*** is a *local method*, but ***shouldBuy()*** and ***shouldSell()*** are [abstract methods](https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html). 
1. As we said before, an abstract class acts like a regular class and can have *local methods*, *parameters*, *a* *constructor*, and [abstract methods](https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html). 

### ***AverageTrader***

##### ***Python version***

```python
class AverageTrader(TradingBot):
    def list_average(self, l: List[float]) -> float:
        return sum(l) / len(l)

    def should_buy(self, prices: List[float]) -> bool:
        return prices[-1] < self.list_average(prices)

    def should_sell(self, prices: List[float]) -> bool:
        return prices[-1] > self.list_average(prices)
```

##### ***Java version***

```java
package edu.def.tmab;

import java.util.ArrayList;

public class AverageTrader extends TradingBot{

    /**
     * in java, when a class inherits an abstraction parent, we should have the constructor for the parent on the child class as well. The keyword for it is "super".
     * @param exchange
     */
    AverageTrader(Exchange exchange) {
        super(exchange);
    }

    public float listAverage(ArrayList<Float> list){

        //we don't have any function to calculate sum of the
        // item on a list automatically.
        float sum = 0;
        for (float item: list){
            sum += item;
        }
        return sum/list.size();
    }

    @Override
    public boolean shouldBuy(ArrayList<Float> prices) {
        // "(prices.size() - 1)" on get() method means getting the last item of the list.
        return prices.get(prices.size() - 1) < this.listAverage(prices);
    }

    @Override
    public boolean shouldSell(ArrayList<Float> prices) {
        // "(prices.size() - 1)" on get() method means getting the last item of the list.
        return prices.get(prices.size() - 1) > this.listAverage(prices);
    }
}
```

1. This child inherits the ***TradingBot*** abstraction class through the “***extends***” keyword.
1. The critical point is that we should first feed the parent’s constructor from this class’s constructor. It can be done by a ***super()*** method which takes arguments if the parent’s constructor needs any.  You can find out more [here](https://stackoverflow.com/questions/10508107/why-call-super-in-a-constructor). Also, we can initialize more parameters in this constructor if the class has any local ones. 
1. As it is clear, we have two overridden methods, ***shouldBuy()*** and ***shouldSell()*** , which are [abstract methods](https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html) that belong to the abstract parent. In addition, we have a local method ***listAverage()*** .

### ***MinMaxTrader***

##### ***Python version***

```python
class MinMaxTrader(TradingBot):

    def should_buy(self, prices: List[float]) -> bool:
        return prices[-1] == min(prices)

    def should_sell(self, prices: List[float]) -> bool:
        return prices[-1] == max(prices)
```

##### ***Java version***

```java
package edu.def.tmab;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Objects;

public class MinMaxTrader extends TradingBot{

    /**
     * in java, when a class inherits an abstraction parent, we should have the constructor for the parent on the child class as well. The keyword for it is "super".
     * @param exchange
     */
    MinMaxTrader(Exchange exchange) {
        super(exchange);
    }

    @Override
    public boolean shouldBuy(ArrayList<Float> prices) {
        // "(prices.size() - 1)" on get() method means getting the last item of the list.
        //Also, Collections.min() will find the maximum item in a list
        return Objects.equals(prices.get(prices.size() - 1), Collections.min(prices));
    }

    @Override
    public boolean shouldSell(ArrayList<Float> prices) {
        // "(prices.size() - 1)" on get() method means getting the last item of the list.
        //Also, Collections.max() will find the maximum item in a list.
        return prices.get(prices.size() - 1) == Collections.max(prices);
    }
}
```

The same points as ***AverageTrader*** class. 
