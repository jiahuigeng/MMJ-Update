import os
import json
import pandas as pd
import argparse


def main(args):
    img_name = "bad_prompt.bmp"
    if args.data == "advbench":
        df_input = pd.read_csv("data/advbench/harmful_behaviors_1.csv")
    else:
        df_input = pd.read_csv("data/safebench/safebench.csv")
    # save_path = os.path.join("test_cases", "vis4adv", "vis4adv.json")
    save_path = os.path.join(args.save_path, f"testcase_{args.data}.csv")
    test_cases = {}
    for idx, row in df_input.iterrows():
        behavior_id = idx
        if args.data == "advbench":
            behavior = row['goal']
        elif args.data == "safebench":
            behavior = row['question']
        current_test_case = ['bad_prompt.bmp', behavior]
        test_cases[behavior_id] = current_test_case
        
    os.makedirs(os.path.dirname(save_path), exist_ok=True) if os.path.dirname(save_path) else None
    with open(save_path, 'w') as file:
        json.dump(test_cases, file, indent=2)
        


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, default="advbench")
    parser.add_argument("--save_path", type=str, default="test_cases/vis4adv")
    args = parser.parse_args()
    main(args)