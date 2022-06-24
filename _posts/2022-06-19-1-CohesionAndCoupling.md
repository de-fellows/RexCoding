---
toc: true
layout: post
description: Cmpletete traslation of Python code to Java.
categories: [Python, Java, OOP]
title: Cohesion and Coupling in Java
author: <a href="https://github.com/sinapordanesh”>Saman Pordanesh</a>
---

# [Cohesion and Coupling](https://www.youtube.com/watch?v=eiDyK_ofPPM) **principles code translation in Java**

*Published by* [Saman Pordanesh](https://github.com/sinapordanesh)

## **Introduction** 

- **Cohesion** is used to indicate the degree to which a class has a single, well-focused purpose. **Coupling** is all about how classes interact with each other; on the other hand, cohesion focuses on how the single class is designed. Higher the cohesiveness of the class, the better is the OO design.
Benefits of Higher Cohesion:
    - Highly cohesive classes are much easier to maintain and less frequently changed.
    - Such classes are more usable than others as they are designed with a well-focused purpose.
- You need to watch the [video](https://www.youtube.com/watch?v=eiDyK_ofPPM) first, understand all principles, and then look at the translation codes in Java. This documentation will help you to understand the translation better
- This translation is based on the final code source of Cohesion and Coupling lessons in python programming languages (***coupling-cohesion-after.py***)
- We need a separate class with the ***main*** function to run the program, despite Python, in which you can run each ***.py*** file individually. ***Main.java*** is the file with the main function for that purpose.
- Standard naming on java is different. You can find more information [here](https://www.oracle.com/java/technologies/javase/codeconventions-namingconventions.html).

## **Directories changes** 

- This is one of the most significant changes we made to our translation. A **Java** project with an exact directory with all dependencies can be good practice for OOP designing. 
- We defined a package name for this project as ***edu.def.cac*** ([package naming standards](https://docs.oracle.com/javase/tutorial/java/package/namingpkgs.html)) and its specific directory under the ***src*** folder. This package name keeps all project components connected to gather when we implement them on different ***.java*** files. 
- However, packages are not necessary, you could use a default package, or even have all classes in the same file; this is more Java best practice.
- More information about **Java’s** project directory standards is [here](https://www.ibm.com/docs/en/i/7.1?topic=topics-java-classes-packages-directories).

## **Compiling Instruction**

- Run the command prompt inside the ***src*** folder.
- Run the following command to compile all ***.java*** files:
```
javac edu/def/cac/*.java
```
- To execute the program, we should run the ***Main.java*** file from the command prompt. To do this, from the same directory, run the following command on the command prompt:
```
java edu.def.cac.Main
```
If your ***main*** function is in a different class, put the name of that class instead of ***Main*** at the end of the command
- You can find more about compiling instruction [here](https://docs.oracle.com/javase/7/docs/technotes/tools/windows/javac.html)

## **Classes changes** 

### ***VehicleInfo***

##### **Python version**

```python
class VehicleInfo:
    
    def __init__(self, brand, electric, catalogue_price):
        self.brand = brand
        self.electric = electric
        self.catalogue_price = catalogue_price

    def compute_tax(self):
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02
        return tax_percentage * self.catalogue_price

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Payable tax: {self.compute_tax()}")
```

##### **Java version** 

```java
package edu.def.cac;

/**
 * A class with 3 private parameters and two public
 * methods. Also, a constructor with 3 arguments.
 */
public class VehicleInfo {
    private String brand;
    private boolean electric;
    private int cataloguePrice;

    VehicleInfo(String brand, boolean electric, int cataloguePrice){
        this.brand = brand;
        this.electric = electric;
        this.cataloguePrice = cataloguePrice;
    }

    /**
     *
     * @return a double which is the computed tax.
     */
    public double computeTax(){
        double taxPercentage = 0.05;
        if (electric){
            taxPercentage = 0.02;
        }
        return taxPercentage * cataloguePrice;
    }

    /**
     *
     */
    public void print(){
        System.out.println("Brand: " + this.brand);
        System.out.println("Payable tax: " + this.computeTax());
    }
}
```

1. we defined three private parameters in this class, and their values will be determined by the class instructor when we initialize the class. **getters** and **setters** for each **private** parameter, are not required, you can access fields directly by making parameters **public** in Java as well, but it's (private parameters) frequently done in Java as an OOP principle. Still, as we won’t need direct access to any parameters in future, we do not implement them here (it’s acceptable). 
1. Be careful that we specify all data types when we initialize them, although it’s unnecessary for python. 
1. We can add strings together for printing by the “***+***” sign, although we used formatted string to do that on python.

### ***Vehicle***

##### **Python version**

```python
class Vehicle:

    def __init__(self, id, license_plate, info):
        self.id = id
        self.license_plate = license_plate
        self.info = info

    def print(self):
        print(f"Id: {self.id}")
        print(f"License plate: {self.license_plate}")
        self.info.print()
```

##### **Java version** 

```java
package edu.def.cac;

/**
 * Public class Vehicle with 3 private parameters
 * and one public method. Plus a constructor with
 * 3 arguments.
 */
public class Vehicle {
    private String id;
    private String licensePlate;
    private VehicleInfo info;

    Vehicle(String id, String licensePlate, VehicleInfo info){
        this.id = id;
        this.licensePlate = licensePlate;
        this.info = info;
    }

    public void print(){
        System.out.println("Id: " + this.id);
        System.out.println("License plate: " + this.licensePlate);
        this.info.print();
    }
}
```


1. A simple class which has three parameters. As we explained in the previous class, we defined all of them as “*private*” without any getter and setter. 
1. The same point about joining strings together for printing in the ***print*** function. 


### ***VehicleRegistry***

##### **Python version**

```python
class VehicleRegistry:

    def __init__(self):
        self.vehicle_info = { }
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("Volkswagen ID3", True, 35000)
        self.add_vehicle_info("BMW 5", False, 45000)
        self.add_vehicle_info("Tesla Model Y", True, 75000)

    def add_vehicle_info(self, brand, electric, catalogue_price):
        self.vehicle_info[brand] = VehicleInfo(brand, electric, catalogue_price)

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand):
        id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(id)
        return Vehicle(id, license_plate, self.vehicle_info[brand])
```

##### **Java version** 

```java
package edu.def.cac;

import java.util.HashMap;
import java.util.Random;

public class VehicleRegistry {

    /**
     * We use HashMap in java when we want to have a data structure as shows Key -> Value
     * here, the key is the car's brand and its is a VehicleInfo object
     */
    HashMap<String, VehicleInfo> vehicleInfo = new HashMap<>();

    VehicleRegistry(){
        //Saturating the HashMap on constructor
        this.addVehicleInfo("Tesla Model 3", true, 60000);
        this.addVehicleInfo("Volkswagen ID3", true, 35000);
        this.addVehicleInfo("BMW 5", false, 45000);
        this.addVehicleInfo("Tesla Model Y", true, 75000);
    }

    public void addVehicleInfo(String brand, boolean electric, int cataloguePrice){
        /*create an entry for the HashMap which the Key is String type and the Vale is a
        non-primary data type VehicleInfo
         */
        this.vehicleInfo.put(brand, new VehicleInfo(brand, electric, cataloguePrice));
    }

    public String generateVehicleId(int length){
        return getSaltString("uppercase", length);
    }

    public String generateVehicleLicense(String id){
        return id.substring(0, 2) + "-" + getSaltString("digits", 2) + "-" + getSaltString("uppercase", 2);
    }

    public Vehicle createVehicle(String brand){
        String id = generateVehicleId(12);
        String licensePlate = generateVehicleLicense(id);
        return new Vehicle(id, licensePlate, vehicleInfo.get(brand));
    }

    /**
     * As we dont have a simple function to arrange a random string on Java, we are implementing
     * this helper method to help us create one.
     * It acts like "random.choices" in Python
     * @param ascii
     * @return
     */
    protected String getSaltString(String ascii, int length) {

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

1. In this class, we are using ***vehicleInfo*** [HashMap](https://www.w3schools.com/java/java_hashmap.asp) as an alternative data structure for [Python’s dictionary](https://www.w3schools.com/python/python_dictionaries.asp). [HashMap](https://www.w3schools.com/java/java_hashmap.asp) is a data structure which allows us to define a key for a specific value and get access to that value with the key in future (*key -> value*). In this class, we use a car’s brand as a key and attach it to belonging vehicle information (value). As a result, we will be able to access each car’s brand information through *key -> value*. In addition, this parameter is a private one.
1. `  `We initialized ***vehicleInfo*** with some data at the class construction ***VehicleRegistry**.* This isn’t a good and professional way to saturate a hash map, but it works in this example just for educational purposes. 
1. The function ***addVehicleInfo*** is for adding new data to the ***vehicleInfo*** [HashMap](https://www.w3schools.com/java/java_hashmap.asp) by getting three arguments. The first argument will be the key on the [HashMap](https://www.w3schools.com/java/java_hashmap.asp), and the others will be used to initialize an object from VehicleInfo class.  As you can see, ***vehicleInfo.put(key, value)*** is a function to add an entry to the HashMap. 
1. At the function ***generateVicleId,*** we see a significant difference between the Java version and the Python one. We need to define the ***getSaltString*** [helper method](https://teamtreehouse.com/community/what-exactly-is-a-helper-method) to generate random strings based on the three categories of ASCII characters (*uppercase, lowercase, digits*). However, we already have a predefined function to do this in Python. 
In this function, we need to return a random string of uppercase characters with the size of ***length***, which is the function’s argument. 

1. At ***generateVehicleLicense,*** we create a specific string format. By the [substring()](https://www.w3schools.com/jsref/jsref_substring.asp) method, we can split a particular part of a string. It’s identical to Python’s ***string[start, end] method***.
1. As we said before, ***getSaltString*** is a [helper method](https://teamtreehouse.com/community/what-exactly-is-a-helper-method) to generate random strings based on specific size and type. You can find more [here](https://stackoverflow.com/questions/20536566/creating-a-random-string-with-a-z-and-0-9-in-java).

### ***Application*** 

##### **Python version**

```python
class Application:

    def register_vehicle(self, brand: string):
        # create a registry instance
        registry = VehicleRegistry()

        vehicle = registry.create_vehicle(brand)

        # print out the vehicle information
        vehicle.print()
```

##### **Java version** 

```java
package edu.def.cac;

public class Application {
    /**
     * to put all different components togather and create an application for a specific brand of car.
     * @param brand: main input to create an application.
     */
    public void registerVehicle(String brand){
        VehicleRegistry registry = new VehicleRegistry();
        Vehicle vehicle = registry.createVehicle(brand);
        vehicle.print();
    }
}
```


1. This class, with a simple public function, is created to put all other classes and their method together to lunch an application. The only argument that the ***registerVehicle*** method needs is a car’s brand string.
