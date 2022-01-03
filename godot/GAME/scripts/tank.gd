tool
extends KinematicBody2D

#aponta para a classe bullet
var pre_bullet = preload("res://scenes/bullet.tscn")
#define a velocidade do tanque
var speed = 200

#grupo das balas
onready var bullet_group = "bullet-"+str(self)

#parametros do export define alias para os nomes das skins
#variavel que define o numero da skin
export (int, "BigHead", "Green", "Huge", "Sand") var bodie = 1 setget set_bodie
#lista de skins
var bodies = [
	"res://sprites/tankBody_bigRed.png",
	"res://sprites/tankBody_green.png",
	"res://sprites/tankBody_huge.png",
	"res://sprites/tankBody_sand.png",	
]

func _ready():
	update()

func set_bodie(val):
	bodie = val
	if Engine.editor_hint:
		update()
func _draw():
	$sprite.texture = load(bodies[bodie])

func _process(delta):
	
	if Engine.editor_hint:
		return 
	#define a movimentação em x e y
	var dir_x = 0
	var dir_y = 0
	if Input.is_action_pressed("ui_left"):
		dir_x -=1
	if Input.is_action_pressed("ui_right"):
		dir_x +=1
	if Input.is_action_pressed("ui_up"):
		dir_y -=1
	if Input.is_action_pressed("ui_down"):
		dir_y +=1
	
	#faz o tanque andar
	move_and_slide(Vector2(dir_x, dir_y) * speed)
	
	#cria um tiro
	if Input.is_action_just_pressed("ui_shoot"):
		
		#verifica quantas balas ja foram geradas na tela
		var bullets = get_tree().get_nodes_in_group(bullet_group).size()
		
		#define que podem exisitr no maximo 10 balas na tela
		if bullets < 3:		
			#cria uma nova bala
			var bullet = pre_bullet.instance()
			
			
			#define a direção da rotação do sprite da bala
			bullet.dir = Vector2(cos(rotation), sin(rotation)).normalized()
			
			#define que a bala sai da mesma posição onde o canhao esta
			bullet.global_position = $barrel/muzzle.global_position
			
			#adiciona o disparo a um grupo do tanque
			bullet.add_to_group(bullet_group)
			#adiciona um disparo ao tanque
			get_parent().add_child(bullet)
			
			#executa a animação de tiro
			$barrel/anim.play()
		
			
	#faz o tanque apontar para o mouse
	look_at(get_global_mouse_position())
		
