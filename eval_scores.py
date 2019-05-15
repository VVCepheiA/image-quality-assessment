import json
import numpy as np
import sys

def main():
    input_file = sys.argv[1]
    with open(input_file) as json_file:  
        data = json.load(json_file)
    scores = [d['mean_score_prediction'] for d in data]
    print('mean:', np.mean(scores))
    print('median:', np.median(scores))
    print('std:', np.std(scores))


if __name__ == "__main__":
    main()