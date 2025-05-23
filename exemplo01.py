from particula import Particula
import matplotlib.pyplot as plt

# Criar a partícula com posição inicial, velocidade, e massa. Posso mudar os parametros
p = Particula(x=0, y=0, vx=10, vy=10, massa=1)


dt = 0.1  # intervalo de tempo
g = -9.8  # aceleração da gravidade (m/s²)

# Simula enquanto a partícula estiver no ar (y >= 0)
while p.y >= 0:
    p.newton(fx=0, fy=p.massa * g, dt=dt)

# mostra o numero de pontos da tragetoria
print("Número de pontos simulados:", len(p.trajetoria_x))

# Plotando a trajetória da partícula
plt.plot(p.trajetoria_x, p.trajetoria_y)
plt.title("Lançamento Oblíquo")
plt.xlabel("Posição x (m)")
plt.ylabel("Posição y (m)")
plt.grid(True)
plt.show()
