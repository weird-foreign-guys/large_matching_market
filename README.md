# large_matching_market

136 final project

## Running the simulator

### Good commands to get started quickly

#### Quick test for k=10 delta=3 in the range [10, 100) with step length 10

`python3 start.py -l 10 -u 100 --step 10 -r 1`

#### Running overnight in the lower range ([10, 400)) for a range of ks and deltas

`python3 start.py -l 10 -u 400 --step 10 -r 3 -k 10 20 30 --d 0.05 3 5`

#### Run this Yuto!!!!
## running now
`python3 start.py -r=1 --lower=300 -u=400 --step=10 --debug=1 --meta=True -k 10 15 20 --delta 0.05 1 3`
# TODO
`python3 start.py -r=1 --lower=50 -u=400 --step=10 --debug=1 --meta=True -k 40 --delta 0.05 1 3`