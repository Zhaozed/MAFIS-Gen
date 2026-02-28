'''
Description: Flexibility Verification for Section 4.3
Author: Zhao zeyu
Date: 2026-03-01 03:28:25
LastEditors: Zhao zeyu
LastEditTime: 2026-03-01 03:28:26
FilePath: /MAFIS-Gen/experiments/run_section_4_3.py
'''
import sys
import os
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'generated_outputs')))
try:
    from AirportRevenueFIS_Extended import AirportRevenueFIS_Extended
except ImportError:
    print("❌ Import failed. Please run M2T generator with the extended JSON first.")
    sys.exit(1)

def run_extended_experiment():
    print("🚀 Initializing Reconfigured System (AirportRevenueFIS_Extended)...")
    fis = AirportRevenueFIS_Extended()
    
    test_sat = 4.5
    test_wait = 4.5
    test_purpose = 1.0
    
    output = fis.evaluate(test_sat, test_wait, test_purpose)
    print(f"\n📊 --- Execution Verification ---")
    print(f"Inputs: Satisfaction={test_sat}, Waiting_Time={test_wait}, Travel_Purpose={test_purpose} (Leisure)")
    print(f"Predicted Consumption: {output:.2f} (Expected: ~77, within 'Great' range)")
    
    activations = fis.get_rule_activations(test_sat, test_wait, test_purpose)
    
    rule_labels = ["R1", "R2", "R9a (Business)", "R9b (Leisure)"]
    
    print("\n🔍 --- Internal Rule Activations ---")
    for label, act in zip(rule_labels, activations):
        print(f"Rule {label}: {act:.2f}")
        
    print("\n🎨 Generating Figure 4.8 (Rule Activation Profile)...")
    plt.figure(figsize=(8, 5))
    bars = plt.bar(rule_labels, activations, color=['#cccccc', '#cccccc', '#ff9999', '#66b3ff'], edgecolor='black')
    
    plt.title('Figure 4.8: Rule Activations (Leisure Traveller with High Sat & Wait)', fontsize=13)
    plt.xlabel('Rules', fontsize=12)
    plt.ylabel('Activation Strength', fontsize=12)
    plt.ylim(0, 1.1)
    
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.02, f"{yval:.2f}", ha='center', va='bottom')
        
    fig_4_8_path = os.path.join(os.path.dirname(__file__), 'figure_4_8_extended.png')
    plt.savefig(fig_4_8_path, dpi=300, bbox_inches='tight')
    print(f"✅ Figure 4.8 saved to: {fig_4_8_path}")
    
    plt.show()

if __name__ == "__main__":
    run_extended_experiment()