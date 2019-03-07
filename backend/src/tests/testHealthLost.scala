package tests

import model._
import org.scalatest._

class testHealthLost extends FunSuite{
  test("tests 3"){
    var p1: Player = new Player(60.0)
    var b1: Bullet = new Bullet(new TwoDvector(2.0, 1.0), new TwoDvector(2.0, 3.0), 5.0)
    assert(compute.healthLost(p1, b1) == 42.0)

    var p2: Player = new Player(0.0)
    assert(compute.healthLost(p2, b1) == 0.0)

    var b2: Bullet = new Bullet(new TwoDvector(1.0, 1.0), new TwoDvector(1.0,1.0), 4.0)
    assert(compute.healthLost(p1, b2) == 54.4)

    var b3: Bullet = new Bullet(new TwoDvector(1.0, 1.0), new TwoDvector(0.0,0.0), 5.0)
    assert(compute.healthLost(p1, b3) == 60.0)

    var b4: Bullet = new Bullet(new TwoDvector(1.0, 1.0), new TwoDvector(1.0,1.0), 100.0)
    assert(compute.healthLost(p1, b4) == 0.0)

    var p3: Player = new Player(100.0)
    var b5: Bullet = new Bullet(new TwoDvector(3.0, 5.0), new TwoDvector(100.0,52.0), 1.0)
    assert(compute.healthLost(p3, b5) == 0.0)

    var b6: Bullet = new Bullet(new TwoDvector(3.0, 5.0), new TwoDvector(100.0,52.0), 0.0)
    assert(compute.healthLost(p3, b6) == 100.0)

    var p4: Player = new Player(-10.0)
    assert(compute.healthLost(p4, b2) == 0.0)
  }
}
