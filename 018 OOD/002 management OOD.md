## 通常包括以下几种类型

- parking lot
- restaraunt
- library
- super market
- hotel

他们通常都是要对某一个流程，进行管理

## OOD，应该这么分析

- 有哪些主题参与其中
- 有哪些场景，将这些主体联系起来
- 面试官可能不会告诉你，这是 OOD 的面试，但是，一旦你察觉到了这是 OOD，你可以和面试官进行交流，但是，倾向于，对所有的主体，都要构建 class

## Parking lot 设计

- parking lot
  - levels: List\<Level>
  - Ticket parkVehicle(Vehicle vehicle)
  - Ticket checkout(Tiket ticket)
- level：有点动态数据
  - id
  - availableSpots: List\<Spot>
- parking spot：静态数据
  - ID
  - size
  - isTaken
- vehicle：静态数据
  - ID
  - szie: enum, S, M, L
- ticket: 这里面，存动态数据
  - ID
  - createdAt:
  - leftAt:
  - rate:
  - car: Car
  - spot: Spot
  - status: enum, Created, Paid
  - paymentAmount:

## 一个重要的设计原则，尽量减少 class 之间的 decency，我们使用了 vehicle 这种 parent class

## 如果是 OOD 面试，可以去问面试官，需要我画图吗？还是 coding 就 OK

## singleton 设计

- 用 java，设计一个 singleton class
- 你设计的方法，有啥缺陷，多线程的时候？
- 那么，加 synchronized，进行加锁，影响性能
- 在 web 系统中，什么时候，会用 singleton，DB，configuration 的类

## 在 OOD 面试最后，也需要自己有一个 dry run，自己写一个 test case，自己测试代码的正确性
