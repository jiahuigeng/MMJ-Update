import os
import json
import pandas as pd


def main():
    img_name = "bad_prompt.bmp"
    df_input = pd.read_csv("data/advbench/harmful_behaviors_1.csv")
    save_path = os.path.join("test_cases", "vis4adv", "vis4adv.json")
    
    test_cases = {}
    for idx, row in df_input.iterrows():
        behavior_id = idx
        behavior = row['goal']
        current_test_case = ['bad_prompt.bmp', behavior]
        test_cases[behavior_id] = current_test_case
        
    os.makedirs(os.path.dirname(save_path), exist_ok=True) if os.path.dirname(save_path) else None
    with open(save_path, 'w') as file:
        json.dump(test_cases, file, indent=2)
        


if __name__ == '__main__':
    main()