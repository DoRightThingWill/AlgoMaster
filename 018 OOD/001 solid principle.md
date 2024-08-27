## single responsibility, in class level, not in method level

## close for modification

## open for extension

- do we have interface in python? how to present interface or abstract class in python?
- how to design a singleton in python, or in java.
- when you need singleton?

## liskov substituion principle

## interface segregation

## dependency inversion

- abstract does not reply on implementation
- implementation relies on abstract
- class reply on interface
- interface doet not reply on implemention. 1--> many relatonship

## Design an elevator

- For human being, or for cargo
- weight limit
- how many floors it can reach
- assumption: can request all elevator in each floor
- break down the requirement into smaller questions:
  - how to check if exceeds weight limit
  - how to decided which elevator to respond first if more than one are available
    - scheduler design
    - rule based: same direction --> none-moving-->counter direction
  - edge case: when the elevator is running, can it process the counter-direction request.

## 5C 解题法，电梯设计为例

- clarify requirement
- core object
  - 首先你会想到 elevator system
  - 对于这个整体的系统，what is the input and output. Input is the request, which has the source floor, and target floor. Output is an elevator, which will stop at the source floor
  - 接下来考虑，这个系统里面，会有哪些 children component。比如一个电梯系统，会有多个电梯
    - 一个 elevator system 有多个 elevator；类似的，一个 elevator，会有多个 button
    - access modifier
      - package level visible
      - private
      - public
      - protected: 出了被本身访问，还可以被子类进行访问，是实现继承的手段
- case

  - 反过来，再进行 review，设计的所有的 class，是不是可以 cover 全部的 requirement；

    - 或者说，每一个 class，他的 responsibility 是什么，比如 elevator system，接受 request，调度电梯；
    - 电梯，接受调度指令，执行 request
    - 同时，电梯还需要处理用户在电梯内发出的 request，比如按键，emergency；关门；weight check
    - unified model language，这样，可以更加准确的了解，整个系统的结构。其中一种，是 class diagtam
    - 类图，是对 class 特性、关系的形象化表示，比代码标识更加凝练

  - request 本身可以当做一个 interface
    - external request
    - internal request

## 三大特性

- polymorphism.
- 继承
  - abstract class，不能被 instantiate，不能使用 new
- 封装

## exception in Java

- checked exception，是 java 中特有的，指的是 compile time exception。比如 IOException，等等，如果一个方法 throw exception，那么调用这个方法，要么也 throw，要么就用 try catch block
- checked exception 和 handled exception 不是同一个概念。前者是 java 中特有的，后者，主要是指对 exception 的处理，如果用了 try catch 就是 handled，否则就是不 handled。handled exception 可以是 checked，也可以是 unchecked
