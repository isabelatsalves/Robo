package MyRobo;
import robocode.*;

public class MeuRobo extends Robot {
  
  public void run() {

    while (true) {
    ahead(100);
    turnLeft(90);
    fire(1);
    turnRight(90);
    }
  }
  
  public void onScannedRobot(ScannedRobotEvent event) {
    double distancia = event.getDistance();
    double graus = (getHeading() + event.getBearing()) % 360;
    turnGunRight(graus);
    fire(400 / distancia);
  }
  
  public void onHitByBullet(HitByBulletEvent event) {
    turnRight(90);
    back(100);
  }
  
  public void onHitWall(HitWallEvent event) {
 
    turnRight(180);
    back(100);
  }
}
