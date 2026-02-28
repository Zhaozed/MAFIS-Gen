# ==============================================================================
# AUTOMATICALLY GENERATED CODE
# Generator: FIS MDE Framework (M2T Engine)
# Description: Interpretable Reasoning Kernel
# Inference Type: Mamdani
# ==============================================================================

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class AirportRevenueFIS:
    def __init__(self):
        # 1. Define Variables (Antecedents and Consequents)
        
        self.satisfaction = ctrl.Antecedent(np.arange(1.0, 5.1, 0.1), 'Satisfaction')
        
        self.waiting_time = ctrl.Antecedent(np.arange(0.0, 5.1, 0.1), 'Waiting_Time')
        
        
        self.consumption = ctrl.Consequent(np.arange(0, 91, 1), 'Consumption')
        
        #  Dynamic injection deblurring method (Centroid -> centroid, etc.)
        self.consumption.defuzzify_method = 'centroid'
        

        # 2. Define Membership Functions
        
        
        
        self.satisfaction['Low'] = fuzz.gaussmf(self.satisfaction.universe, 1.5, 0.5)
        
        
        
        self.satisfaction['Medium'] = fuzz.gaussmf(self.satisfaction.universe, 3.0, 0.5)
        
        
        
        self.satisfaction['High'] = fuzz.gaussmf(self.satisfaction.universe, 4.5, 0.3)
        
        
        
        
        
        self.waiting_time['Low'] = fuzz.trimf(self.waiting_time.universe, [0, 0, 1.8])
        
        
        
        self.waiting_time['Medium'] = fuzz.trimf(self.waiting_time.universe, [1.2, 2.25, 3.3])
        
        
        
        self.waiting_time['High'] = fuzz.trimf(self.waiting_time.universe, [2.7, 4.0, 5.0])
        
        
        
        
        
        self.consumption['Little'] = fuzz.trimf(self.consumption.universe, [0, 0, 30])
        
        
        
        self.consumption['Average'] = fuzz.trimf(self.consumption.universe, [30, 45, 60])
        
        
        
        self.consumption['Great'] = fuzz.trimf(self.consumption.universe, [60, 90, 90])
        
        
        

        # 3. Define Rule Base
        self.rules = []
        
        # Rule R1 (Weight: 1.0, Connection: AND)
        rule_r1 = ctrl.Rule(
            # Dynamically select logical operators: & (AND) or | (OR)
            self.satisfaction['Low'] & self.waiting_time['Low'],
            self.consumption['Little']
        )
        self.rules.append(rule_r1)
        
        # Rule R2 (Weight: 1.0, Connection: AND)
        rule_r2 = ctrl.Rule(
            # Dynamically select logical operators: & (AND) or | (OR)
            self.satisfaction['Low'] & self.waiting_time['Medium'],
            self.consumption['Little']
        )
        self.rules.append(rule_r2)
        
        # Rule R3 (Weight: 1.0, Connection: AND)
        rule_r3 = ctrl.Rule(
            # Dynamically select logical operators: & (AND) or | (OR)
            self.satisfaction['Low'] & self.waiting_time['High'],
            self.consumption['Average']
        )
        self.rules.append(rule_r3)
        
        # Rule R4 (Weight: 1.0, Connection: AND)
        rule_r4 = ctrl.Rule(
            # Dynamically select logical operators: & (AND) or | (OR)
            self.satisfaction['Medium'] & self.waiting_time['Low'],
            self.consumption['Little']
        )
        self.rules.append(rule_r4)
        
        # Rule R5 (Weight: 1.0, Connection: AND)
        rule_r5 = ctrl.Rule(
            # Dynamically select logical operators: & (AND) or | (OR)
            self.satisfaction['Medium'] & self.waiting_time['Medium'],
            self.consumption['Average']
        )
        self.rules.append(rule_r5)
        
        # Rule R6 (Weight: 1.0, Connection: AND)
        rule_r6 = ctrl.Rule(
            # Dynamically select logical operators: & (AND) or | (OR)
            self.satisfaction['Medium'] & self.waiting_time['High'],
            self.consumption['Average']
        )
        self.rules.append(rule_r6)
        
        # Rule R7 (Weight: 1.0, Connection: AND)
        rule_r7 = ctrl.Rule(
            # Dynamically select logical operators: & (AND) or | (OR)
            self.satisfaction['High'] & self.waiting_time['Low'],
            self.consumption['Average']
        )
        self.rules.append(rule_r7)
        
        # Rule R8 (Weight: 1.0, Connection: AND)
        rule_r8 = ctrl.Rule(
            # Dynamically select logical operators: & (AND) or | (OR)
            self.satisfaction['High'] & self.waiting_time['Medium'],
            self.consumption['Great']
        )
        self.rules.append(rule_r8)
        
        # Rule R9 (Weight: 1.0, Connection: AND)
        rule_r9 = ctrl.Rule(
            # Dynamically select logical operators: & (AND) or | (OR)
            self.satisfaction['High'] & self.waiting_time['High'],
            self.consumption['Great']
        )
        self.rules.append(rule_r9)
        

        # 4. Initialize Control System
        self.system = ctrl.ControlSystem(self.rules)
        self.simulation = ctrl.ControlSystemSimulation(self.system)

    def evaluate(self, satisfaction_val, waiting_time_val):
        """Standard evaluation method."""
        
        self.simulation.input['Satisfaction'] = satisfaction_val
        
        self.simulation.input['Waiting_Time'] = waiting_time_val
        
        try:
            self.simulation.compute()
            return self.simulation.output['Consumption']
        except KeyError:
            return 0.0

    def get_rule_activations(self, satisfaction_val, waiting_time_val):
        """
        Dynamically generated method to extract internal activation strengths for White-box interpretation.
        Required for generating Figure 4.8 and 4.10 in the paper.
        """
        # Calculate individual memberships
        
        
        sat_low = fuzz.interp_membership(self.satisfaction.universe, self.satisfaction['Low'].mf, satisfaction_val)
        
        sat_medium = fuzz.interp_membership(self.satisfaction.universe, self.satisfaction['Medium'].mf, satisfaction_val)
        
        sat_high = fuzz.interp_membership(self.satisfaction.universe, self.satisfaction['High'].mf, satisfaction_val)
        
        
        
        wai_low = fuzz.interp_membership(self.waiting_time.universe, self.waiting_time['Low'].mf, waiting_time_val)
        
        wai_medium = fuzz.interp_membership(self.waiting_time.universe, self.waiting_time['Medium'].mf, waiting_time_val)
        
        wai_high = fuzz.interp_membership(self.waiting_time.universe, self.waiting_time['High'].mf, waiting_time_val)
        
        

        # Calculate rule strengths
        return [
            
            # Dynamically select either min (AND) or max (OR) and multiply by the Rule Weight!
            min(sat_low, wai_low) * 1.0,  # R1
            
            # Dynamically select either min (AND) or max (OR) and multiply by the Rule Weight!
            min(sat_low, wai_medium) * 1.0,  # R2
            
            # Dynamically select either min (AND) or max (OR) and multiply by the Rule Weight!
            min(sat_low, wai_high) * 1.0,  # R3
            
            # Dynamically select either min (AND) or max (OR) and multiply by the Rule Weight!
            min(sat_medium, wai_low) * 1.0,  # R4
            
            # Dynamically select either min (AND) or max (OR) and multiply by the Rule Weight!
            min(sat_medium, wai_medium) * 1.0,  # R5
            
            # Dynamically select either min (AND) or max (OR) and multiply by the Rule Weight!
            min(sat_medium, wai_high) * 1.0,  # R6
            
            # Dynamically select either min (AND) or max (OR) and multiply by the Rule Weight!
            min(sat_high, wai_low) * 1.0,  # R7
            
            # Dynamically select either min (AND) or max (OR) and multiply by the Rule Weight!
            min(sat_high, wai_medium) * 1.0,  # R8
            
            # Dynamically select either min (AND) or max (OR) and multiply by the Rule Weight!
            min(sat_high, wai_high) * 1.0 # R9
            
        ]