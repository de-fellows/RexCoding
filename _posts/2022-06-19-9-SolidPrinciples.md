---
toc: true
layout: post
description: Cmpletete traslation of Python code to Java.
categories: [Python, Java, OOP]
title: SOLID principles in Java
author: <a href="https://github.com/sinapordanesh”>Saman Pordanesh</a>
---

# **[SOLID principles](https://www.youtube.com/watch?v=pTB30aXS77U&feature=youtu.be) code translation in Java**

*Published by* [Saman Pordanesh](https://github.com/sinapordanesh)

## **Introduction** 

- SOLID is an acronym for the first five object-oriented design (OOD) principles.
These principles establish practices that lend to developing software with considerations for maintaining and extending as the project grows. Adopting these practices can also contribute to avoiding code smells, refactoring code, and Agile or Adaptive software development.
SOLID stands for:
S - Single-responsiblity Principle
O - Open-closed Principle
L - Liskov Substitution Principle
I - Interface Segregation Principle
D - Dependency Inversion Principle
- You need to watch the [video](https://www.youtube.com/watch?v=pTB30aXS77U&feature=youtu.be) first, understand all principles, and then look at the translation codes in Java. This documentation will help you to understand the translation better.
- This translation is based on the final code source of Solid Principles lessons in python programming languages (***dependency-inversion-after.py***)
- We need a separate class with the ***main*** function to run the program, despite Python, which you can each ***.py*** file individually. ***Main.java*** is the file with the main function for that purpose.
- Standard naming on java is different. You can find more information [here](https://www.oracle.com/java/technologies/javase/codeconventions-namingconventions.html).

## **Directories changes** 

- This is one of the most significant changes we made to our translation. A **Java** project with an exact directory with all dependencies can be good practice for OOP designing. 
- We defined a package name for this project as ***edu.def.solid*** ([package naming standards](https://docs.oracle.com/javase/tutorial/java/package/namingpkgs.html)) and its specific directory under the ***src*** folder. This package name keeps all project components connected to gather when we implement them on different ***.java*** files. 
- However, packages are not necessary, you could use a default package, or even have all classes in the same file; this is more Java best practice.
- More information about **Java’s** project directory standards is [here](https://www.ibm.com/docs/en/i/7.1?topic=topics-java-classes-packages-directories).

## **Compiling Instruction**

- Run the command prompt inside the ***src*** folder.
- Run the following command to compile all ***.java*** files:
```
javac edu/def/solid/*.java
```
- To execute the program, we should run the ***Main.java*** file from the command prompt. To do this, from the same directory, run the following command on the command prompt:
```
java edu.def.solid.Main
```
If your ***main*** function is in a different class, put the name of that class instead of ***Main*** at the end of the command
- You can find more about compiling instruction [here](https://docs.oracle.com/javase/7/docs/technotes/tools/windows/javac.html)

## **Classes changes** 

### ***Order***

##### ***Python version***
```python
class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total
```

##### ***Java version***

```java
package edu.def.solid;

public class Order {
    private String[] items;
    private int[] quantities;
    private int[] prices;
    private String status = "open";
    int numberOfItems = 0;

    Order(int numberOfItems){
        items = new String[numberOfItems];
        quantities = new int[numberOfItems];
        prices = new int[numberOfItems];
    }

    public void addItem(String name, int quantity, int price){
        this.items[numberOfItems] = name;
        this.quantities[numberOfItems] = quantity;
        this.prices[numberOfItems] = price;
        numberOfItems++;
    }

    public int totalPrice(){
        int total = 0;
        for (int i = 0; i < numberOfItems; i++){
            total += this.quantities[i] * this.prices[i];
        }
        return total;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getStatus() {
        return status;
    }
}
```

1. In this class, we need to clarify each array’s size as a Java programming rule. We can do it at the initializer by passing the number of items on the class constructor. 
1. We implemented all variables (items, quantities, …) as class attributes on Java with **private** visibility to protect them from direct access out of the class. Also, ***status*** has a default value of “*open*”.
1. A variable like ***numberOfItems*** is needed to keep track of the arrays and access them later, as Java doesn’t automatically detect where should add a new item in the array (nothing like append in python). In addition, we should keep updating this variable by adding every single item (in the ***addItem*** function).
1. **getters** and **setters** for each **private** parameter, are not required; You can access fields directly by making parameters **public** in Java as well, but it's (private parameters) frequently done in Java as an OOP principle. We followed that principle here and as we will need to access ***status*** in other classes, we defined getter and setter for this class’s parameter. 

### ***Authorizer***

##### ***Python version***
```python
class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass
```

##### ***Java version***
```java
package edu.def.solid;

public interface Authorizer {
    public boolean isAuthorized();
}
```

1. This class was an abstract class on the python version. Abstracts are usually used when we want to implement a specific function with all its functionalities that all children will use in the future. But when we need only the prototype (function naming, return type and arguments only), which will be implemented by each child later, we use [interfaces](https://www.w3schools.com/java/java_interface.asp) in Java programming.
As a result, we implement the ***Authorizer*** class as an [interface](https://www.w3schools.com/java/java_interface.asp) class containing the ***isAuthotized*** function prototype.

1. A class in Java can inherit an [interface](https://www.w3schools.com/java/java_interface.asp) by the “***implements***” keyword after the class name.

```java
public class AuthorizerSMS implements Authorizer{ ...
```

Also, all [interface](https://www.w3schools.com/java/java_interface.asp) methods should be overridden in this child class (implement them completely)

```java
@Override
    public boolean isAuthorized() {
        return this.authorized;
    }
```


### ***AuthorizerSMS***

##### ***Python version***
```python
class Authorizer_SMS(Authorizer):

    def __init__(self):
        self.authorized = False

    def verify_code(self, code):
        print(f"Verifying SMS code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized
```

##### ***Java version***
```java
package edu.def.solid;

public class AuthorizerSMS implements Authorizer{
    private boolean authorized = false;

    public void verifyCode(int code){
        System.out.print("Verifying SMS code " + code);
        this.authorized = true;
    }

    @Override
    public boolean isAuthorized() {
        return this.authorized;
    }

}
```


1. We defined the variable ***authorized*** as a private class attribute.
1. The ***isAuthorized*** method was **overridden** based on its [interface](https://www.w3schools.com/java/java_interface.asp), inheriting that ([***Authorizer***](#solid_class_authorizer)). 


1. At the ***verifyCode*** method, we appended the variable to the printed text by the “***+**”* sign, although in python, a formatting printing method was used (the ***f*** char at the start of the string)

### ***AuthorizerGoogle***

##### ***Python version***

```python
class Authorizer_Google(Authorizer):

    def __init__(self):
        self.authorized = False

    def verify_code(self, code):
        print(f"Verifying Google auth code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized
```

##### ***Java version***

```java
package edu.def.solid;

public class AuthorizerGoogle implements Authorizer {
    private boolean authorized = false;

    public void verifyCode(int code){
        System.out.print("Verifying Google code " + code);
        this.authorized = true;
    }

    @Override
    public boolean isAuthorized() {
        return this.authorized;
    }
}
```

The same points as [***AuthorizerSMS***](#solid_class_authorizersms)

### ***AuthorizerRobot***

##### ***Python version***
```python
class Authorizer_Robot(Authorizer):

    def __init__(self):
        self.authorized = False

    def not_a_robot(self):
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized
```

##### ***Java version***

```java
package edu.def.solid;

public class AuthorizerRobot implements Authorizer {
    private boolean authorized = false;

    public void notARobot(){
        this.authorized = true;
    }

    @Override
    public boolean isAuthorized() {
        return this.authorized;
    }
}
```


The same points as [***AuthorizerSMS***](#solid_class_authorizersms)

### ***PaymentProcessor***

##### ***Python version***
```python
class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass
```

##### ***Java version***

```java
package edu.def.solid;

public interface PaymentProcessor {
    public void pay(Order order) throws Exception;
}
```

1. this class is an [interface](https://www.w3schools.com/java/java_interface.asp) and acts the same as the [***Authorizer***](#solid_class_authorizer) class. This is an [interface](https://www.w3schools.com/java/java_interface.asp) which imposes the implementation of a specific method on each child, which will be inherent in this [interface](https://www.w3schools.com/java/java_interface.asp). 
1. In addition, be careful that the ***order*** argument in the payment method is in the type of [***Order***](#solid_class_order) class. (We call it [**non-primitive data type**](https://www.geeksforgeeks.org/data-types-in-java/))
1. We have an Exception method under a specific condition in the python. In Java, we must specify the “***throws Exception***” keyword on the function’s prototype and [interface](https://www.w3schools.com/java/java_interface.asp). 

### ***DebitPaymentProcessor***

##### ***Python version***

```python
class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code, authorizer: Authorizer):
        self.security_code = security_code
        self.authorizer = authorizer
    
    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"
```

##### ***Java version***

```java
package edu.def.solid;

public class DebitPaymentProcessor implements PaymentProcessor{
    private int securityCode;
    private Authorizer authorizer;

    DebitPaymentProcessor(int securityCode, Authorizer authorizer){
        this.securityCode = securityCode;
        this.authorizer = authorizer;
    }

    @Override
    public void pay(Order order) throws Exception {
        if (!authorizer.isAuthorized()){
            throw new Exception("Not authorized");
        }
        System.out.println("Processing debit payment type");
        System.out.println("Verifying security code: " + this.securityCode);
        order.setStatus("paid");
    }
}
```


1. We have a constructor to specify two-class parameter values, ***securitycode*** and ***authorizer***. Notice that authorizer is a [***non-primitive data type***](https://www.geeksforgeeks.org/data-types-in-java/) in the type of [***Authorizer***](#solid_class_authorizer). 
1. We specified all parameters as private because of the Java OOP rules and without getter and setter, as they are being used only for internal purposes.
1. The ***pay*** method is an overridden method from the [***PaymentProcessor***](#solid_class_paymentProcessor) [interface](https://www.w3schools.com/java/java_interface.asp). It shows us that this class inherits the [***PaymentProcessor***](#solid_class_paymentProcessor) [interface](https://www.w3schools.com/java/java_interface.asp).
1. The ***pay*** method in this class throws an exception, so we need “***throws Exception***” keyword at the method’s prototype.


### ***CreditPaymentProcessor***

##### ***Python version***
```python
class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"
```

##### ***Java version***

```java
package edu.def.solid;

public class CreditPaymentProcessor implements PaymentProcessor {
    private int securityCode;

    CreditPaymentProcessor(int securityCode){
        this.securityCode = securityCode;
    }

    @Override
    public void pay(Order order){
        System.out.println("Processing credit payment type");
        System.out.println("Verifying security code: " + this.securityCode);
        order.setStatus("paid");
    }
}
```

The same points of ***debitPaymentProcessor*** will apply for this class, except we don’t *have the **authorizer*** parameter and any exceptions for the ***pay*** method.

### ***PaypalPaymentProcessor***

##### ***Python version***

```python
class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address, authorizer: Authorizer):
        self.email_address = email_address
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"
```

##### ***Java version***

```java
package edu.def.solid;

public class PaypalPaymentProcessor implements PaymentProcessor{
    private String emailAddress;
    private Authorizer authorizer;

    PaypalPaymentProcessor(String emailAddress, Authorizer authorizer){
        this.emailAddress = emailAddress;
        this.authorizer = authorizer;
    }

    @Override
    public void pay(Order order) throws Exception {
        if (!authorizer.isAuthorized()){
            throw new Exception("Not authorized");
        }
        System.out.println("Processing paypal payment type");
        System.out.println("Using email address: " + this.emailAddress);
        order.setStatus("paid");
    }
}
```


The same points of ***debitPaymentProcessor*** will apply to this class. Only some changes about authentication and change from security code to email verification.
