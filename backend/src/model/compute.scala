package model


object compute {
  def bulletEnd(bullet: Bullet, time: Double): TwoDvector = {
    var xdir : Double = bullet.l.x + (bullet.v.x * time)
    var ydir: Double = bullet.l.y + (bullet.v.y * time)
    var vec : TwoDvector = new TwoDvector(xdir, ydir)
    vec
  }

  def bulletSpeed(bu: Bullet): Double = {
    var speed : Double = Math.sqrt(Math.pow(bu.v.x, 2)+ Math.pow(bu.v.y, 2))
    (math rint speed * 10)/ 10
  }

  def healthLost(p: Player, b: Bullet): Double = {
    if(p.health > 0) {
      var amount: Double = p.health - (b.dmg * bulletSpeed(b))
      if(amount < 0){
        0
      }
      else{
        amount
      }
    }
    else{
      0.0
    }
  }
}
