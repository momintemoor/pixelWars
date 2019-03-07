package tests

import model._
import org.scalatest._

class testBulletSpeed extends FunSuite{
  test("tests 2"){
    var b1: Bullet = new Bullet(new TwoDvector(2.0,2.0), new TwoDvector(1.0, 2.0), 20.0)
    assert(compute.bulletSpeed(b1) == 2.2)

    var b2: Bullet = new Bullet(new TwoDvector(1.0, 1.0), new TwoDvector(5.3, 2.1), 12.0)
    assert(compute.bulletSpeed(b2) == 5.7)

    var b3: Bullet = new Bullet(new TwoDvector(2.0,2.0), new TwoDvector(0.0, 0.0), 30.0)
    assert(compute.bulletSpeed(b3) == 0.0)

    var b4: Bullet = new Bullet(new TwoDvector(2.0,2.0), new TwoDvector(58.0, 21.0), 10.0)
    assert(compute.bulletSpeed(b4) == 61.7)

    var b5: Bullet = new Bullet(new TwoDvector(2.0,2.0), new TwoDvector(127.0, 83.0), 10.0)
    assert(compute.bulletSpeed(b5) == 151.7)

    var b6: Bullet = new Bullet(new TwoDvector(2.0,2.0), new TwoDvector(0.0, 6.2), 20.0)
    assert(compute.bulletSpeed(b6) == 6.2)

  }
}
