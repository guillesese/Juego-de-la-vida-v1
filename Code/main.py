import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation   

GRID_SIZE = 50
ON = 255
OFF = 0


def update(frameNum, img, grid, size):
    # Actualizamos el estado de la cuadricula
    newGrid = grid.copy()
    for i in range(size):
        for j in range(size):
            # Contamos los vecinos vivos
            total = int((grid[i, (j-1)%size] + grid[i, (j+1)%size] +
                         grid[(i-1)%size, j] + grid[(i+1)%size, j] +
                         grid[(i-1)%size, (j-1)%size] + grid[(i-1)%size, (j+1)%size] +
                         grid[(i+1)%size, (j-1)%size] + grid[(i+1)%size, (j+1)%size]) / 255)
            
            # Reglas del juego de la vida
            if grid[i, j] == OFF:
                # celula muerta
                if total == 3:
                    # si tiene exactamente 3 vecinos, nace
                    newGrid[i, j] = ON
            else:
                #celula viva
                if total > 3 or total < 2: 
                    # si tiene mas de 3 vecinos, muere. Sobrepoblacion
                    # si tiene menos de 2 vecinos, muere. Aislamiento
                    newGrid[i, j] = OFF             
    
    # Actualizamos la imagen
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

def main():

    updateInterval = 50

    grid = np.random.choice([ON,OFF],GRID_SIZE*GRID_SIZE,p=[0.2,0.8]).reshape(GRID_SIZE,GRID_SIZE)

    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img,grid,GRID_SIZE,), frames=10, interval=updateInterval,save_count=50)

    plt.show()

if __name__ == '__main__':
    main()
