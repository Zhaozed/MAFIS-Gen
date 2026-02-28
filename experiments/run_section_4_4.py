'''
Description: Behavioral Fidelity Analysis for Section 4.4
Author: Zhao zeyu
Date: 2026-03-01 03:35:44
LastEditors: Zhao zeyu
LastEditTime: 2026-03-01 03:40:40
FilePath: /MAFIS-Gen/experiments/run_section_4_4.py
'''
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Add generated code directory to system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'generated_outputs')))
try:
    from AirportRevenueFIS import AirportRevenueFIS
except ImportError:
    print("❌ Import failed. Please run the M2T generator with the original JSON first to generate AirportRevenueFIS.py.")
    sys.exit(1)

def run_experiment_4_4():
    print("🚀 Initializing Original System (AirportRevenueFIS) for Section 4.4...")
    fis = AirportRevenueFIS()
    
    # ---------------------------------------------------------
    # 1. Logical Consistency with Rule Base (Table 4.4)
    # ---------------------------------------------------------
    print("\n📊 --- 4.4.1 Logical Consistency Validation (Table 4.4) ---")
    scenarios = {
        'A': {'sat': 1.5, 'wait': 0.5, 'expected_rule': 'R1', 'expected_range': 'Little (0-30)'},
        'B': {'sat': 1.5, 'wait': 4.0, 'expected_rule': 'R3', 'expected_range': 'Average (30-60)'},
        'C': {'sat': 3.0, 'wait': 2.5, 'expected_rule': 'R5', 'expected_range': 'Average (30-60)'},
        'D': {'sat': 3.0, 'wait': 4.5, 'expected_rule': 'R6', 'expected_range': 'Average (30-60)'},
        'E': {'sat': 4.5, 'wait': 4.5, 'expected_rule': 'R9', 'expected_range': 'Great (60-90)'}
    }
    
    print(f"{'Scenario':<10} | {'Satisfaction':<15} | {'Waiting_Time':<15} | {'Output':<10} | {'Conforms?'}")
    print("-" * 70)
    
    # Data collection for the heatmap in 4.4.3
    activation_matrix = []
    
    for key, data in scenarios.items():
        output = fis.evaluate(data['sat'], data['wait'])
        
        # Simple check for expected output range
        conforms = "✓"
        if "Little" in data['expected_range'] and not (0 <= output <= 30): conforms = "✗"
        if "Average" in data['expected_range'] and not (30 < output <= 60): conforms = "✗"
        if "Great" in data['expected_range'] and not (60 < output <= 90): conforms = "✗"
            
        print(f"{key:<10} | {data['sat']:<15} | {data['wait']:<15} | {output:<10.2f} | {conforms}")
        
        # Collect activation strengths for this scenario (9 rules)
        activations = fis.get_rule_activations(data['sat'], data['wait'])
        activation_matrix.append(activations)

    # ---------------------------------------------------------
    # 2. Sensitivity Analysis (Figure 4.9)
    # ---------------------------------------------------------
    print("\n📈 --- 4.4.2 Generating Sensitivity Analysis (Figure 4.9) ---")
    wait_times = [0.5, 2.5, 4.5]
    satisfaction_range = np.arange(1.0, 5.5, 0.5)
    
    plt.figure(figsize=(8, 5))
    markers = ['o', 's', '^']
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
    
    for i, wait in enumerate(wait_times):
        consumptions = []
        for sat in satisfaction_range:
            consumptions.append(fis.evaluate(sat, wait))
        plt.plot(satisfaction_range, consumptions, marker=markers[i], color=colors[i], 
                 label=f'Waiting_Time = {wait}', linewidth=2)
                 
    # plt.title('Figure 4.9: Sensitivity Analysis', fontsize=14)
    plt.xlabel('Satisfaction (1.0 - 5.0)', fontsize=12)
    plt.ylabel('Predicted Consumption (0 - 90)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.ylim(0, 100)
    
    fig_4_9_path = os.path.join(os.path.dirname(__file__), 'figure_4_9_sensitivity.png')
    plt.savefig(fig_4_9_path, dpi=300, bbox_inches='tight')
    print(f"✅ Figure 4.9 saved to: {fig_4_9_path}")

    # ---------------------------------------------------------
    # 3. Rule Activation Heatmap (Figure 4.10)
    # ---------------------------------------------------------
    print("\n🔥 --- 4.4.3 Generating Rule Activation Heatmap (Figure 4.10) ---")
    plt.figure(figsize=(10, 6))
    
    # Convert to numpy array and transpose so that Y-axis = rules (R1-R9), X-axis = scenarios (A-E)
    data_array = np.array(activation_matrix).T 
    
    scenario_labels = ['A', 'B', 'C', 'D', 'E']
    rule_labels = [f'R{i}' for i in range(1, 10)]
    
    # Draw heatmap using seaborn
    sns.heatmap(data_array, annot=True, fmt=".2f", cmap="YlOrRd", 
                xticklabels=scenario_labels, yticklabels=rule_labels,
                cbar_kws={'label': 'Activation Strength'})
                
    # plt.title('Figure 4.10: Rule Activation Heatmap across Scenarios', fontsize=14)
    plt.xlabel('Test Scenarios', fontsize=12)
    plt.ylabel('Rules', fontsize=12)
    
    fig_4_10_path = os.path.join(os.path.dirname(__file__), 'figure_4_10_heatmap.png')
    plt.savefig(fig_4_10_path, dpi=300, bbox_inches='tight')
    print(f"✅ Figure 4.10 saved to: {fig_4_10_path}")
    
    plt.show()

if __name__ == "__main__":
    run_experiment_4_4()