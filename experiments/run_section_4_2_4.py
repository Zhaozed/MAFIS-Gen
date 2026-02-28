"""
Description: Verification script for Section 4.2.4 (Complete)
Author: Zhao zeyu
Date: 2026-03-01
FilePath: /MAFIS-Gen/experiments/run_section_4_2_4.py
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Force load the latest generated code from the pipeline
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'generated_outputs')))
try:
    from AirportRevenueFIS import AirportRevenueFIS
except ImportError:
    print("❌ Import failed. Please run 'pipeline/m2t_generator.py' first.")
    sys.exit(1)

def run_experiments():
    fis = AirportRevenueFIS()
    
    # ---------------------------------------------------------
    # Experiment 1: Generate data for Table 4.3
    # ---------------------------------------------------------
    scenarios = {
        'A': (1.5, 0.5),
        'B': (1.5, 4.0),
        'C': (3.0, 2.5),
        'D': (3.0, 4.5),
        'E': (4.5, 4.5)
    }
    
    print("📊 --- Table 4.3 Test Data Output ---")
    for name, (sat, wait) in scenarios.items():
        output = fis.evaluate(sat, wait)
        activations = fis.get_rule_activations(sat, wait)
        
        max_act = max(activations) if activations else 0
        dominant_rule_idx = activations.index(max_act) + 1 if activations else -1
        
        print(f"Scenario {name}: Sat={sat}, Wait={wait} | Output={output:.2f} | Dominant Rule=R{dominant_rule_idx} (Activation={max_act:.2f})")
    
    # ---------------------------------------------------------
    # Experiment 2: Generate Figure 4.7b (Scenario E Rule Activations)
    # ---------------------------------------------------------
    print("\n🎨 Generating Figure 4.7b (Scenario E rule activation chart)...")
    act_E = fis.get_rule_activations(4.5, 4.5)
    rules_labels = [f"R{i+1}" for i in range(len(act_E))]
    
    plt.figure(figsize=(8, 5))
    bars = plt.bar(rules_labels, act_E, color='skyblue', edgecolor='black')
    plt.title('Figure 4.7b: Rule Activations for Scenario E (Sat=4.5, Wait=4.5)', fontsize=14)
    plt.xlabel('Rules', fontsize=12)
    plt.ylabel('Activation Strength', fontsize=12)
    plt.ylim(0, 1.1)
    
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.02, f"{yval:.2f}", ha='center', va='bottom')
        
    fig_4_7b_path = os.path.join(os.path.dirname(__file__), 'figure_4_7b_activations.png')
    plt.savefig(fig_4_7b_path, dpi=300, bbox_inches='tight')
    print(f"✅ Figure 4.7b saved to: {fig_4_7b_path}")
    
    # ---------------------------------------------------------
    # Experiment 3: Generate Figure 4.7a (Membership Functions)
    # ---------------------------------------------------------
    print("🎨 Generating Figure 4.7a (Membership function plots)...")
    fig, axes = plt.subplots(3, 1, figsize=(8, 10))
    
    for term_name, term in fis.satisfaction.terms.items():
        axes[0].plot(fis.satisfaction.universe, term.mf, label=term_name, linewidth=2)
    axes[0].set_title("Input: Satisfaction", fontsize=12)
    axes[0].set_ylabel("Membership", fontsize=10)
    axes[0].legend()
    axes[0].grid(True, linestyle='--', alpha=0.6)
    
    for term_name, term in fis.waiting_time.terms.items():
        axes[1].plot(fis.waiting_time.universe, term.mf, label=term_name, linewidth=2)
    axes[1].set_title("Input: Waiting Time", fontsize=12)
    axes[1].set_ylabel("Membership", fontsize=10)
    axes[1].legend()
    axes[1].grid(True, linestyle='--', alpha=0.6)
    
    for term_name, term in fis.consumption.terms.items():
        axes[2].plot(fis.consumption.universe, term.mf, label=term_name, linewidth=2)
    axes[2].set_title("Output: Consumption", fontsize=12)
    axes[2].set_ylabel("Membership", fontsize=10)
    axes[2].legend()
    axes[2].grid(True, linestyle='--', alpha=0.6)
    
    plt.tight_layout()
    fig_4_7a_path = os.path.join(os.path.dirname(__file__), 'figure_4_7a_mfs.png')
    plt.savefig(fig_4_7a_path, dpi=300, bbox_inches='tight')
    print(f"✅ Figure 4.7a saved to: {fig_4_7a_path}")

    # ---------------------------------------------------------
    # Experiment 4: Generate Figure 4.7c (3D Control Surface)
    # ---------------------------------------------------------
    print("🎨 Generating Figure 4.7c (3D Control Surface)...")
    
    # Create a meshgrid using the exact universes from the generated FIS
    sat_univ = fis.satisfaction.universe
    wait_univ = fis.waiting_time.universe
    
    # Sample down the grid a bit for faster plotting if it's too dense
    x, y = np.meshgrid(
        np.linspace(sat_univ.min(), sat_univ.max(), 30),
        np.linspace(wait_univ.min(), wait_univ.max(), 30)
    )
    
    z = np.zeros_like(x)
    
    # Evaluate the FIS on the grid
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            # Our evaluate method already safely handles KeyErrors (dead zones) and returns 0.0
            z[i, j] = fis.evaluate(x[i, j], y[i, j])
            
    fig_3d = plt.figure(figsize=(10, 8))
    ax_3d = fig_3d.add_subplot(111, projection='3d')
    
    surf = ax_3d.plot_surface(x, y, z, cmap=cm.viridis, edgecolor='k', linewidth=0.5, alpha=0.9)
    
    ax_3d.set_title('Figure 4.7c: Control Surface of Consumption', fontsize=14)
    ax_3d.set_xlabel('Satisfaction', fontsize=12)
    ax_3d.set_ylabel('Waiting Time', fontsize=12)
    ax_3d.set_zlabel('Consumption', fontsize=12)
    
    # Add a color bar
    fig_3d.colorbar(surf, ax=ax_3d, shrink=0.5, aspect=10)
    
    fig_4_7c_path = os.path.join(os.path.dirname(__file__), 'figure_4_7c_surface.png')
    plt.savefig(fig_4_7c_path, dpi=300, bbox_inches='tight')
    print(f"✅ Figure 4.7c saved to: {fig_4_7c_path}")
    
    plt.show()

if __name__ == "__main__":
    run_experiments()