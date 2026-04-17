import numpy as np
import matplotlib.pyplot as plt
import os

# Create images directory if not exists
os.makedirs('images', exist_ok=True)

def plot_vector_diagram():
    # Values from report
    V1_abs = 190
    I_abs = 13.909
    phi_deg = -17.9  # Capacitive (I leads V1)
    
    # Phases (degrees)
    psi_v1 = 0
    psi_i = -phi_deg
    psi_ur = psi_i
    psi_ul = psi_i + 90
    psi_uc = psi_i - 90
    
    # Abs values for voltages
    UR_abs = 180.81
    UL_abs = 47.19
    UC_abs = 105.56
    
    # Scaling for current to make it visible on the same plot
    I_scale = (V1_abs / I_abs) * 0.5
    
    vectors = [
        (V1_abs, psi_v1, 'V_1', 'red', 2),
        (UR_abs, psi_ur, 'U_R', 'blue', 2),
        (UL_abs, psi_ul, 'U_L', 'green', 2),
        (UC_abs, psi_uc, 'U_C', 'purple', 2),
        (I_abs * I_scale, psi_i, 'I', 'black', 3),
    ]
    
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.axhline(0, color='black', lw=0.5)
    ax.axvline(0, color='black', lw=0.5)
    
    for length, angle_deg, label, color, width in vectors:
        angle_rad = np.deg2rad(angle_deg)
        x = length * np.cos(angle_rad)
        y = length * np.sin(angle_rad)
        
        ax.annotate('', xy=(x, y), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color=color, lw=width, mutation_scale=20))
        
        # Adjust label position to avoid overlap
        ha = 'left' if np.cos(angle_rad) >= 0 else 'right'
        va = 'bottom' if np.sin(angle_rad) >= 0 else 'top'
        
        # Manual offsets for specific labels
        off_x, off_y = 5, 5
        if label == 'I':
            off_x, off_y = -15, -15 # Move I label away from UR
            ha = 'right'
            va = 'top'
        elif label == 'U_R':
            off_x, off_y = 15, 15
        elif label == 'V_1':
            off_y = 0
            va = 'center'
        
        label_text = f'${label}$'
        if label == 'I':
            label_text = r'$\dot{I} \cdot k_I$'
            
        ax.text(x + np.sign(x)*off_x if x!=0 else off_x, 
                y + np.sign(y)*off_y if y!=0 else off_y, 
                label_text, fontsize=14, color=color,
                fontweight='bold', ha=ha, va=va)

    ax.set_aspect('equal')
    max_val = max(V1_abs, UR_abs, UL_abs, UC_abs) * 1.2
    ax.set_xlim(-max_val, max_val)
    ax.set_ylim(-max_val, max_val)
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_title('Векторная диаграмма токов и напряжений (RLC)', fontsize=16)
    
    plt.tight_layout()
    plt.savefig('images/vector_3_2_B.png', dpi=300)
    plt.close()

def plot_triangles():
    # Resistance triangle
    R = 13
    XL = 3.393
    XC = 7.590
    X = XL - XC
    Z = np.sqrt(R**2 + X**2)
    
    # Power triangle
    P = 2515
    Q = -812
    S = np.sqrt(P**2 + Q**2)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot Resistance triangle
    ax1.annotate('', xy=(R, 0), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color='blue', lw=2, mutation_scale=15))
    ax1.annotate('', xy=(R, X), xytext=(R, 0), arrowprops=dict(arrowstyle='->', color='red', lw=2, mutation_scale=15))
    ax1.annotate('', xy=(R, X), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color='black', lw=2, mutation_scale=15))
    
    # Force autoscale to see vectors
    ax1.plot([0, R, R], [0, 0, X], alpha=0)
    
    ax1.text(R/2, 0.5, '$R=13$ Ом', ha='center', va='bottom', fontsize=12, color='blue')
    ax1.text(R + 0.5, X/2, f'$X={X:.2f}$ Ом', ha='left', va='center', fontsize=12, color='red')
    ax1.text(R/2 - 1, X/2 - 0.5, f'$|Z|={Z:.2f}$ Ом', ha='right', va='top', rotation=np.rad2deg(np.arctan2(X, R)), fontsize=12)
    
    ax1.set_title('Треугольник сопротивлений', fontsize=14)
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)
    
    # Plot Power triangle
    ax2.annotate('', xy=(P, 0), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color='blue', lw=2, mutation_scale=15))
    ax2.annotate('', xy=(P, Q), xytext=(P, 0), arrowprops=dict(arrowstyle='->', color='red', lw=2, mutation_scale=15))
    ax2.annotate('', xy=(P, Q), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color='black', lw=2, mutation_scale=15))
    
    # Force autoscale to see vectors
    ax2.plot([0, P, P], [0, 0, Q], alpha=0)
    
    ax2.text(P/2, 50, f'$P={P}$ Вт', ha='center', va='bottom', fontsize=12, color='blue')
    ax2.text(P + 100, Q/2, f'$Q={Q}$ ВАр', ha='left', va='center', fontsize=12, color='red')
    ax2.text(P/2 - 100, Q/2 - 50, f'$S={S:.0f}$ ВА', ha='right', va='top', rotation=np.rad2deg(np.arctan2(Q, P)), fontsize=12)
    
    ax2.set_title('Треугольник мощностей', fontsize=14)
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.3)
    
    # Explicitly set limits with a bit of margin
    ax1.set_xlim(-1, R + 5)
    ax1.set_ylim(min(X, 0) - 2, max(X, 0) + 2)
    
    ax2.set_xlim(-100, P + 500)
    ax2.set_ylim(min(Q, 0) - 200, max(Q, 0) + 200)
    
    plt.tight_layout()
    plt.savefig('images/triangles_3_2_B.png', dpi=300)
    plt.close()

if __name__ == '__main__':
    plot_vector_diagram()
    plot_triangles()
    print("Diagrams generated successfully.")
