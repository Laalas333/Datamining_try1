import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, difficulty):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = 0
        self.difficulty = difficulty
        self.mined_hash = None

    def mine_block(self):
        prefix = '0' * self.difficulty
        while True:
            block_data = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
            block_hash = hashlib.sha256(block_data.encode()).hexdigest()
            if block_hash[:self.difficulty] == prefix:
                self.mined_hash = block_hash
                return
            self.nonce += 1

class Blockchain:
    def __init__(self, difficulty):
        self.chain = [self.create_genesis_block(difficulty)]
        self.difficulty = difficulty

    def create_genesis_block(self, difficulty):
        return Block(0, "0", int(time.time()), "Genesis Block", difficulty)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.index = len(self.chain)
        new_block.previous_hash = self.get_latest_block().mined_hash
        new_block.difficulty = self.difficulty
        new_block.mine_block()
        self.chain.append(new_block)

# Create a blockchain and add blocks
if __name__ == "__main__":
    difficulty_level = 4  # Adjust the difficulty level as needed
    blockchain = Blockchain(difficulty_level)

    # Add a few blocks
    for i in range(3):
        new_block = Block(0, "", int(time.time()), f"Block {i}", blockchain.difficulty)
        new_block.mine_block()
        blockchain.add_block(new_block)
        print(f"Block {new_block.index} mined: {new_block.mined_hash}")

    # Print the entire blockchain
    for block in blockchain.chain:
        print(f"Block {block.index} - Hash: {block.mined_hash}")
