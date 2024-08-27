public class Level{

}

public class ParkingLotSingleton{
    private ParkingLotSingleton instance = null;
    private List<Level> levels;

    private ParkingLotSingleton(){
        this.levels = new ArrayList<Level>();
    }

    // The issue of this design is: when multithreading, it may cause race condition and 
    // create more than one instances
    // how to soleve it，对这个方法加锁，make it thread safe
    // public static synchronized ParkingLotSingleton getInstance(){
    public static ParkingLotSingleton getInstance(){
        if (this.instance == null){
            this.instance = new ParkingLotSingleton();
        }  
        
        return this.instance;
    }

}

// 静态内部类
public class ParkingLot{
    // constructor
    private PakringLot(){};

    private static class LazyParkingLot{
        static final ParkingLot instance = new PakringLot();
    }

    public static getInstance(){
        return LazyParkingLot.instance;
    }
}