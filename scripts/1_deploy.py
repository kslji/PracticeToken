from brownie import PracticeToken
from scripts.helpfull_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")


def main():
    account = get_account()
    Practice_token = PracticeToken.deploy(initial_supply, {"from": account})
    print(Practice_token.name())
