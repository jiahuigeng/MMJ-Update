python generate_completions.py --model_name llava_v1_5l --test_cases_path test_cases/vis4adv/vis4adv.json --save_path visadv_llava15l.json
python evaluate_completions_full.py --completions_path visadv_llava15l.json --save_path visadv_llava15l_eval.json --include_advbench_metric


python generate_visav_test_case.py --data safebench --save_path test_cases/llava15_advbench 
python generate_completions.py --model_name llava_v1_5 --test_cases_path test_cases/llava15_advbench/testcase_safebench.csv --save_path vissafe_llava15.json

python generate_test_cases.py --method_name Visual_Adv   --save_dir ./test_cases/llava15_unconstraint


python evaluate_completions_full.py --completions_path  vissafe_llava15.json --save_path  vissafe_llava15_eval.json --include_advbench_metric
