package towers.model.game_objects

import play.api.libs.json.{JsValue, Json}
import towers.model.genetics.genes.Gene
import towers.model.physics.PhysicsVector

import scala.collection.mutable.ListBuffer

class DodgeBallTower(val x: Int, val y: Int) extends GameObject {

  // The height at which projectiles are fired
  val height = 3.0

  // Towers can only fire at players closer than this distance from the tower
  val sightRange = 5.0

  // The magnitude of the velocity at which projectiles are fired
  val projectileVelocity = 5.0

  def fire(jsonGameState: String): List[Projectile] = {
    // TODO: Objective 2
    var min: Double = 10000000000.00
    val player_list : ListBuffer[Player] = ListBuffer()
    val gs = Json.parse(jsonGameState)
    var new_player: Player = null
    val players = (gs \ "players").as[List[JsValue]]
    val proj_list: ListBuffer[Projectile] = ListBuffer()

    if(players.nonEmpty) {
      for (player <- players) {
        //extract player details
        val x = (player \ "x").as[Double]
        val y = (player \ "y").as[Double]
        val v_x = (player \ "v_x").as[Double]
        val v_y = (player \ "v_y").as[Double]
        val id = (player \ "id").as[String]

        val p = new Player(new PhysicsVector(x, y), new PhysicsVector(v_x, v_y))
        player_list += p
        //append player list
      }

      for (player <- player_list) {
        var distance = player.location.distance2d(new PhysicsVector(x + 0.5, y + 0.5))
        //find minimum distance between player and tower and use that player
        if (distance < min) {
          min = distance
          new_player = player
        }
      }

      var direction = new PhysicsVector(new_player.location.x - (x + 0.5), new_player.location.y - (y + 0.5)).normal2d()
      //find direction of player from tower
      if (min < this.sightRange) {
        var projectile = new Projectile(new PhysicsVector(x + 0.5, y + 0.5, height), new PhysicsVector(direction.x * this.projectileVelocity, direction.y * this.projectileVelocity))
        //create projectile to be fired
        proj_list += projectile
      }
    }

    proj_list.toList
  }


  def aimFire(jsonGameState: String): List[Projectile] = {
    // TODO: Bonus Objective
    List()
  }


  // Suggested Genetic Algorithm setup
  def getFitnessFunction(targetPlayer: Player): PhysicsVector => Double = {
    null
  }

  def vectorIncubator(genes: List[Gene]): PhysicsVector = {
    null
  }

}
