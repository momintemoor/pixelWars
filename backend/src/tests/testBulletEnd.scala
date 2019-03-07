package tests

import model._
import org.scalatest._

class testBulletEnd extends FunSuite {
  test("tests") {
    var b1: Bullet = new Bullet(new TwoDvector(5.0, 4.0), new TwoDvector(2.0, 2.0), 10.0)
    var t1: Double = 1.0
    assert(compute.bulletEnd(b1, t1).x == 7.0)
    assert(compute.bulletEnd(b1, t1).y == 6.0)

    var b2: Bullet = new Bullet(new TwoDvector(123.0, 8.0), new TwoDvector(3.0, 1.0), 10.0)
    var t2: Double = 1.5
    assert(compute.bulletEnd(b2, t2).x == 127.5)
    assert(compute.bulletEnd(b2, t2).y == 9.5)

    var b3: Bullet = new Bullet(new TwoDvector(5.0, 4.0), new TwoDvector(0.0, 0.0), 10.0)
    assert(compute.bulletEnd(b3, t1).x == 5.0)
    assert(compute.bulletEnd(b3, t1).y == 4.0)

    var t3: Double = 0.0
    assert(compute.bulletEnd(b2, t3).x == 123.0)
    assert(compute.bulletEnd(b2, t3).y == 8.0)

    var b4: Bullet = new Bullet(new TwoDvector(0.0, 4.0), new TwoDvector(3.0, 1.0), 10.0)
    var t4: Double = 2.0
    assert(compute.bulletEnd(b4, t4).x == 6.0)
    assert(compute.bulletEnd(b4, t4).y == 6.0)

  }
}
