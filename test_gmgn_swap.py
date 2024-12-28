import requests

def test_gmgn_swap():
    try:
        response = requests.get(GMGN_SWAP_ENDPOINT, params=params)
        if response.status_code == 200:
            data = response.json()
            print("GMGN API Response:", data)
        else:
            print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Parameters and API URL
GMGN_SWAP_ENDPOINT = "https://gmgn.ai/defi/router/v1/sol/tx/get_swap_route"
params = {
    "token_in_address": "So11111111111111111111111111111111111111112",  # SOL token address
    "token_out_address": "7EYnhQoR9YM3N7UoaKRoA44Uy8JeaZV3qyouov87awMs",  # USDC token address
    "in_amount": "100000000",  # 0.1 SOL in lamports
    "from_address": "72zKFuUdiWuJWuEt7kp67EMWnPD2ugbeHTpk9E4cnCWw",  # Your Solana wallet address
    "slippage": 0.5  # Slippage tolerance in percentage
}

# Run the function
if __name__ == "__main__":
    test_gmgn_swap()
