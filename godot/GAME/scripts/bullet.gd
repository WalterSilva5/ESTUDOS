extends Area2D
var vel = 400
var dir = Vector2(0, -1) setget set_dir
onready var init_pos = global_position
var max_distance_bullet = 300
var live = true
func _ready():
	pass

func _process(delta):
	if live:
		#apaga o tiro caso ele atinja a distancia maxima de tiro
		if global_position.distance_to(init_pos)>=max_distance_bullet:
			auto_destroy()
		translate(dir*vel*delta)
func auto_destroy():
	#para a emissão de particulas de movimento
			$smoke.emitting = false
			#mata o objeto do tiro
			live = false
			#oculta o sprite da bala 
			$sprite.visible = false
			#executa a animação de explosão
			$anim_self_destruction.play("explode")
			#aguarda a animação finalizar antes de eliminar o objeto do tiro
			yield($anim_self_destruction, "animation_finished")
			#desativa as colisões dos tiros
			call_deferred("set_monitoring", false)
			call_deferred("set_monitorable", false)
			queue_free() 

func set_dir(val):
	dir = val
	rotation = dir.angle()

#apaga o objeto da bala ao sair da tela
func _on_notifier_screen_exited():
	queue_free()


func _on_bullet_body_entered(body):
	if body.collision_layer != 1:
		auto_destroy+()
	
