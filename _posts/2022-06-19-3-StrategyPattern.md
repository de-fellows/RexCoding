---
toc: true
layout: post
description: Cmpletete traslation of Python code to Java.
categories: [Python, Java, OOP]
title: The Strategy Pattern in Java
author: <a href="https://github.com/sinapordanesh”>Saman Pordanesh</a>
---

# [The Strategy Pattern](https://www.youtube.com/watch?v=WQ8bNdxREHU) **code translation in Java** 

*Published by* [Saman Pordanesh](https://github.com/sinapordanesh)

## **General Introduction** 

- [**Strategy**](https://refactoring.guru/design-patterns/strategy) is a behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.
- You need to watch the [video](https://www.youtube.com/watch?v=WQ8bNdxREHU) first, understand all principles, and then look at the translation codes in Java. This documentation will help you to understand the translation better
- This translation is based on the final code source of **Strategy Pattern** lessons in python programming languages (***strategy-after.py***) 
**Point**: This part was done in two different (***oop*** & ***functional***) methods. This translation is based on the ***oop*** method, and we didn’t translate the ***functional*** one, as that method doesn’t work in ***Java*** very well, although in ***Python*** may work well.
- We need a separate class with the ***main*** function to run the program, despite **Python**, in which you can run each ***.py*** file individually. ***Main.java*** is the file with the main function for that purpose.
- Standard naming on java is different. You can find more information [here](https://www.oracle.com/java/technologies/javase/codeconventions-namingconventions.html).


## **Directories changes** 

- This is one of the most significant changes we made to our translation. A **Java** project by an exact directory with all dependencies can be a good practce OOP designing. 
- We defined a package name for this project as ***edu.def.sp*** ([package naming standards](https://docs.oracle.com/javase/tutorial/java/package/namingpkgs.html)) and its specific directory under the ***src*** folder. This package name keeps all project components connected to gather when we implement them on different ***.java*** files. 
- However, packages are not necessary, you could use a default package, or even have all classes in the same file; this is more Java best practice.
- More information about **Java’s** project directory standards is [here](https://www.ibm.com/docs/en/i/7.1?topic=topics-java-classes-packages-directories).

## **Implementational Instruction**

1. We will create one .java file per class under ***edu.def.sp*** package.
1. As we have different ordering methods, we’ll define one class per each ordering way. They all inherit an [interface](https://www.w3schools.com/java/java_interface.asp) (***TicketOrderingStrategy.java***) that contains only one ordering method (***createOrdering.java***).
1. As mentioned, one class for each ordering method is needed, which will be: 
***FIFOOrderingStrategy.java – FILOOrderingStrategy.java - RandomOrderingStrategy.java – BlackHoleStrategy.java***

1. When creating other classes (***SuportTicket.java*** & ***CustomSupport.java***), we need ***Main.java*** to contain our main function to run the program.
1. After that, we will translate all classes to their belonging files based on the **Python** source. We will compare them with the original version in the following section.

## **Compiling Instruction**

- Run the command prompt inside the ***src*** folder.
- Run the following command to compile all ***.java*** files:
```
javac edu/def/sp/*.java
```
- To execute the program, we should run the ***Main.java*** file from the command prompt. To do this, from the same directory, run the following command on the command prompt:
```
java edu.def.sp.Main
```
If your ***main*** function is in a different class, put the name of that class instead of ***Main*** at the end of the command
- You can find more about compiling instruction [here](https://docs.oracle.com/javase/7/docs/technotes/tools/windows/javac.html)

## **Classes changes** 

### ***SupportTicket***


##### ***Python version*** 

```python
class SupportTicket:

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue

def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))

``` 

##### ***Java version***

```java
package edu.def.sp;

import java.util.Random;

public class SupportTicket {
    private String id;
    private String customer;
    private String issue;

    SupportTicket(String customer, String issue){
        this.id = getSaltString("uppercase", 8);
        this.customer = customer;
        this.issue = issue;
    }

    public String getId() {
        return id;
    }

    public String getCustomer() {
        return customer;
    }

    public String getIssue() {
        return issue;
    }

    /**
     * As we dont have a simple function to arrange a random string on Java, we are implementing
     * this helper method to help us create one.
     * It acts like "random.choices" in Python
     * @param ascii
     * @return
     */
    private String getSaltString(String ascii, int length) {

        //char sets based on the incoming argument
        String SALTCHARS;

        switch (ascii){
            case "uppercase":
                SALTCHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
                break;
            case "lowercase":
                SALTCHARS = "abcdefghijklmnopqrstuvwxyz";
                break;
            case "digits":
                SALTCHARS = "1234567890";
                break;
            default:
                SALTCHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890";
        }
        StringBuilder salt = new StringBuilder();
        Random rnd = new Random();
        while (salt.length() < length) { // length of the random string.
            int index = (int) (rnd.nextFloat() * SALTCHARS.length());
            salt.append(SALTCHARS.charAt(index));
        }
        return salt.toString();
    }
}
```

1. This is a class for creating tickets with three parameters ***id***, ***customer***, ***issue***, and three ***getters*** for each parameter. As we are defining the parameter values on the constructor and won’t need to change them separately later, we don’t have a ***setter*** method for any parameter. Aslo, we can access parameters directly by making them **public**, but we use **private** parameters as an OOP designing principle.
1. The constructor received two arguments for ***customer*** and ***issue***, but ***Id*** will be valued by generating a random string generator.
1. The only private method used to generate a random string with a specified size (we need to define this function as we don’t have any predefined method to do that in **Java**, although **Python** has). 

### ***TicketOrderingStrategy***

##### ***Python version*** 

```python
class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        pass
``` 

##### ***Java version*** 

```java
package edu.def.sp;

import java.util.ArrayList;

public interface TicketOrderingStrategy {

    /**
     * A function which receives a list and return another list based on the ordering type.
     * @param list: an argument of ArrayList data type which contains SupportTicket objects
     * @return: the same data type of incoming argument, but with different ordering
     */
    public ArrayList<SupportTicket> createOrdering(ArrayList<SupportTicket> list);
}
```

1. This is the [interface](https://www.w3schools.com/java/java_interface.asp) we discussed at instruction, which all other ordering classes will inherit. We will override this [interface](https://www.w3schools.com/java/java_interface.asp)'s ***createOrdering()*** method in all those classes. 
1. As we can see, the ***creatingOrdering()*** method’s prototype defines which arguments are needed for this method and what will be its return value data type.    

### ***FIFOOrderingStrategy***

##### ***Python version*** 

```python
class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return list.copy()
``` 

##### ***Java version*** 

```java
package edu.def.sp;

import java.util.ArrayList;

public class FIFOOrderingStrategy implements TicketOrderingStrategy{

    @Override
    public ArrayList<SupportTicket> createOrdering(ArrayList<SupportTicket> list) {
        return (ArrayList<SupportTicket>) list.clone();
    }
}

```

1. This class is one of the ordering ways classes implemented(inherited) from the ***TicketSupportingStrategy*** [interface](https://www.w3schools.com/java/java_interface.asp).
1. We have overridden the [interface](https://www.w3schools.com/java/java_interface.asp)’s method as our desire for this class of ordering. 
1. The list is already in order in this ordering method (*first in, first out*) der. You need to return it by creating a copy through the [clone](https://www.geeksforgeeks.org/clone-method-in-java-2/) method. 
1. [Clone](https://www.geeksforgeeks.org/clone-method-in-java-2/): ***clone()*** is a method to deeply copy an object in ***Java*** programming languages. When we use the “**=**” sign to copy an object, we are putting the address of the *source* (***obj1***) object to the *destination* (***obj2***); this means that if we change the ***boj1***’s value, ***obj2***’s value will be adjusted consequently. But with the ***clone()*** method, we can create an independent copy of **obj1** and assign it to the ***obj2***, although still, we can do more about making a completely separate copy, which is out of the scope of this article. Please click [here](https://www.baeldung.com/java-deep-copy) for more.



### ***FILOOrderingStrategy*** 

##### ***Python version*** 

```python
class FILOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy
```

##### ***Java version*** 

```java
package edu.def.sp;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;

public class FILOOrderingStrategy implements TicketOrderingStrategy{

    @Override
    public ArrayList<SupportTicket> createOrdering(ArrayList<SupportTicket> list) {
        //clone() reates a partial deep copy of the object
        ArrayList<SupportTicket> listCopy = (ArrayList<SupportTicket>) list.clone();
        //a function to reverse an ArrayList
        Collections.reverse(listCopy);
        return listCopy;
    }
}
```

Most of the **FIFOOrderingStrategy**’s points are applicable here**.**

1. In this ordering class, after making a copy of the ***list*** by [clone](https://www.geeksforgeeks.org/clone-method-in-java-2/), we should **reverse** the list because of our ordering way (*first in, last out*). We did it using the [***Collection***](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html) class and its method **reverse()**, which reversed the list and returned it.

### ***RandomOrderingStrategy***

##### ***Python version*** 

```python
class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy
``` 

##### ***Java version*** 

```java
package edu.def.sp;

import java.util.ArrayList;
import java.util.Collections;

public class RandomOrderingStrategy implements TicketOrderingStrategy{

    @Override
    public ArrayList<SupportTicket> createOrdering(ArrayList<SupportTicket> list) {
        ArrayList<SupportTicket> listCopy = (ArrayList<SupportTicket>) list.clone();
        //shuffle the list randomly
        Collections.shuffle(listCopy);
        return listCopy;
    }
}
```

Most of the ***FIFOOrderingStrategy***’s points are applicable here.

1. In this ordering class, after making a copy of the ***list*** by [clone](https://www.geeksforgeeks.org/clone-method-in-java-2/), we should **shuffle** the list because of our ordering way (*random*). 
We did it using a class called [***Collection***](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html) and its method **shuffle()**, which shuffled the list and returned it.

### ***BlackHoleStrategy***

##### ***Python version*** 

```python
class BlackHoleStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return []
```

##### ***Java version*** 

```java
package edu.def.sp;

import java.util.ArrayList;

public class BlackHoleStrategy implements TicketOrderingStrategy{
    @Override
    public ArrayList<SupportTicket> createOrdering(ArrayList<SupportTicket> list) {
        //just return an empty ArrayList
        return new ArrayList<>();
    }
}
```

Most of the ***FIFOOrderingStrategy***’s points are applicable here.

1. This class returns an empty ***ArrayList<>()*** when we’ll need it for any reason. 

### ***CustomerSupport***

##### ***Python version*** 

```python
class CustomerSupport:

    def __init__(self, processing_strategy: TicketOrderingStrategy):
        self.tickets = []
        self.processing_strategy = processing_strategy

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self):
        # create the ordered list
        ticket_list = self.processing_strategy.create_ordering(self.tickets)

        # if it's empty, don't do anything
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        # go through the tickets in the list
        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")
``` 

##### ***Java version*** 

```java
package edu.def.sp;

import java.util.ArrayList;

public class CustomerSupport {

    private ArrayList<SupportTicket> tickets;
    private TicketOrderingStrategy processingStrategy;

    CustomerSupport(TicketOrderingStrategy processingStrategy){
        tickets = new ArrayList<>();
        this.processingStrategy = processingStrategy;
    }


    public void createTicket(String customer, String issue){
        tickets.add(new SupportTicket(customer, issue));
    }


    public void processTickets(){
        ArrayList<SupportTicket> ticketList = this.processingStrategy.createOrdering(this.tickets);

        if (ticketList.size() == 0){
            System.out.println("There are no tickets to process. Well done!");
            return;
        }

        for (SupportTicket ticket: ticketList){
            this.processTicket(ticket);
        }
    }

    /**
     * As it has only internal usage, we can define this function as a private one.
     * @param ticket
     */
    private void processTicket(SupportTicket ticket){
        System.out.println("==================================");
        System.out.println("Processing ticket id: " + ticket.getId());
        System.out.println("Customer: " + ticket.getCustomer());
        System.out.println("Issue: " + ticket.getIssue());
        System.out.println("==================================");
    }
}
```

1. This class is the heart of the application; create customers ***ArrayList***, add tickets to it, process tickets and show them to the user by any request. 
1. We have two private parameters whose value will be assigned to them in the class’s constructor.
1. In the constructor, we pass an object of the ***TicketOrderingStrategy*** interface, which is a non-primitive data type. This object will define the ordering in this class. Also, we are creating a new ***ArrayList*** object in this constructor.
1. In the ***createTickets ()*** public method, we create a ***SupportTicket*** object and add it to the ***tickets*** *ArrayList*.
1. In the ***proccessTicket()*** method, we are ordering the ticket ***ArrayList*** by passing this list to the ***processingStrategy*** object’s method (**createOrdering()**). This will return the desired ordered list, and the ***ticket*** - ***ArrayList*** will be replaced. Then, we will start to print each list entry by passing them to the ***processTicket()*** method. 
