import time
from tqdm import tqdm

def tqdm_progress():
    for i in tqdm(range(1, 60)):
        ''' 假设code执行0.1s '''
        time.sleep(0.1)

if __name__ == '__main__':
    tqdm_progress()