import hashlib
import time

# Define the target difficulty (number of leading zeros in the hash)
target_difficulty = 3

def mine_block(data, difficulty):
    nonce = 0
    prefix = '0' * difficulty
    while True:
        block = data + str(nonce)
        block_hash = hashlib.sha256(block.encode()).hexdigest()
        if block_hash[:difficulty] == prefix:
            return block_hash, nonce
        nonce += 1

# Simulated block data
block_data = "Hi"

start_time = time.time()

# Mine a block with the given data and target difficulty
mined_hash, nonce = mine_block(block_data, target_difficulty)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Mined Hash: {mined_hash}")
print(f"Nonce: {nonce}")
print(f"Elapsed Time: {elapsed_time:.6f} seconds")
