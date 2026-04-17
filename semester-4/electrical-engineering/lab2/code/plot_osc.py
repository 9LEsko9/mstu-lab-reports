import numpy as np
import matplotlib.pyplot as plt
import os

def load_scp(file_path):
    with open(file_path, 'r', encoding='latin-1') as f:
        lines = f.readlines()
    header_idx = -1
    for i, line in enumerate(lines):
        if 'Time' in line and 'Channel_A' in line:
            header_idx = i
            break
    if header_idx == -1: header_idx = 7
    time, a, b, c = [], [], [], []
    for line in lines[header_idx+2:]:
        parts = line.split()
        if len(parts) >= 4:
            try:
                time.append(float(parts[0])); a.append(float(parts[1]))
                b.append(float(parts[2])); c.append(float(parts[3]))
            except ValueError: continue
    return np.array(time), np.array(a), np.array(b), np.array(c)

def plot_osc_style(time, a, b, c, title, filename, labels, period_ms):
    # Oscilloscope style: dark background
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Colors like a real oscilloscope
    colors = ['#FFFF00', '#00FF00', '#00FFFF'] # Yellow, Green, Cyan
    data = [a, b, c]
    
    t_ms = time * 1000
    for i in range(3):
        ax.plot(t_ms, data[i], label=labels[i], color=colors[i], lw=1.5)
        
        # Find peak for annotation (using first period found in data)
        t_start = t_ms.min()
        mask = (t_ms >= t_start) & (t_ms <= t_start + period_ms)
        
        if any(mask):
            peak_idx = np.argmax(data[i][mask])
            peak_t = t_ms[mask][peak_idx]
            peak_v = data[i][mask][peak_idx]
            
            # Add marker and label
            ax.plot(peak_t, peak_v, 'o', color=colors[i], markersize=4)
            ax.annotate(f'{peak_v:.1f}V', xy=(peak_t, peak_v), xytext=(5, 5),
                        textcoords='offset points', color=colors[i], fontsize=10, fontweight='bold')
    
    # ... (grid and style code)
    
    # Limits
    ax.set_xlim(t_ms.min(), t_ms.min() + period_ms * 2.5)
    
    # Add measurements box
    props = dict(boxstyle='round', facecolor='black', alpha=0.8, edgecolor='#888888')
    info_text = ""
    for i, l in enumerate(labels):
        t_start = t_ms.min()
        mask = (t_ms >= t_start) & (t_ms <= t_start + period_ms)
        if any(mask):
            val = np.max(data[i][mask])
            info_text += f"{l} (pk): {val:.2f} V\n"
    
    ax.text(1.02, 0.5, info_text, transform=ax.transAxes, fontsize=11,
            verticalalignment='center', bbox=props, color='white', fontfamily='monospace')

    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    plt.style.use('default')

def run():
    if os.path.exists('data/3.2Б.scp'):
        t, a, b, c = load_scp('data/3.2Б.scp')
        plot_osc_style(t, a, b, c, 'Oscillogram: RLC Circuit (90 Hz)', 
                       'images/osc_B_labeled.png', ['$V_1$', '$u_L$', '$u_R$'], 1/90*1000)
        print("Oscillogram B updated.")

    if os.path.exists('data/3.2V.scp'):
        t, a, b, c = load_scp('data/3.2V.scp')
        plot_osc_style(t, a, b, c, 'Oscillogram: Different Frequencies', 
                       'images/osc_V_labeled.png', ['$V_1$', '$J\\cdot 1\\Omega$', '$u_3$'], 1/90*1000)
        print("Oscillogram V updated.")

    if os.path.exists('data/3.2G.scp'):
        t, a, b, c = load_scp('data/3.2G.scp')
        plot_osc_style(t, a, b, c, 'Oscillogram: Same Frequency', 
                       'images/osc_G_labeled.png', ['$V_1$', '$J\\cdot 1\\Omega$', '$u_3$'], 1/90*1000)
        print("Oscillogram G updated.")

if __name__ == '__main__':
    run()
