import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def gradient_descent(x_init, y_init, learning_rate=0.1, max_iter=50):
    x, y = x_init, y_init
    history = [(x, y)]
    
    for i in range(max_iter):
        loss = x**2 + y**2
        grad_x = 2 * x
        grad_y = 2 * y
        x = x - learning_rate * grad_x
        y = y - learning_rate * grad_y
        history.append((x, y))
        if loss < 1e-6:
            break
    
    return np.array(history)

def gradient_descent_momentum(x_init, y_init, learning_rate=0.1, beta=0.9, max_iter=50):
    x, y = x_init, y_init
    vx, vy = 0, 0
    history = [(x, y)]
    
    for i in range(max_iter):
        grad_x = 2 * x
        grad_y = 2 * y
        vx = beta * vx + learning_rate * grad_x
        vy = beta * vy + learning_rate * grad_y
        x = x - vx
        y = y - vy
        history.append((x, y))
        loss = x**2 + y**2
        if loss < 1e-6:
            break
    
    return np.array(history)

def objective_function(x, y):
    return x**2 + y**2

def plot_optimization_path(history):
    fig, ax = plt.subplots(figsize=(10, 8))
    
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)
    Z = objective_function(X, Y)
    
    contour = ax.contour(X, Y, Z, levels=20, cmap='viridis', alpha=0.4)
    ax.clabel(contour, inline=True, fontsize=10)
    
    ax.plot(history[:, 0], history[:, 1], 'ro-', 
           linewidth=3, markersize=6, label='Trajetória do Gradiente')
    
    ax.plot(history[0, 0], history[0, 1], 'bo', 
           markersize=15, label='Ponto Inicial', zorder=5)
    
    ax.plot(0, 0, 'g*', markersize=25, label='Mínimo Global', zorder=5)
    
    for i in range(0, len(history)-1, 5):
        ax.annotate('', xy=(history[i+1, 0], history[i+1, 1]), 
                   xytext=(history[i, 0], history[i, 1]),
                   arrowprops=dict(arrowstyle='->', color='red', lw=2))
    
    ax.set_xlabel('x', fontsize=14, fontweight='bold')
    ax.set_ylabel('y', fontsize=14, fontweight='bold')
    ax.set_title('Gradient Descent', 
                fontsize=16, fontweight='bold')
    ax.legend(loc='upper right', fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    
    plt.tight_layout()
    return fig

def plot_3d_surface(history):
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    x = np.linspace(-3, 3, 50)
    y = np.linspace(-3, 3, 50)
    X, Y = np.meshgrid(x, y)
    Z = objective_function(X, Y)
    
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6, 
                          edgecolor='none', antialiased=True)
    
    z_history = [objective_function(x, y) for x, y in history]
    ax.plot(history[:, 0], history[:, 1], z_history, 
           'ro-', linewidth=3, markersize=6, label='Trajetória')
    
    ax.scatter(history[0, 0], history[0, 1], z_history[0], 
              color='red', s=200, marker='o', label='Início')
    ax.scatter(history[-1, 0], history[-1, 1], z_history[-1], 
              color='green', s=200, marker='*', label='Final')
    
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_zlabel('f(x, y)', fontsize=12)
    ax.set_title('Superfície da Função Objetivo 3D', fontsize=14, fontweight='bold')
    ax.legend()
    
    fig.colorbar(surf, shrink=0.5, aspect=5)
    
    return fig

if __name__ == "__main__":
    x_init, y_init = -2.0, 3.0
    
    hist_gd = gradient_descent(x_init, y_init, learning_rate=0.1)
    
    plot_optimization_path(hist_gd)
    plot_3d_surface(hist_gd)
    
    plt.show()